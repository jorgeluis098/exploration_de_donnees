from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nav")
def navegation():
    return render_template("nav.html")

if __name__ == "__main__":
    app.run(debug=True)

