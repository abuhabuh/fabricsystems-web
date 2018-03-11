import flask

app = flask.Flask(__name__)


@app.route("/")
def handle_root():
    fp = open('src/static/index.html')
    return fp.read()


@app.route("/health")
def handle_health():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
