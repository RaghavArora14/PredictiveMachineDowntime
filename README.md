# Manufacturing Downtime Predictor

**Manufacturing Downtime Predictor** is a web-based application designed to predict machine downtime or production defects in a manufacturing environment. The application utilizes machine learning models trained on historical and real-time machine data to provide actionable insights, helping optimize production efficiency and reduce unplanned downtime.

## Objective
This project was developed to meet the following goals:

1. Build a predictive analysis model for manufacturing data.
2. Create RESTful API endpoints to enable uploading of data, model training, and prediction generation.
3. Provide an interactive front-end for users to interact with the application.

## Features
- **Data Upload**: Upload manufacturing data in CSV format.
- **Model Training**: Train machine learning models (Logistic Regression, Decision Tree, or Support Vector Machine) using uploaded data.
- **Downtime Prediction**: Predict machine downtime based on operational features and return predictions with confidence scores.
- **Synthetic Data Generation**: Generate manufacturing data with key fields like `Machine_ID`, `Temperature`, `Run_Time`, and `Downtime_Flag`.
- **RESTful API Endpoints**: Interact with the system programmatically to automate workflows.
- **Performance Metrics**: Provide detailed metrics such as accuracy, precision, recall, and F1-score after model training.
- **Download Synthetic Dataset**: Easily download generated synthetic datasets for testing and development purposes.
- **Interactive Front-End**: A user-friendly front-end built using HTML, CSS, and JavaScript for seamless user interaction.
- **Image Uploads for Documentation**: Users can upload images to visualize and document the application’s working interface.

## Key Technologies
- **Backend Framework**: Python Flask
- **Frontend Technologies**: HTML, CSS, JavaScript
- **Machine Learning Library**: scikit-learn
- **Data Handling**: pandas

## Files in the Project

### 1. `app.py`
This is the main Flask application that handles the server-side logic of the project. It serves the front-end, manages data uploads, model training, and prediction, and interacts with the machine learning models through API endpoints.

- **Key functionality**:
  - Routes and serves the web application using Flask.
  - Handles file uploads and dataset parsing.
  - Trains machine learning models using the uploaded dataset (`Logistic Regression`, `Decision Tree`, or `SVM`).
  - Makes predictions based on user input and the trained model.
  - Exposes RESTful APIs for uploading data, training models, generating predictions, and downloading synthetic data.

### 2. `model.py`
This file contains the `ModelTrainer` class, which is responsible for training the machine learning models and making predictions. It uses the `scikit-learn` library to build, train, and evaluate models like Logistic Regression, Decision Tree, and Support Vector Machine.

- **Key functionality**:
  - Handles the training of the machine learning models.
  - Prepares data for model training by splitting it into training and testing sets.
  - Trains models and evaluates them using metrics like accuracy, precision, recall, and F1-score.
  - Makes predictions based on input features.

### 3. `index.html`
This is the main front-end HTML file that provides the structure of the web interface. It allows users to upload datasets, train models, and make predictions. The file also includes buttons for navigating between different sections (uploading data, training models, and making predictions).

- **Key functionality**:
  - Defines the layout and structure of the web interface.
  - Includes forms for uploading data, selecting a machine learning model, and inputting feature values for predictions.
  - Dynamically generates the input fields for making predictions based on the dataset's features.

### 4. `script.js`
This file contains the JavaScript code that manages the dynamic interactions between the front-end and the Flask back-end. It updates the user interface in real-time based on user input and server responses, ensuring a smooth and responsive user experience.

- **Key functionality**:
  - Handles user interactions, including uploading data, selecting model types, and submitting prediction requests.
  - Dynamically generates input fields for making predictions based on the features of the uploaded dataset.
  - Sends asynchronous HTTP requests (using the `fetch` API) to the Flask back-end for uploading data, training machine learning models, and fetching predictions.
  - Updates the UI with success or error messages after processing data on the server.
  - Manages tab navigation and dynamically displays different sections of the user interface based on user selection.

### 5. `style.css`
This file contains the CSS styles for the web interface. It defines the visual appearance of the web application, including layouts, buttons, and form styles. It ensures that the application is user-friendly and visually appealing.

- **Key functionality**:
  - Styles the web page for a clean and professional look.
  - Defines the layout for different sections of the application (e.g., Upload, Train Model, Predict).
  - Provides styles for buttons, forms, and messages displayed on the web interface.

### 6. `data_gen.py`
This script is responsible for generating synthetic operational data for machines. It simulates various features such as temperature, run time, torque, and tool wear, and then assigns a downtime flag (`Downtime_Flag`) based on predefined conditions. The generated dataset is saved as a CSV file.

- **Key functionality**:
  - Generates machine data with features: `Machine_ID`, `Temperature`, `Run_Time`, `Torque`, and `Tool_Wear`.
  - Assigns the `Downtime_Flag` based on specific conditions (e.g., high temperature, long run time, high torque).
  - Saves the generated data to a CSV file (`machine_data.csv`).

### Synthetic Dataset
This CSV file contains the synthetic dataset generated by `data_gen.py`. It includes the following columns:
  - **Machine_ID**: Unique identifier for each machine.
  - **Temperature**: The operating temperature of the machine (°C).
  - **Run_Time**: Total run time of the machine (minutes).
  - **Torque**: The applied torque to the machine (Newton-meters).
  - **Tool_Wear**: The wear level of the machine's tool.
  - **Downtime_Flag**: A binary flag indicating if the machine is likely to experience downtime (`1` for downtime, `0` for no downtime).

## API Endpoints
The application exposes the following endpoints:

### 1. `/upload` (POST)
Uploads a CSV file containing manufacturing data and selects the target variable for prediction.
- **Input**:
  - Form-data with:
    - `file`: The CSV file containing data.
    - `target`: The target column to predict (e.g., `Downtime_Flag`).
- **Output**:
  ```json
  {
    "message": "Dataset uploaded successfully",
    "features": ["Feature1", "Feature2", ...],
    "target": "Target"
  }
  ```

### 2. `/train` (POST)
Trains the machine learning model on the uploaded dataset.
- **Input**:
  ```json
  {
    "model_type": "lr" // Options: "lr" (Logistic Regression), "dt" (Decision Tree), "svm" (Support Vector Machine)
  }
  ```
- **Output**:
  ```json
  {
    "message": "Model trained successfully",
    "metrics": {
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1_score": 1.0
    }
  }
  ```

### 3. `/predict` (POST)
Accepts feature inputs and returns a prediction along with confidence.
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
- **Output**:
  ```json
  {
    "prediction": "Yes",
    "confidence": 0.89
  }
  ```

### 4. `/generate-data` (POST)
Generates synthetic manufacturing data for testing.
- **Output**: CSV file for download.

### Example Requests and Outputs
#### Upload Data
```bash
curl -X POST -F "file=@data.csv" -F "target=Downtime_Flag" http://127.0.0.1:5000/upload
```
**Expected Output:**
```json
{
  "message": "Dataset uploaded successfully",
  "features": ["Temperature", "Run_Time", "Torque", "Tool_Wear"],
  "target": "Downtime_Flag"
}
```

#### Train Model
```bash
curl -X POST -H "Content-Type: application/json" -d '{"model_type": "dt"}' http://127.0.0.1:5000/train
```
**Expected Output:**
```json
{
  "message": "Model trained successfully",
  "metrics": {
    "accuracy": 1.0,
    "precision": 1.0,
    "recall": 1.0,
    "f1_score": 1.0
  }
}
```

#### Make Prediction
```bash
curl -X POST -H "Content-Type: application/json" -d '{"features": {"Temperature": 95.0, "Run_Time": 450, "Torque": 65.5, "Tool_Wear": 180}}' http://127.0.0.1:5000/predict
```
**Expected Output:**
```json
{
  "prediction": "Yes",
  "confidence": 0.93
}
```

#### Download Synthetic Data
```bash
curl -X POST http://127.0.0.1:5000/generate-data --output synthetic_data.csv
```
**Expected Output:**
A CSV file named `synthetic_data.csv` will be downloaded containing simulated manufacturing data.

## Explanation of API and RESTful Principles
### What is a RESTful API?
REST (Representational State Transfer) is a software architectural style for creating scalable web services. A RESTful API uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on data.

Key principles of REST include:
1. **Statelessness**: Each request from a client must contain all necessary information for the server to process it.
2. **Resource Identification**: Resources are identified using URLs (e.g., `/upload`, `/train`).
3. **Standard Methods**: REST uses standard HTTP methods like GET, POST, PUT, and DELETE.
4. **Representation**: Data can be sent in formats like JSON, XML, or HTML.

### How This Application Uses Flask for RESTful APIs
Flask is a lightweight web framework in Python that simplifies the creation of RESTful APIs. In this application:
1. **Endpoints**: Flask routes (e.g., `@app.route('/upload', methods=['POST'])`) define specific API operations.
2. **Request Handling**: The `request` object is used to handle input data (e.g., JSON, form-data).
3. **Responses**: The `jsonify` function is used to return structured JSON responses to clients.

For example, the `/train` endpoint:
- Accepts JSON input specifying the model type.
- Processes the data and trains the model using scikit-learn.
- Returns performance metrics as a JSON response.

## Usage Workflow
1. **Upload Data**: Navigate to the Upload tab, upload a dataset, and specify the target variable.
2. **Train the Model**: Select a machine learning algorithm and initiate model training. View performance metrics upon completion.
3. **Make Predictions**: Input feature values into the Predict tab to get a prediction for machine downtime.
4. **Download Synthetic Dataset**: Use the "Generate Data" feature to create and download synthetic data.
5. **Upload Images**: Upload images of the UI in action to document functionality.
   
## Dynamic Front-End Functionality
The front-end of the application dynamically updates the input fields for predictions based on the uploaded dataset and selected target variable. Using JavaScript:
- **Input Generation**: When a dataset is uploaded, the front-end retrieves the feature names via the `/upload` API.
- **Dynamic Forms**: HTML elements for each feature are generated dynamically, ensuring the user can input values for all required fields.
- **Target Selection**: The target variable is highlighted and removed from the input fields to avoid confusion.
- **Real-Time Updates**: The interface adapts automatically when new data is uploaded or the target is changed.

This dynamic functionality ensures a seamless user experience and reduces the potential for errors during prediction input.
## UI Screenshots
![image](https://github.com/user-attachments/assets/4aae5110-e956-4e03-966a-78058925d439)
![image](https://github.com/user-attachments/assets/73edbf1f-c4c0-48a5-a5f3-a379afdfbb36)
![image](https://github.com/user-attachments/assets/f9eb0d09-b618-408f-b018-a15d65305663)

## Explanation of Model Choices
The application supports three machine learning models, each chosen for its suitability to manufacturing data:

### Logistic Regression (LR)
- **Rationale**: Logistic Regression is effective for linearly separable data and provides probabilistic predictions. It is used here for simplicity and interpretability.
- **Performance**: Achieved 95.50% accuracy on synthetic data, making it a strong baseline for linearly dependent datasets.

### Decision Tree (DT)
- **Rationale**: Decision Trees naturally handle non-linear relationships and interactions between features. For this dataset, which shows non-linear dependency on temperature and run-time, the Decision Tree achieved high accuracy.
- **Performance**: Achieved perfect metrics (100% for accuracy, precision, recall, and F1 score) on the synthetic dataset.

### Support Vector Machine (SVM)
- **Rationale**: SVM is suited for high-dimensional and complex decision boundaries. By using a non-linear kernel, it effectively separates challenging datasets.
- **Performance**: Achieved 97.75% accuracy, with precision of 92.31%, recall of 60.00%, and F1-score of 72.73% on the synthetic dataset.

### Train-Test Split
The data is split into 80% for training and 20% for testing to evaluate model performance effectively. This ensures a reliable estimate of how the model will perform on unseen data.

## Contributors
- [Raghav Arora](https://github.com/RaghavArora14)

## License
This project is licensed under the Apache License 2.0.

