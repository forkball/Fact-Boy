from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import wikipedia
import random
import requests

app = Flask(__name__)
app.config.from_pyfile('config.py')

#loop until exception free
def getFact(subject):
    fact = None
    try:
        fact = {
            "title": wikipedia.page(subject).title,
            "fact": wikipedia.summary(subject,sentences=1),
            "src": getSrc(subject)
        }
    except wikipedia.exceptions.DisambiguationError as e:
        return getFact(e.options[random.randint(0,len(e.options) - 1)])
    except (wikipedia.exceptions.HTTPTimeoutError, requests.exceptions.ConnectionError) as e:
        return "Can't connect to Wikipedia!"
    except wikipedia.exceptions.PageError as e:
        return "I don't know what '" + subject + "' is!"
    else:
        return fact

#gets source of subject       
def getSrc(subject):
    return wikipedia.page(subject).url

#gets greeting depending on day
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


#index route, landing page
@app.route('/')
def index():
    greeting = getGreeting()
    return render_template('index.html', title='Fact Boy', greeting = greeting)

#fact route, handles fact generation
@app.route("/fact")
def fact():
    greeting = getGreeting()
    #retrieve subject arg
    subject = request.args.get('subject')
    
    #if there is no subject, redirect
    if not (subject):
        return redirect(url_for('index'))

    fact = getFact(subject)
    #render template, pass greeting, subject, and fact dict
    return render_template('index.html', title='Fact Boy',greeting = greeting, subject = subject, content = fact)

if __name__ == "__main__":
    app.run(debug=True)