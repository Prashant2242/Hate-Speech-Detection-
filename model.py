# backend/model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset
data = {
    'text': [
        'I love you', 
        'You are amazing', 
        'I hate you', 
        'You are stupid', 
        'Such a wonderful day', 
        'You are a loser'
    ],
    'label': [0, 0, 1, 1, 0, 1]  # 0 = Not Hate, 1 = Hate Speech
}

df = pd.DataFrame(data)

# Features and Labels
X = df['text']
y = df['label']

# Text Vectorization
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model and vectorizer
joblib.dump(model, 'model/hate_speech_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Model and vectorizer saved!")
