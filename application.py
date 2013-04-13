from flask import Flask
from flask import render_template
from flask import Markup

import markdown

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="index"):
    try:
        content = open("pages/"+name+".md").read()
    except:
        content = open("pages/index.md").read()
    content = Markup(markdown.markdown(content))
    return render_template('page.html', content=content)

app.run(debug=True)
