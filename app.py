from flask import Flask, request, jsonify, render_template
from pandas import DataFrame, read_csv
import numpy as np
from os import environ, path, join
from model import ModelTrainer
from data_gen import generate_synthetic_data
import os
app = Flask(__name__)

# Global variables
data = None
target = None
model_trainer = ModelTrainer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_data():
    global data, target
    
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    target = request.form.get('target')
    
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Please upload a CSV file"}), 400
        
    try:
        data = read_csv(file)
        features = list(data.columns)
        
        if target and target not in features:
            return jsonify({"error": "Selected target not found in dataset"}), 400
            
        return jsonify({
            "message": "Dataset uploaded successfully",
            "features": features,
            "target": target
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/train', methods=['POST'])
def train_model():
    global data, target, model_trainer
    
    if data is None:
        return jsonify({"error": "No dataset uploaded"}), 400
        
    if target is None:
        return jsonify({"error": "Target variable not selected"}), 400
        
    model_type = request.json.get('model_type', 'lr')
    if model_type not in ['lr', 'dt', 'svm']:
        return jsonify({"error": "Invalid model type"}), 400
        
    try:
        X = data.drop(columns=[target])
        y = data[target]
        
        metrics = model_trainer.train(X, y, model_type)
        return jsonify({
            "message": "Model trained successfully",
            "metrics": metrics
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    if not model_trainer.model:
        return jsonify({"error": "Model not trained"}), 400
        
    try:
        features = request.json.get('features', {})
        prediction, confidence = model_trainer.predict(features)
        
        return jsonify({
            "prediction": "Yes" if prediction == 1 else "No",
            "confidence": float(confidence)
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/generate-data', methods=['POST'])
def generate_data():
    try:
        df = generate_synthetic_data()
        filename = 'synthetic_manufacturing_data.csv'
        df.to_csv(filename, index=False)
        
        return jsonify({
            "message": "Synthetic data generated successfully",
            "features": list(df.columns),
            "filename": filename
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/upload-generated', methods=['POST'])
def upload_generated():
    global data, target
    try:
        filepath = join('synthetic_manufacturing_data.csv')
        if not path.exists(filepath):
            return jsonify({"error": "Generated data file not found"}), 400
            
        data = read_csv(filepath)
        target = request.json.get('target', 'Downtime_Flag')
        
        if target not in data.columns:
            return jsonify({"error": "Target variable not found in dataset"}), 400
            
        return jsonify({
            "message": "Generated data loaded successfully",
            "features": list(data.columns),
            "target": target
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    model_trainer = ModelTrainer()
    app.run(host='0.0.0.0', port=port)