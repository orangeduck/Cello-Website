from flask import Flask
from flask import render_template
from flask import Markup

import markdown

app = Flask(__name__)

@app.route('/')
@app.route('/<page>')
@app.route('/<page>/<section>')
def index(page="home", section=None):
    
    if not (page in ["home", "documentation"]): page = "home"
    
    if (page    in ["documentation"] and 
        section in ["functions", "types", "memory", "exceptions"]):
        section = "_"+section
    else:
        section = ""
    
    content = open("pages/"+page+section+".md").read()
        
    content = markdown.markdown(content)
    content = content.replace("<pre><code>", "<pre><code data-language=\"libcello\">")
    content = content.replace("</h2>", "</h2><hr/>")
    content = Markup(content)
    
    return render_template('page.html', content=content)

app.run(debug=True)
