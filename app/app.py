# ----- app.py -----
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Charger le modèle
model_path = os.environ.get('MODEL_PATH', '../immoSense.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    """Affiche la page d'accueil"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API de prédiction"""
    try:
        # Récupérer les données JSON
        data = request.get_json()
        
        # Convertir en DataFrame
        input_data = pd.DataFrame([data])
        
        # Faire la prédiction
        prediction = model.predict(input_data)
        
        # Retourner le résultat
        return jsonify({
            'success': True,
            'prediction': prediction.tolist(),
            'input_data': data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
