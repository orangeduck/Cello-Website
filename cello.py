from flask import Flask
from flask import render_template
from flask import Markup

from werkzeug.contrib.cache import MemcachedCache

import os
import markdown

app = Flask(__name__)
app.root_path = os.path.dirname(__file__)

cache = MemcachedCache(['127.0.0.1:11211'])

@app.route('/')
@app.route('/<page>')
@app.route('/<page>/<section>')
def index(page="home", section=None):
    
    if not (page in ["home", "documentation", "contribute"]): page = "home"
    if (page     in ["documentation"] and 
        section in ["types", "containers", "functions", "memory", "exceptions", "hacking"]):
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
