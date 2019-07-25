from flask import Flask

app1 = Flask(__name__)


@app1.route("/")
def index():
    return "March or die! Get ready"


if __name__ == '__main__':  # if current file is executable(script)
    app1.run(port=5000, debug=True)
