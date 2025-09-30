from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# load the model: 
model = joblib.load('rf_model.pkl')

# define a route for making predictions:
@app.route('/predict', methods = ['POST'])
def predict():
    # Get input data from POST request:
    data = request.get_json()
    # Convert input data to numpy array:
    input_data = np.array(data['input']).reshape(1, -1)  
    prediction = model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug = True)