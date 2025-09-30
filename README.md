# 🌸 Iris Classification API - ML Model Deployment

A complete machine learning project demonstrating how to build, train, and deploy a Random Forest classifier as a REST API using Flask.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.3+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.3+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Overview

This project showcases a complete machine learning workflow from model training to production deployment. We use the classic Iris dataset to build a Random Forest classifier that predicts iris flower species based on their physical characteristics, then serve it via a Flask REST API.

## 🎯 Features

- **Machine Learning Pipeline**: Complete workflow from data loading to model training
- **Model Serialization**: Efficient model saving and loading using joblib
- **REST API**: Production-ready Flask web service
- **Comprehensive Testing**: Multiple methods for API validation
- **Detailed Documentation**: Step-by-step guides and explanations

## 🛠️ Technology Stack

- **Python 3.7+**: Core programming language
- **scikit-learn**: Machine learning library
- **Flask**: Web framework for API development
- **joblib**: Model serialization
- **NumPy**: Numerical computations

## 📁 Project Structure

```
API_MLmodel/
├── API_MLmodel.ipynb    # Main notebook with complete workflow
├── model.py            # Flask API server
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
└── assets/            # Project assets and screenshots
    └── postman.png    # Postman API testing screenshot
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd API_MLmodel
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask scikit-learn joblib numpy
   ```

4. **Train the model (optional)**
   ```bash
   jupyter notebook API_MLmodel.ipynb
   ```
   Run all cells to train and save the model.

5. **Start the API server**
   ```bash
   python3 model.py
   ```

The API will be available at `http://127.0.0.1:5000` (When you start the server you will get your own URL)

## 🌐 API Usage

### Endpoint
```
POST http://127.0.0.1:5000/predict
```

### Request Format
```json
{
    "input": [sepal_length, sepal_width, petal_length, petal_width]
}
```

### Response Format
```json
{
    "prediction": class_id
}
```

### Class Mapping
- `0` → Iris Setosa
- `1` → Iris Versicolor
- `2` → Iris Virginica

## 🧪 Testing Examples

### Using curl
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": [5.1, 3.5, 1.4, 0.2]}'
```

### Using Python requests
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {"input": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=data)
print(response.json())  # {"prediction": 0}
```

### Using Postman
1. Create a new POST request
2. URL: `http://127.0.0.1:5000/predict`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
   ```json
   {
       "input": [5.1, 3.5, 1.4, 0.2]
   }
   ```


## 📊 Sample Test Cases

```json
// Iris Setosa (typically prediction: 0)
{"input": [5.1, 3.5, 1.4, 0.2]}

// Iris Versicolor (typically prediction: 1)
{"input": [6.2, 2.8, 4.8, 1.8]}

// Iris Virginica (typically prediction: 2)
{"input": [7.7, 3.8, 6.7, 2.2]}
```

## 📈 Model Information

### Dataset
- **Source**: Iris dataset from scikit-learn
- **Samples**: 150 iris flowers
- **Features**: 4 (sepal length/width, petal length/width)
- **Classes**: 3 (Setosa, Versicolor, Virginica)

### Algorithm
- **Model**: Random Forest Classifier
- **Training Split**: 70% training, 30% testing
- **Benefits**: Robust performance, feature importance, reduced overfitting

### Feature Ranges
1. **Sepal Length**: 4.3-7.9 cm
2. **Sepal Width**: 2.0-4.4 cm
3. **Petal Length**: 1.0-6.9 cm
4. **Petal Width**: 0.1-2.5 cm

## 🔧 Development

### Requirements
Create a `requirements.txt` file:
```txt
flask==2.3.3
scikit-learn==1.3.0
joblib==1.3.2
numpy==1.24.3
```

### Code Structure
- `API_MLmodel.ipynb`: Interactive notebook with complete workflow
- `model.py`: Flask API server implementation
- `rf_model.pkl`: Serialized Random Forest model

## 🚀 Production Deployment

### Recommendations
- Implement proper error handling and logging
- Add authentication and rate limiting
- Use environment variables for configuration
- Containerize with Docker
- Deploy to cloud platforms (AWS, GCP, Azure)


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
