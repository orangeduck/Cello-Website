from flask import Flask
from flask import render_template
from flask import Markup

from werkzeug.contrib.cache import MemcachedCache

import os
import markdown

from doc.cello_classes import cello_classes
from doc.cello_types import cello_types

app = Flask(__name__)
app.root_path = os.path.dirname(__file__)

try:
    cache = MemcachedCache(['127.0.0.1:11211'])
except RuntimeError:
    
    class FakeCache:
        def get(self, k): return None
        def set(self, k, v, **kwargs): return None
        
    cache = FakeCache()
    
@app.route('/')
@app.route('/<page>')
@app.route('/<page>/<section>')
def index(page="home", section=None):
    
    if not (page in ["home", "documentation", "contribute", "reference"]): page = "home"
    
    if (page in ["documentation"] and 
        section  in 
        ["types", "containers", "functions",
        "memory", "exceptions", "hacking", 
        "comparison", "installation", "celloworld",
        "values", "parents"]):
        
        section = "_"+section
        
    elif (page in ["reference"] and
        
        section in map(lambda k: k.lower(), cello_classes.keys()) or
        section in map(lambda k: k.lower(), cello_types.keys())):
        section = "_"+section
        
    else:
        section = ""
    
    filename = os.path.join(app.root_path, "pages", page + section + ".md")

    content = cache.get("libcello-" + filename)
    if content is None:
        f = open(filename)
        content = f.read()
        f.close()
        content = markdown.markdown(content)
        content = content.replace(
          "<pre><code>", 
          "<pre><code data-language=\"libcello\">")
        content = content.replace(
          "<h3>",  "<h3 class='text-center' style='margin-bottom:20px;'>")
        
        content = content.replace("</h1>", "</h1><hr/>")
        content = Markup(content)
        cache.set("libcello-" + filename, content, timeout=5*60)

    return render_template('page.html', content=content)

if __name__ == "__main__":
    app.run(debug=True)
