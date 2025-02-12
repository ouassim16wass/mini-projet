# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Charger les modèles
rf_model = joblib.load('models/rf_model.pkl')
dt_model = joblib.load('models/dt_model.pkl')
ann_model = joblib.load('models/ann_model.pkl')

# Fonction pour prédire
def make_prediction(model, data):
    return model.predict(data)

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données envoyées par la requête
    content = request.get_json()
    
    # Convertir les données en DataFrame
    input_data = pd.DataFrame(content)

    # Exemple de prédiction avec tous les modèles
    rf_pred = make_prediction(rf_model, input_data)
    dt_pred = make_prediction(dt_model, input_data)
    ann_pred = make_prediction(ann_model, input_data)

    # Retourner les résultats en JSON
    return jsonify({
        'rf_prediction': rf_pred.tolist(),
        'dt_prediction': dt_pred.tolist(),
        'ann_prediction': ann_pred.tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
