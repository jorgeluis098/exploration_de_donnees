from flask import Flask, render_template, jsonify, request
import pandas as pd
from io import StringIO, BytesIO
from base64 import b64encode
from scipy.spatial import  distance 
import numpy as np
from sklearn.cluster import KMeans
from modulos.tablas import Tabla
from mpl_toolkits.mplot3d import Axes3D
import pickle

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

@app.route('/read_pearson', methods=['POST'])
def processPearson():
    response = {}
    if request.files:
        file_content = request.files["filePearson"].read().decode("utf-8")
        file_name = request.files["filePearson"].filename
        if ( file_name.lower().endswith('txt') ):
            Datos = pd.read_table(StringIO(file_content))
        else: 
            Datos = pd.read_csv(StringIO(file_content))
        Matriz = Datos.corr(method='pearson')
        response["keyPearson"] = Matriz.to_html(table_id='matriz_pearson')
    else:
        raise EnvironmentError('error no hay archivo')
    return jsonify(response)



@app.route("/distancias")
def distancias():
    return render_template("distancias.html")

@app.route('/read_distancias', methods=['POST'])
def processDistancias():
    response = {}
    if request.form:
        lamda = float(request.form["lambda"])
        file_content = request.files["fileDistancias"].read().decode("utf-8")
        file_name = request.files["fileDistancias"].filename
        if ( file_name.lower().endswith('txt') ):
            Datos = pd.read_table(StringIO(file_content))
        else: 
            Datos = pd.read_csv(StringIO(file_content))
        Datos = Datos.drop(['ID'], axis=1)
        matriz_distancias = np.ones((Datos.shape[0],Datos.shape[0]))
        if (request.form['distances'] == "Euclidiana"):
            for i in range( 0, Datos.shape[0]):
                for j in range(0, Datos.shape[0]):
                    dist_1 = Datos.iloc[i]
                    dist_2 = Datos.iloc[j]
                    distancia = distance.euclidean(dist_1,dist_2)
                    matriz_distancias[i][j] = distancia
        if (request.form['distances'] == "Chebyshev"):
            for i in range( 0, Datos.shape[0]):
                for j in range(0, Datos.shape[0]):
                    dist_1 = Datos.iloc[i]
                    dist_2 = Datos.iloc[j]
                    distancia = distance.chebyshev(dist_1,dist_2)
                    matriz_distancias[i][j] = distancia
        if (request.form['distances'] == "Manhattan"):
            for i in range( 0, Datos.shape[0]):
                for j in range(0, Datos.shape[0]):
                    dist_1 = Datos.iloc[i]
                    dist_2 = Datos.iloc[j]
                    distancia = distance.cityblock(dist_1,dist_2)
                    matriz_distancias[i][j] = distancia
        if (request.form['distances'] == "Minkowsky"):
            for i in range( 0, Datos.shape[0]):
                for j in range(0, Datos.shape[0]):
                    dist_1 = Datos.iloc[i]
                    dist_2 = Datos.iloc[j]
                    distancia = distance.minkowski(dist_1,dist_2,lamda)
                    matriz_distancias[i][j] = distancia
        matriz_distancias = np.around(matriz_distancias,2)
        matriz_distancias = pd.DataFrame(matriz_distancias)
        response["keyDistancias"] = matriz_distancias.to_html(table_id='matrizDistanciass')
    else:
        raise EnvironmentError('error no hay archivo')
    return jsonify(response)


@app.route("/k-mean")
def kmean():
    return render_template("k_mean.html")


@app.route('/read_k_means', methods=['POST'])
def processK_means():
    response = {}
    Nclusters = int(request.form["clusters"])
    if request.files:
        file_content = request.files["fileK_means"].read().decode("utf-8")
        file_name = request.files["fileK_means"].filename
        if ( file_name.lower().endswith('txt')):
            Datos = pd.read_table(StringIO(file_content))
        else: 
            Datos = pd.read_csv(StringIO(file_content))
        Datos = Datos.drop(['IDNumber'], axis=1)
        Datos = Datos.drop(['Diagnosis'], axis=1)
        VariablesModelo = Datos.values
        MParticional = KMeans(n_clusters=Nclusters, random_state=0).fit(VariablesModelo)
        MParticional.predict(VariablesModelo)
        MParticional.labels_
        Datos['clusterP'] = MParticional.labels_
        CentroidesP = MParticional.cluster_centers_
        CentroidesP = pd.DataFrame(CentroidesP.round(4))
        response["keyk"] = CentroidesP.to_html(table_id='cen')
    else:
        raise EnvironmentError('error no hay archivo')
    return jsonify(response)

@app.route("/regresion-logistica")
def regresion():
    return render_template("regresionL.html")


@app.route('/regresion', methods=['POST'])
def processRlog():
    response = {}
    if request.form:
        datos = dict(request.form)
        datos = {k:[float(v)] for k,v in datos.items()}
        datos = pd.DataFrame.from_dict(datos)
        with open('Wattson.bb', 'rb') as model_file:
            model = pickle.load(model_file)
        result = model.predict(datos)
        resultados = {0: 'Maligno', 1: 'Benigno'}
        response["keyRL"] = resultados[result[0]]
    else:
        raise EnvironmentError('error no hay archivo')
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

