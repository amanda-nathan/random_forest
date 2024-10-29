# random_forest_prediction.py

import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Data (approximated points from the original plot) from Facebook post
years = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
percent_increase = np.array([0.2, 5.7, 3.3, 3.0, 2.1, 7.4, 4.9, 7.8, 3.9, 9.1, 4.8, 7.1])


rf_model = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=42)
rf_model.fit(years.reshape(-1, 1), percent_increase)


st.title("Random Forest Prediction App")
st.write("This app predicts % Increase based on years since Walsh using a Random Forest model.")
st.write("The data points are approximated from an original plot.")


rf_predictions = rf_model.predict(years.reshape(-1, 1))
rf_r2 = r2_score(percent_increase, rf_predictions)
st.write(f"Random Forest Model R²: {rf_r2:.4f}")


st.subheader("Predict New % Increase")
new_year = st.number_input("Enter a new year (e.g., 12, 13, etc.):", min_value=0, step=1)
if new_year is not None:
    new_year_array = np.array([[new_year]])
    prediction = rf_model.predict(new_year_array)
    st.write(f"Predicted % Increase for year {new_year}: {prediction[0]:.2f}%")


st.subheader("Model Visualization")
plt.figure(figsize=(10, 6))
plt.scatter(years, percent_increase, color="darkcyan", label="Data Points")
plt.plot(years, rf_predictions, linestyle="--", color="green", label=f"Random Forest (R²={rf_r2:.4f})")
plt.xlabel("Years since Walsh")
plt.ylabel("% Increase")
plt.title("26 Keith St. % Increase vs. Years since Walsh with Random Forest Model")
plt.legend()
st.pyplot(plt)
