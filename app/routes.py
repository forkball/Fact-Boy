from flask import render_template, request
from bs4 import BeautifulSoup
from datetime import datetime
from app import app
import requests

wiki = "https://en.wikipedia.org/wiki/"

@app.route('/')
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

@app.route("/fact")
def fact():
    subject = request.args.get('subject')
    webpage = requests.get(wiki + subject)
    soup = BeautifulSoup(webpage.content)
    body = soup.find("div", {"class": "mw-parser-output"})
    return render_template('fact.html', title='Fact Boy',subject = body)