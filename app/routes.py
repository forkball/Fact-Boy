from flask import render_template
from datetime import datetime
from app import app

@app.route('/')
@app.route('/index')
def index():
    currentTime = datetime.now().hour
    greetings = ["Evenin' Fact Boy","Afternoon Fact Boy","Mornin' Fact Boy"]
    greeting = ""

    if (currentTime >= 20):
        greeting = greetings[0]
    if (currentTime >= 12):
        greeting = greetings[1]
    else:
        greeting = greetings[2]

    return render_template('index.html', title='Fact Boy',greeting = greeting)