import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
	return flask.render_template("main.html")

if __name__ == "__main__":
	app.run(debug=True,host='192.168.1.124', port=80)