from flask import render_template, request
from datetime import datetime
from app import app

import wikipedia
import random

@app.route('/')
def index():
    greeting = getGreeting()
    return render_template('index.html', title='Fact Boy',greeting = greeting)

@app.route("/fact")
def fact():
    greeting = getGreeting()
    subject = request.args.get('subject')
    fact = getFact(subject)
    return render_template('index.html', title='Fact Boy',greeting = greeting, subject = subject, content = fact)

def getFact(subject):
    fact = None
    try:
        fact = wikipedia.summary(subject, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        return getFact(e.options[random.randint(0,len(e.options) - 1)])
    except wikipedia.exceptions.HTTPTimeoutError as e:
        return "Can't connect to Wikipedia!"
    except wikipedia.exceptions.PageError as e:
        return "I don't know what '" + subject + "' is!"
    else:
        return fact

def getGreeting():
    currentTime = datetime.now().hour
    greetings = ["Evenin' Fact Boy","Afternoon Fact Boy","Mornin' Fact Boy"]
    greeting = ""

    if (currentTime >= 20):
        greeting = greetings[0]
    elif (currentTime >= 12):
        greeting = greetings[1]
    else:
        greeting = greetings[2]
    
    return greeting
