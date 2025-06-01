import numpy as np
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and columns
model = joblib.load('house_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')  # List of all feature columns used in training

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Example: only these features are coming from frontend
    input_data = {
        'GrLivArea': data.get('GrLivArea', 0),
        'OverallQual': data.get('OverallQual', 0),
        'GarageCars': data.get('GarageCars', 0),
        'TotalBsmtSF': data.get('TotalBsmtSF', 0)
    }
    # You can add more default features as needed here if required

    # Turn into a dataframe
    import pandas as pd
    input_df = pd.DataFrame([input_data])

    # One-hot encode and align to model columns
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_df)[0]
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
