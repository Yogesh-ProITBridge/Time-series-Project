import streamlit as st
import pandas as pd
import xgboost as xgb
import pickle
from datetime import datetime, timedelta

# Load the trained model
with open('best_xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the Streamlit app
st.title('Gold Price Prediction')

# Sidebar input for the date
st.sidebar.header('Input Date and Days for Prediction')
selected_date = st.sidebar.date_input('Select a date', datetime.now())
days_ahead = st.sidebar.selectbox('Days ahead for prediction', [2, 5, 7])


# Function to create date-related features
def create_date_features(date):
    return {
        'Year': date.year,
        'Month': date.month,
        'Day': date.day
    }


# Function to predict gold price for a single date
def predict_gold_price(date,model):
    features = create_date_features(date)
    input_df = pd.DataFrame([features])
    predicted_price = model.predict(input_df)
    return predicted_price[0]


# Function to predict gold prices for multiple dates
def predict_gold_prices(model, start_date, steps):
    forecast = pd.DataFrame(columns=['Date', 'Predicted_Price'])
    start_date = pd.to_datetime(start_date)
    for i in range(steps + 1):
        current_date = start_date + timedelta(days=i)
        features = create_date_features(current_date)
        input_df = pd.DataFrame([features])
        predicted_price = model.predict(input_df)
        forecast = pd.concat([forecast, pd.DataFrame({'Date': [current_date], 'Predicted_Price': predicted_price})],
                             ignore_index=True)
    return forecast


# Main panel
st.subheader('User Input Date')
st.write(f"Selected Date: {selected_date.strftime('%Y-%m-%d')}")
st.write(f"Predicting for {days_ahead} days ahead")

# Predictions
if st.button('Predict'):
    # Predict for the selected date
    prediction = predict_gold_price(selected_date, model)
    st.subheader('Prediction for Selected Date')
    st.write(f'The predicted gold price for {selected_date.strftime("%Y-%m-%d")} is: INR {prediction:.2f}')

    # Predict for the next `days_ahead` days
    forecast = predict_gold_prices(model, selected_date, days_ahead)
    st.subheader('Future Predictions')
    for index, row in forecast.iterrows():
        st.write(f'The predicted gold price for {row["Date"].strftime("%Y-%m-%d")} is: INR {row["Predicted_Price"]:.2f}')