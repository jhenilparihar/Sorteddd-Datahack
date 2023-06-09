import streamlit as st
import datetime as dt
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
# import yfinance as yf
import tensorflow as tf

import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, LSTM, Dense


def load_view():
    col1,col2,col3 = st.columns((1,5,1))
    with st.container():
        with col2:
            st.header("ADANI")
            teststart = dt.datetime(2020,1,1)
            testend = dt.datetime.now()
            model = keras.models.load_model('./model_adanient_pred.h5')
            company = 'ADANIENT.NS'

            startdate = dt.datetime(2010,1,1)
            enddate = dt.datetime(2020,1,1)

            data = yf.download(company, startdate, enddate)
            test_data = yf.download(company, teststart, testend)
            actual_prices = test_data['Close'].values
            scaler = MinMaxScaler(feature_range= (0,1))
            scaled_data = scaler.fit_transform(test_data['Close'].values.reshape(-1,1))

            total_dataset = pd.concat([data['Close'], test_data['Close']])
            prediction_days = 120
            model_inputs = total_dataset[len(total_dataset)- len(test_data) - prediction_days:].values
            model_inputs = model_inputs.reshape(-1, 1)
            model_inputs = scaler.transform(model_inputs)

            x_test = []

            for x in range(prediction_days, len(model_inputs)):
                x_test.append(model_inputs[x - prediction_days:x, 0])

            x_test = np.array(x_test)
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

            predicted_prices = model.predict(x_test)
            predicted_prices = scaler.inverse_transform(predicted_prices)

            fig = px.line(test_data.index, y=actual_prices, title='Time Series')
            fig.add_scatter(x=test_data.index, y=predicted_prices)
            fig.update_xaxes(
                title="Date",
                rangeslider_visible=False,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )
            fig.update_yaxes(title="Price")
            st.write(fig)

        with col2:
            st.header("TCS")
            teststart = dt.datetime(2020,1,1)
            testend = dt.datetime.now()
            model = keras.models.load_model('./model_tcs.h5')
            company = 'TCS.NS'

            startdate = dt.datetime(2010,1,1)
            enddate = dt.datetime(2020,1,1)

            data = yf.download(company, startdate, enddate)
            test_data = yf.download(company, teststart, testend)
            actual_prices = test_data['Close'].values
            scaler = MinMaxScaler(feature_range= (0,1))
            scaled_data = scaler.fit_transform(test_data['Close'].values.reshape(-1,1))

            total_dataset = pd.concat([data['Close'], test_data['Close']])
            prediction_days = 120
            model_inputs = total_dataset[len(total_dataset)- len(test_data) - prediction_days:].values
            model_inputs = model_inputs.reshape(-1, 1)
            model_inputs = scaler.transform(model_inputs)

            x_test = []

            for x in range(prediction_days, len(model_inputs)):
                x_test.append(model_inputs[x - prediction_days:x, 0])

            x_test = np.array(x_test)
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

            predicted_prices = model.predict(x_test)
            predicted_prices = scaler.inverse_transform(predicted_prices)

            fig1 = px.line(test_data.index, y=actual_prices, title='Time Series')
            fig1.add_scatter(x=test_data.index, y=predicted_prices)
            fig1.update_xaxes(
                title="Date",
                rangeslider_visible=False,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )
            fig.update_yaxes(title="Price")
            st.write(fig1)
        
        with col2:
            st.header("RELIANCE")
            teststart = dt.datetime(2020,1,1)
            testend = dt.datetime.now()
            model = keras.models.load_model('./model_reliance.h5')
            company = 'RELIANCE.NS'

            startdate = dt.datetime(2010,1,1)
            enddate = dt.datetime(2020,1,1)

            data = yf.download(company, startdate, enddate)
            test_data = yf.download(company, teststart, testend)
            actual_prices = test_data['Close'].values
            scaler = MinMaxScaler(feature_range= (0,1))
            scaled_data = scaler.fit_transform(test_data['Close'].values.reshape(-1,1))

            total_dataset = pd.concat([data['Close'], test_data['Close']])
            prediction_days = 120
            model_inputs = total_dataset[len(total_dataset)- len(test_data) - prediction_days:].values
            model_inputs = model_inputs.reshape(-1, 1)
            model_inputs = scaler.transform(model_inputs)

            x_test = []

            for x in range(prediction_days, len(model_inputs)):
                x_test.append(model_inputs[x - prediction_days:x, 0])

            x_test = np.array(x_test)
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

            predicted_prices = model.predict(x_test)
            predicted_prices = scaler.inverse_transform(predicted_prices)

            fig2 = px.line(test_data.index, y=actual_prices, title='Time Series')
            fig2.add_scatter(x=test_data.index, y=predicted_prices)
            fig2.update_xaxes(
                title="Date",
                rangeslider_visible=False,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )
            fig.update_yaxes(title="Price")
            st.write(fig2)

        
    col1, col2, _ = st.columns((3, 10, 3))
    with col2:
        st.title("Adani Vs Other Similar Companies")
        st.markdown('<br>', unsafe_allow_html=True)

    _, col1, col2, __ = st.columns((1, 2, 10, 1))
    with col1:

        st.metric("Adani", "42%", "-8%")
        st.metric("Reliance", "74%", "6%")
        st.metric("Tata", "86%", "4%")

    with col2:
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Adani', 'Tata', 'Reliance'])

        st.markdown('<br>', unsafe_allow_html=True)
        st.line_chart(chart_data)

        
        