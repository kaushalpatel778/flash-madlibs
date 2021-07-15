from flask import Flask,render_template,request
from stories import story
app=Flask(__name__)
app.config['SECRET_KEY'] = "secret"
from flask_debugtoolbar import DebugToolbarExtension

debug = DebugToolbarExtension(app)

@app.route('/')
def ask_questions():
    prompt=story.prompts
    return render_template("questions.html",prompt=prompt)

@app.route('/story')
def show_story():
    text =story.generate(request.args)
    return render_template("story.html",text=text)