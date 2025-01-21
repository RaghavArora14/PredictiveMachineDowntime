
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelTrainer:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = None
        self.needs_scaling = False

    def prepare_data(self, X, y):
        self.feature_names = list(X.columns)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        if self.needs_scaling:
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
        
        return X_train, X_test, y_train, y_test

    def train(self, X, y, model_type='lr'):
        self.needs_scaling = model_type in ['lr', 'svm']
        
        X_train, X_test, y_train, y_test = self.prepare_data(X, y)
        
        if model_type == 'lr':
            self.model = LogisticRegression()
        elif model_type == 'dt':
            self.model = DecisionTreeClassifier(max_depth=5)
        elif model_type == 'svm':
            self.model = SVC(probability=True)
        
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred)
        }
        
        return metrics

    def predict(self, features):
        if not self.model:
            raise ValueError("Model not trained yet")
            
        # Convert features to correct order based on training data
        feature_array = np.array([[features[fname] for fname in self.feature_names]])
        
        if self.needs_scaling:
            feature_array = self.scaler.transform(feature_array)
            
        prediction = self.model.predict(feature_array)[0]
        confidence = self.model.predict_proba(feature_array)[0].max()
        
        return prediction, confidence