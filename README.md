

# Manufacturing Downtime Predictor

**Manufacturing Predictor** is a web-based application designed to help manufacturers predict machine downtime and prevent potential failures using machine learning models. It uses historical and real-time data from machines to predict when a machine is likely to fail or require maintenance, which can help optimize factory operations, reduce unplanned downtime, and improve productivity.

This application leverages powerful machine learning algorithms, such as Logistic Regression, Decision Trees, and Support Vector Machines, to train models that predict downtime based on various operational features such as temperature, run-time, torque, and tool wear.

## Features

- **Interactive Web Interface**: A user-friendly web interface that allows easy interaction with the system, making it simple to upload data, train models, and make predictions.
- **Multiple Machine Learning Models**: The application supports three popular machine learning algorithms, each with different strengths and use cases:
  - Logistic Regression (LR)
  - Decision Trees (DT)
  - Support Vector Machine (SVM)
- **Real-Time Model Training & Evaluation**: The app allows users to train models and immediately view their performance metrics, such as accuracy, precision, recall, and F1 score.
- **Synthetic Data Generation**: Generate synthetic manufacturing data to simulate machine behavior, enabling testing of models and predictions when real data is unavailable or insufficient.
- **RESTful API Endpoints**: Exposes a set of API endpoints for easy integration with external systems and for automated predictions.
- **Model Performance Metrics**: After training, the application provides detailed performance metrics to help users understand how well their models are performing.
- **Responsive Design**: The web interface adapts to various screen sizes, making it easy to use on desktops, tablets, and smartphones.

## Installation

### Prerequisites
To run the Manufacturing Predictor app, ensure you have the following installed:

- **Python 3.8 or higher**: Python is the programming language used for this project.
- **pip (Python Package Installer)**: This is used to install the necessary dependencies.


### Setup Instructions
1. **Clone the Repository**: Start by cloning the repository to your local machine using Git.
   ```bash
   git clone https://github.com/your-username/manufacturing-predictor.git
   cd manufacturing-predictor
   ```

2. **Install the Required Packages**: Use pip to install the dependencies listed in the `requirements.txt` file. This will ensure all the necessary libraries are available to run the application.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**: Start the Flask application by running:
   ```bash
   python app.py
   ```
   This will start the web server on `http://localhost:5000`.

4. **Access the Web Interface**: Open a web browser and navigate to `http://localhost:5000` to interact with the application.

---

## API Endpoints for Testing

Below are the `curl` commands to test the three key endpoints of the application: Upload Data, Train Model, and Make Prediction.

### 1. Upload Data
- **Endpoint**: `/upload`
- **Method**: POST
- **Input**: 
  - Form data with a CSV file containing the manufacturing data.
  - Target variable name (e.g., `Downtime_Flag`).

#### Command to Upload Data:
```bash
curl -X POST -F "file=@file_path" -F "target=Downtime_Flag" http://127.0.0.1:5000/upload
```
Replace `file_path` with the path to your CSV file,

- **Output**:
  ```json
  {
    "message": "Dataset uploaded successfully",
    "features": ["feature1", "feature2", ...],
    "target": "target_variable"
  }
  ```

### 2. Train Model
- **Endpoint**: `/train`
- **Method**: POST
- **Input**:
  ```json
  {
    "model_type": "lr" // or "dt" or "svm"
  }
  ```

#### Command to Train Model (Logistic Regression):
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"model_type\": \"lr\"}" http://127.0.0.1:5000/train
```

#### Command to Train Model (Decision Tree):
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"model_type\": \"dt\"}" http://127.0.0.1:5000/train
```

#### Command to Train Model (Support Vector Machine):
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"model_type\": \"svm\"}" http://127.0.0.1:5000/train
```

- **Output**:
  ```json
  {
    "message": "Model trained successfully",
    "metrics": {
      "accuracy": 0.95,
      "precision": 0.94,
      "recall": 0.93,
      "f1_score": 0.93
    }
  }
  ```

### 3. Make Prediction
- **Endpoint**: `/predict`
- **Method**: POST
- **Input**:
  ```json
  {
    "features": {
      "Temperature": 85.0,
      "Run_Time": 350,
      "Torque": 45.5,
      "Tool_Wear": 150
    }
  }
  ```

#### Command to Make Prediction:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"features\": {\"Machine_ID\": 1, \"Temperature\": 85.0, \"Run_Time\": 350, \"Torque\": 45.5, \"Tool_Wear\": 150}}" http://127.0.0.1:5000/predict
```

- **Output**:
  ```json
  {
    "prediction": "Yes",
    "confidence": 0.89
  }
  ```

---

## Usage Guide

### 1. Data Upload
- Navigate to the "Upload Data" section.
- Upload a CSV file containing the data for your manufacturing machines. This file should include features such as `Temperature`, `Run_Time`, `Torque`, `Tool_Wear`, and a target variable like `Downtime_Flag` (indicating whether or not the machine experienced downtime).
- After uploading, select the target variable (such as `Downtime_Flag`) to indicate what the model will predict.

### 2. Model Training
- After uploading your data, go to the "Train Model" tab.
- Choose the machine learning model you want to use (Logistic Regression, Decision Tree, or Support Vector Machine).
- Click "Train Model," and the system will start training the selected model on the uploaded data.
- Once training is complete, the application will display performance metrics (accuracy, precision, recall, and F1 score) to help evaluate how well the model is performing.

### 3. Making Predictions
- Go to the "Predict" section of the web interface.
- Enter the values of the features (e.g., `Temperature`, `Run_Time`, `Torque`, `Tool_Wear`) that you want to make predictions for.
- Click "Predict" to get the downtime prediction for your machine along with a confidence score indicating the model's certainty.

---

### Model Details

#### Logistic Regression
- **Use Case**: Best for modeling linear relationships between features and the target variable.
- **Strengths**: Efficient, fast, and easy to implement. Works well when features are independent and linearly related to the target variable.
- **Limitations**: Struggles with non-linear relationships.

#### Decision Tree
- **Use Case**: Works well with non-linear relationships between features and the target variable.
- **Strengths**: Handles non-linear relationships naturally, no feature scaling is required, easy to interpret.
- **Limitations**: Tends to overfit without proper tuning (e.g., limiting the depth of the tree).

#### Support Vector Machine (SVM)
- **Use Case**: Effective for complex problems with high-dimensional feature spaces.
- **Strengths**: Performs well for complex, non-linear classification tasks.
- **Limitations**: Requires more computation and memory, and sensitive to feature scaling.

---

## Performance Considerations
The application is designed to run efficiently even with a large dataset. Data processing and model training are optimized to minimize memory usage and processing time.

---

## Contributing
To contribute to this project:
1. **Fork** the repository on GitHub.
2. Create a **feature branch** for your changes.
3. **Commit** your changes with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a **Pull Request** for review.

