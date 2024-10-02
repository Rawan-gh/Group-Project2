import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('LinearRegression.pkl', 'rb') as f:
    model = pickle.load(f)

# Title for the app
st.title('Linear Regression Prediction App')

# Input fields
st.write("Please enter the following details:")

# Get input data from the user
interest_rate = st.number_input('Interest Rate', min_value=0.0, step=0.1)
employment = st.number_input('Employment', min_value=0.0, step=0.1)

# When the user clicks the Predict button
if st.button('Predict'):
    try:
        # Prepare the data for prediction
        data = pd.DataFrame([[interest_rate, employment]], columns=['Interest Rates', 'Employment'])

        # Make the prediction
        prediction = model.predict(data)[0]

        # Display the result
        st.success(f"The predicted value is: {round(prediction, 2)}")
    except ValueError:
        st.error("Invalid Data")
