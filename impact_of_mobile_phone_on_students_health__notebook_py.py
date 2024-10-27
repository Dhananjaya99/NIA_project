# -*- coding: utf-8 -*-
"""Impact_of_Mobile_Phone_on_Students_Health__Notebook.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rYL5Bjqi_Y4IrdkGvtrt90nf5yNTcYRm
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('/content/Impact_of_Mobile_Phone_on_Students_Health(2).csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Handle missing values (if any) by removing or filling them
# For simplicity, we'll drop rows with missing values (if any)
data = data.dropna()

# Basic statistics of the dataset
print("\nStatistical Summary of the dataset:")
print(data.describe())

# Display data types
print("\nData types:")
print(data.dtypes)

# Convert categorical columns (if any) using Label Encoding
labelencoder = LabelEncoder()
for column in data.select_dtypes(include=['object']).columns:
    data[column] = labelencoder.fit_transform(data[column])

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(15, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Pairplot to visualize relationships
sns.pairplot(data)
plt.show()

# Feature Selection and Target Variable
# Assuming the last column is the target (health impact)
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target (health impact)

# Train/Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier (example model)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance Plot
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importance")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.tight_layout()
plt.show()

import joblib

joblib.dump(model, 'Impact_of_Mobile_Phone_on_Students_Health_Model.joblib')

import pickle

filename = 'Impact_of_Mobile_Phone_on_Students_Health_Model.sav'
pickle.dump(RandomForestClassifier, open(filename, 'wb'))