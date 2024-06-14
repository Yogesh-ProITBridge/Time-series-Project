# Gold Price Forecasting

This project involves collecting, analyzing, and forecasting gold prices using various predictive models. The project includes data collection through web scraping and API integration, data preparation, model building, evaluation, and deployment.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Predictive Modeling](#predictive-modeling)
- [Model Evaluation](#model-evaluation)
- [Model Deployment](#model-deployment)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [Skills and Tools](#skills-and-tools)


## Introduction

This project aims to forecast gold prices using various time series models and machine learning techniques. The goal is to provide accurate predictions that can aid in decision-making processes for stakeholders.

## Data Collection

Gold price data was collected using:
- Web Scraping: BeautifulSoup
- API Integration: Gold API

## Data Preparation

The collected data underwent several preprocessing steps including:
- Handling missing values and outliers
- Feature engineering (e.g., moving averages)

## Exploratory Data Analysis (EDA)

EDA was conducted to identify trends, seasonal patterns, and anomalies in the data using visualization libraries such as Matplotlib and Seaborn.

## Predictive Modeling

The following predictive models were used to forecast gold prices:
- Linear Regression
- XGBoost Regressor
- FB Prophet
- ARIMA

## Model Evaluation

Models were evaluated using cross-validation and performance metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). Hyperparameter tuning was conducted to optimize model performance.

## Model Deployment

The final model was dockerized and deployed on AWS EC2 instances to ensure scalability and efficient access. Deployment involved:
- Dockerization of the model
- Deployment on EC2 instances

## Conclusion and Recommendations

Conclusions and suggestions derived from model evaluation were presented to stakeholders, ensuring practical applicability for decision-making processes.

## Skills and Tools

- **Data Collection**: BeautifulSoup,  GoldAPI
- **Data Preparation**: Pandas, NumPy
- **EDA**: Matplotlib, Seaborn
- **Predictive Modeling**: Scikit-learn, Statsmodels, XGBoost, FB Prophet
- **Deployment**: Docker, AWS EC2, streamlit
- **Programming Languages**: Python




![Screenshot 2024-06-12 225641](https://github.com/Yogesh-ProITBridge/Time-series-Project/assets/151123394/b0c408a9-c4fa-4c10-a80a-aa77c2450ca3)

![Screenshot 2024-06-14 001559](https://github.com/Yogesh-ProITBridge/Time-series-Project/assets/151123394/85dc21e0-b17d-4231-b1eb-f2226760960f)
