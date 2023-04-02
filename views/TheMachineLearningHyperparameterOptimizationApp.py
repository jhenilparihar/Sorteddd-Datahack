# streamlit_app.py

import streamlit as st
import snowflake.connector
import pandas as pd

import pandas_datareader as web
# import pandas as pd
import datetime as dt
import yfinance as yf

from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import seaborn as sns
# import missingno as msno
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats
import pylab

# Stats model to perfrom statistical analysis
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

# To build ML models
# from fbprophet import Prophet
from matplotlib import pyplot as plt
import pandas.util.testing as tm
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error, mean_squared_error
import lightgbm as lgb
import numpy as np
# from main import df,run_query
# st.set_page_config(
#     page_title = "Multipage App"
# )

# st.title("Main Page")

# st.sidebar.success("Select a page above")
def load_view(): 
# Initialize connection.
    # Uses st.cache_resource to only run once.
    @st.cache_resource
    def init_connection():
        return snowflake.connector.connect(
            **st.secrets["snowflake"], client_session_keep_alive=True
        )

    conn = init_connection()

    # Perform query.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

# rows = run_query("SELECT Date,High,Low from ADANIENTR;")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

# st.components.v1.iframe()
# st.markdown('<iframe title="Report Section" width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiYzMwNzE2MzMtNWQ0ZS00MjMxLWIyZmEtY2Q4OTExYjMyMDA2IiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="false"></iframe>', unsafe_allow_html=True)

    df = pd.DataFrame(run_query("Select * from ADANIENTR;"))

    # df = []
    # for row in rows:
    #     df.append(row[0],row[1])
    # st.write(df)
    fig = px.line(df, x=0, y=df.columns[0:6], title='Time Series')

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

    fig1 = go.Figure([go.Scatter(x=df[0],y=df[5])])
    fig1.update_layout(
        # autosize=True,
        # template='simple_white',
        title='Adani Volume'
    )
    fig1.update_xaxes(title="Date",
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ))
    fig1.update_yaxes(title="Volume")
    col1,col2 = st.columns((5,5))

    teststart = dt.datetime(2020,1,1)
    testend = dt.datetime.now()

    test_data = yf.download('ADANIENT.NS', teststart, testend)
    actual_prices = test_data['Close'].values


    with st.container():
        with col1:
            st.write(fig)
        with col2:
            st.write(fig1)

    # st.write(forecast)
    