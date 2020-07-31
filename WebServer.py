import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
	return flask.render_template("main.html")

@app.route("/hermir")
def hermir():
	return flask.render_template("canvas.html")

if __name__ == "__main__":
	app.run(debug=True,host='127.0.0.1', port=80)