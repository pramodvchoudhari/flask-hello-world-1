from flask import Flask
app =Flask(__name__)

@app.route("/")
def home():
	return "<h1>Hello world 1!</h1>"
