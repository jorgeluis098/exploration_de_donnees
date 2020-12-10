from flask import Flask, render_template, jsonify, request
import pandas as pd
from io import StringIO, BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apriori")
def aprior():
    return render_template("apriory.html")


@app.route('/read_apriori', methods=['POST'])
def process():
    response = {}
    import pdb; pdb.set_trace
    if request.form:
        min_sup = float(request.form["support"])/100
        min_conf = float(request.form["confidence"])/100
        min_lif = float(request.form["lift"])
        from apyori import apriori
        rules = apriori(data_config["DATA"].get_apyori_list(), min_support=min_sup, min_confidence=min_conf, min_lift=min_lif, min_length=2)
        rules = list(rules)

        response["html"] = TableHTML(table_class="table table-hover").apriori_table(rules)
    return jsonify(response)

@app.route("/pearson")
def pearso():
    return render_template("pearson.html")

if __name__ == "__main__":
    app.run(debug=True)

