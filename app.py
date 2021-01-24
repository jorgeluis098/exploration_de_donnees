from flask import Flask, render_template, jsonify, request
import pandas as pd
from io import StringIO, BytesIO
from base64 import b64encode


from modulos.tablas import Tabla

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
    if request.form:
        min_sup = float(request.form["supportApriori"])/100
        min_conf = float(request.form["confianzaApriori"])/100
        min_lif = float(request.form["liftApriori"])
        from apyori import apriori
        file_content = request.files["fileApriori"].read().decode("utf-8")
        Datos = pd.read_csv(StringIO(file_content), header=None)
        registros = []
        for i in range(0, Datos.shape[0]):
            registros.append([str(Datos.values[i,j]) for j in range(0, Datos.shape[1])])
        rules = apriori(registros, min_support=min_sup, min_confidence=min_conf, min_lift=min_lif, min_length=2)
        rules = list(rules)
        response["key"] = Tabla(table_clase="table table-hover", table_id="table_apriori").apriori_table(rules)
    return jsonify(response)

@app.route("/pearson")
def pearso():
    return render_template("pearson.html")


@app.route("/distancias")
def distancias():
    return render_template("distancias.html")


@app.route("/k-mean")
def kmean():
    return render_template("k_mean.html")


@app.route("/regresion-logistica")
def regresion():
    return render_template("regresionL.html")

if __name__ == "__main__":
    app.run(debug=True)

