import numpy as np
from flask import Flask, render_template, request
import math
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Clean input: remove commas and convert to float
        features = [
            float(x.replace(',', ''))
            for x in request.form.values()
        ]

        final_features = np.array(features).reshape(1, -1)

        prediction = model.predict(final_features)

        output = math.floor(prediction[0])

        return render_template(
            'index.html',
            predict_text=f"Number of weekly rides: {output}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            predict_text=f"Input error: Please enter valid numbers only"
        )


if __name__ == "__main__":
    app.run(debug=True)
