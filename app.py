from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apriori")
def aprior():
    return render_template("apriory.html")

@app.route("/pearson")
def pearso():
    return render_template("pearson.html")

if __name__ == "__main__":
    app.run(debug=True)

