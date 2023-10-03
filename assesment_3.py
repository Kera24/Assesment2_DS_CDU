# -*- coding: utf-8 -*-
"""Assesment_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FW5ZN-lq0aoCTrqhkU3_RQQvnxTL7XZQ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import explained_variance_score

data= pd.read_csv('/content/po2_data.csv')
data.head(5)

print("First 5 rows of the dataset:")
print(data.head())

print("Summary Statistics:")
print(data.describe())

print("Information about the dataset:")
print(data.info())

print("Missing Values:")
print(data.isnull().sum())

# Visualize the dataset
plt.figure(figsize=(10, 6))
plt.scatter(data['test_time'], data['motor_updrs'])
plt.xlabel('Test time (days)')
plt.ylabel('Motor UPDRS score')
plt.title('Motor UPDRS score vs. test time')
plt.grid(True)
plt.show()

# Example: visualize the relationship between age and motor UPDRS score
plt.scatter(data['age'], data['motor_updrs'])
plt.xlabel('Age')
plt.ylabel('Motor UPDRS Score')
plt.title('Age vs Motor UPDRS Score')
plt.show()

# Prepare the data for modeling
X = data.drop(['motor_updrs', 'total_updrs'], axis=1)  # Features
y_motor = data['motor_updrs']  # Target: Motor UPDRS Score
y_total = data['total_updrs']  # Target: Total UPDRS Score

# Split the data into training and testing sets
X_train, X_test, y_motor_train, y_motor_test, y_total_train, y_total_test = train_test_split(
    X, y_motor, y_total, test_size=0.2, random_state=42)

# Initialize the linear regression model
model_motor = LinearRegression()
model_total = LinearRegression()

# Train the models
model_motor.fit(X_train, y_motor_train)
model_total.fit(X_train, y_total_train)

# Make predictions
motor_predictions = model_motor.predict(X_test)
total_predictions = model_total.predict(X_test)

# Evaluate the models
motor_mse = mean_squared_error(y_motor_test, motor_predictions)
total_mse = mean_squared_error(y_total_test, total_predictions)
motor_r2 = r2_score(y_motor_test, motor_predictions)
total_r2 = r2_score(y_total_test, total_predictions)

# Evaluate the models using explained variance score
motor_explained_variance = explained_variance_score(y_motor_test, motor_predictions)
total_explained_variance = explained_variance_score(y_total_test, total_predictions)

# Make predictions
motor_predictions = model_motor.predict(X_test)
total_predictions = model_total.predict(X_test)

# Calculate Mean Absolute Error
motor_mae = mean_absolute_error(y_motor_test, motor_predictions)
total_mae = mean_absolute_error(y_total_test, total_predictions)

# Print evaluation metrics
print("Motor UPDRS Mean Squared Error:", motor_mse)
print("Total UPDRS Mean Squared Error:", total_mse)
print("Motor UPDRS R-squared:", motor_r2)
print("Total UPDRS R-squared:", total_r2)
print("Motor UPDRS Explained Variance Score:", motor_explained_variance)
print("Total UPDRS Explained Variance Score:", total_explained_variance)
print("Motor UPDRS Mean Absolute Error:", motor_mae)
print("Total UPDRS Mean Absolute Error:", total_mae)

motor_r2 = r2_score(y_motor_test, motor_predictions)
total_r2 = r2_score(y_total_test, total_predictions)
print("Motor UPDRS R-squared:", motor_r2)
print("Total UPDRS R-squared:", total_r2)

# Evaluation metrics
metrics = ['Mean Squared Error (MSE)', 'Mean Absolute Error (MAE)', 'Explained Variance Score']
motor_scores = [motor_mse, motor_mae, motor_explained_variance]
total_scores = [total_mse, total_mae, total_explained_variance]

# Bar chart for Motor UPDRS model
plt.figure(figsize=(10, 6))
plt.bar(metrics, motor_scores, color='skyblue')
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Evaluation Metrics for Motor UPDRS Model')
plt.ylim(0, 1)  # Set the y-axis limit for better visualization
plt.show()

# Bar chart for Total UPDRS model
plt.figure(figsize=(10, 6))
plt.bar(metrics, total_scores, color='lightgreen')
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Evaluation Metrics for Total UPDRS Model')
plt.ylim(0, 1)  # Set the y-axis limit for better visualization
plt.show()

labels = ['Motor UPDRS', 'Total UPDRS']
r2_scores = [motor_r2, total_r2]

# Create bar chart
plt.figure(figsize=(8, 6))
plt.bar(labels, r2_scores, color=['blue', 'green'])
plt.ylim(0, 1)  # R-squared score ranges from 0 to 1
plt.ylabel('R-squared Score')
plt.title('R-squared Score Comparison')
plt.show()