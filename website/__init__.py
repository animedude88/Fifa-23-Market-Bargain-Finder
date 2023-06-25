from flask import Flask, render_template
from threading import Thread
from replit import db

app = Flask(__name__)

@app.route('/')
def home():
	
  if not db['playerbase']:
    return "Player Base Loading Up"
  else:
    return render_template("home.html",base = db['playerbase'])

def run():
  app.run(host='0.0.0.0',port=4444)


def keep_alive():
    t = Thread(target=run)
    t.start()