from flask import Flask, request, jsonify
from src.db.db_manager import save_statistics, load_statistics
from src.functions import average_statistics

app = Flask(__name__)


@app.route("/api/prometheus/statistics", methods=["POST"])
def post_statistics():

    try:
        statistic = request.json
        save_statistics(statistic)

        return jsonify(
            {"status": "created",
             "statistic": statistic}
                       )

    except Exception:  # Si el cliente ingresa mal los datos de las statistics tendrá este error
        return jsonify(status=400, description="Bad Request"), 400


@app.route("/api/prometheus/statistics", methods=["GET"])
def get_statistics():
    statistics = load_statistics()

    return jsonify([statistic.serialize() for statistic in statistics])


"""
Creo la variable "statistics" dentro del endpoint statistics GET porque si hago una variable global al inicio del 
archivo quedan guardados en dicha variable los registros del csv al momento de correr el servidor. 

Entonces, si durante el uso de la API cargo una nueva statistic y quiero acceder a las statistics del archivo 
"statistics.csv", en el caso de guardar la variable global, no apareceria la nueva statistic en este endpoint, sino que
aparecerian las que ya estaban guardadas en el archivo csv antes de correr el servidor. 

Guardando la variable dentro del endpoint, cada vez que haga una API call accede al archivo csv y devuelve todos los 
registros que existan en ese momento en el archivo
"""


@app.route("/api/prometheus/statistics/reports", methods=["GET"])
def get_reports():

    statistics = load_statistics()
    report_date = request.args.get("report_date", "")

    # Error en caso de no pasar el parametro report_date
    if report_date == "":
        return jsonify(status=400, description="report_date param needed"), 400

    # Con el uso del elif creo la condicion del formato de "report_date": YYYY-MM-DD
    elif len(report_date) == 10 and report_date[4] == "-" and report_date[7] == "-":

        blood_sugar_levels = []
        emotion_levels = []

        for statistic in statistics:
            if statistic.date == report_date:
                blood_sugar_levels.append(statistic.blood_sugar_level)
                emotion_levels.append(statistic.emotion_level)

        average_blood_sugar_level = average_statistics(blood_sugar_levels)
        average_emotion_level = average_statistics(emotion_levels)

        return jsonify({"avg_blood_sugar_level": average_blood_sugar_level,
                        "avg_emotion_level": average_emotion_level})

    # Si completan el parametro pero el formato es incorrecto, se devuelve el siguiente error
    else:
        return jsonify(status=400, description="Wrong param format. Reformat the param: YYYY-MM-DD"), 400


"""
En el endpoint statistics/reports GET también guardo el registro de statistics dentro del endpoint por el mismo motivo
que el endpoint anterior
"""

"""
Coleccion de Postman:
https://www.postman.com/martucichi/workspace/examen-final/collection/21244850-3a4b2dee-bb44-44c6-82a9-c8ca92d0bc9d?
action=share&creator=21244850
"""
