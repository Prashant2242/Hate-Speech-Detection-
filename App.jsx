// frontend/src/App.js

import React, { useState } from 'react';
import './App.css';
import hateSpeechImg from './assets/hate_speech.png';

function App() {
  const [message, setMessage] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        message: message,
      }),
    });

    const text = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, 'text/html');
    const prediction = doc.querySelector('h2')?.textContent || 'No prediction';
    setResult(prediction);
  };

  return (
    <div className="app">
      <div className="left">
        <h1>Hate Speech Detection</h1>
        <form onSubmit={handleSubmit}>
          <textarea
            placeholder="Write about your Feelings"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            required
          />
          <button type="submit">Submit</button>
        </form>

        {result && <h2>{result}</h2>}
      </div>

      <div className="right">
        <img src={hateSpeechImg} alt="Hate Speech" />
      </div>
    </div>
  );
}

export default App;
