from flask import Flask
from flask import render_template
from flask import Markup

from werkzeug.contrib.cache import MemcachedCache

import os
import markdown

app = Flask(__name__)
app.root_path = os.path.dirname(os.path.realpath(__file__))

import logging
from logging import FileHandler 
file_handler = FileHandler(app.root_path+'/error.log')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

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
    
    if not (page in ["home", "learn"]): page = "home"
    
    print('test', os.path.join(app.root_path, 'doc', 'object-list.md'))
    
    if (page in ["learn"] and 
        section  in 
        ["installation",
         "cello-world",
         "a-fat-pointer-library",
         "cello-vs-cpp-vs-objc",
         "benchmarks",
         "quickstart",
         "queries-and-pitfalls",
         "garbage-collection",
         "best-improvements-of-cello-2.0"] + 
         open(os.path.join(app.root_path, 'doc', 'object-list.md')).read().lower().split(' ')):
        
        section = "-"+section
        
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
        
        content = content.replace("</h1>", "</h1><hr style='margin-bottom:20px;'/>")
        content = Markup(content)
        cache.set("libcello-" + filename, content, timeout=5*60)

    if page == 'home':
        title = 'High Level C'
    else:
        if section != "":
            title = section.replace('-', ' ').title()
        else:
            title = page.replace('-', ' ').title()

    return render_template('page.html', content=content, title=title)

if __name__ == "__main__":
    app.run(debug=False)
