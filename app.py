# backend/app.py

from flask import Flask, request
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load('model/hate_speech_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)[0]
    
    if prediction == 1:
        result = "Hate Speech Detected"
    else:
        result = "No Hate Speech"
        
    return f"<h2>{result}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
