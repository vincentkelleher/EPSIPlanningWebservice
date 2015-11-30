from flask import Flask, jsonify
from flask.ext.pymongo import PyMongo
import json
import os

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route("/cours/")
def cours():
    cours = []
    for planning in mongo.db.planning.find():
        planning["_id"] = str(planning["_id"])
        planning["horaire_debut"] = planning["horaire_debut"].isoformat()
        planning["horaire_fin"] = planning["horaire_fin"].isoformat()

        cours.append(planning)

    return jsonify(data=cours), 200

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))