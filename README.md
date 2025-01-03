
# Random Forest Prediction App

This repository contains the code for a Streamlit app that predicts the percentage increase in value of a property based on the number of years since a specific event ("Walsh"). 
The app was inspired by a Facebook post (shown below) discussing the trend of property value increases. The original poster used linear regression to model the trend, 
which prompted the creation of this app to explore the application of other machine learning models.

**Original Facebook Post:**

![image](https://github.com/user-attachments/assets/d588a76f-628a-4d09-9541-822d7c5d4f0b)

## Motivation

The Facebook post sparked me to try to replicate the trend of the property value increase that the poster shared. This app aims to contribute to that discussion by:

* **Reproducing the original plot:** Approximated data points from the plot were used to recreate the visualization.
* **Exploring different models:** Linear Regression, Decision Tree, and Random Forest models were applied to the data to analyze the trend.
* **Providing an interactive prediction tool:** Users can input a future year to see a predicted percentage increase based on the Random Forest model.

## Live App

You can access the live Streamlit app here: https://randomforest-me6powdyqkapxhi2bznfgz.streamlit.app/

## How to run locally

1. **Clone the repository:** `git clone https://github.com/your-username/your-repo-name.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the app:** `streamlit run random_forest_prediction.py`

## App Features

* **Interactive prediction:** Input a year to get a prediction of the percentage increase.
* **Model visualization:** See a scatter plot of the data and the model's predictions.
* **R-squared value:**  Displays the R-squared value of the model to indicate its performance.

## Dependencies

* numpy
* streamlit
* scikit-learn
* matplotlib

## Note

The data points used in this app are approximated from the original plot shared by Tom Ricketts on Facebook and may not be completely accurate. This app is intended for demonstration and discussion purposes only.

