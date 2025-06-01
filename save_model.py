import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load and preprocess data
df = pd.read_csv('train.csv')
X_raw = df.drop(['SalePrice', 'Id'], axis=1)
y = df['SalePrice']
X = pd.get_dummies(X_raw)
X = X.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

# 2. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Save the trained model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as house_price_model.pkl")

# 4. Save the model columns (feature names)
joblib.dump(X.columns.tolist(), 'model_columns.pkl')
print("Feature columns saved as model_columns.pkl")
