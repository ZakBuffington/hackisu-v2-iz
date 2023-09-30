from flask import Flask, render_template
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def main():
    return render_template("home.html")


@app.route("/", methods = ["POST"])
def FFACalc():

    return render_template("Resultpage.html", result = result)


if __name__ == "__main__":
    app.run()