import flask
from flask import render_template
from flask import request
app = flask.Flask(__name__)


@app.route('/')
def homepage():
	# return("Welcome to the home page new page")
	return render_template("./EzyChair.html")

if __name__ == "__main__" :
	app.run(debug=True)