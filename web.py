import werkzeug
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)
Title = __name__


@app.route('/')
def home():
	return render_template('index.html', title=Title)

def run():
	app.run(host='0.0.0.0', port=6969)


def WebRun():
	t = Thread(target=run)
	t.start()
