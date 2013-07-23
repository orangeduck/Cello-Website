from flask import Flask
from flask import render_template
from flask import Markup

from werkzeug.contrib.cache import MemcachedCache

import os
import markdown

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
    
    if (page     in ["documentation"] and 
        section  in 
        ["types", "containers", "functions", 
        "memory", "exceptions", "hacking", 
        "comparison"]):
        
        section = "_"+section
        
    elif (page     in ["reference"] and
        
        section  in
        ["array", "bool", "char", "dictionary", 
         "file", "function", "list", "map",
         "none", "int", "real", "pool", "reference",
         "string", "table", "tree", "type"] or
         
         section in 
         ["format", "show", "call", "num", "retain",
          "new", "assign", "copy", "eq", "ord", "hash", 
          "collection", "sort", "reverse", "append",
          "iter", "push", "at", "dict", "aschar", "asstr",
          "aslong", "asdouble", "with", "stream", "serialize"] or
          
          section in [
           "exception", "lambda", "value"]):
        
        
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
        content = content.replace("<pre><code>", "<pre><code data-language=\"libcello\">")
        content = content.replace("</h2>", "</h2><hr/>")
        content = content.replace("</h1>", "</h1><hr/>")
        content = Markup(content)
        cache.set("libcello-" + filename, content, timeout=5*60)

    return render_template('page.html', content=content)

if __name__ == "__main__":
    app.run(debug=True)
