import streamlit as st
import utils as utl
from views import EDA, home, AutoMlRegressionApp, AutoMlClassificationApp, TheMachineLearningHyperparameterOptimizationApp, report, strappopenai, news
import snowflake.connector
import pandas as pd

# Initialize connection.
# Uses st.cache_resource to only run once.


st.set_page_config(layout="wide", page_title='SnowLit.AI')
# st.set_option('deprecation.showPyplotGlobalUse', False)
import json
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time


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


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_success = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_91rvnawv.json")
col1, col2, col3 = st.columns((2, 9, 2))
with col2:
    with st_lottie_spinner(lottie_success, loop=False, key="progress"):
        time.sleep(3)

utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "EDA":
        EDA.load_view()
    elif route == "AutoMlRegressionApp":
        AutoMlRegressionApp.load_view()
    elif route == "AutoMlClassificationApp":
        AutoMlClassificationApp.load_view()
    elif route == "report":
        report.load_view()
    elif route == "news":
        news.load_view()
    elif route == "TheMachineLearningHyperparameterOptimizationApp":
        TheMachineLearningHyperparameterOptimizationApp.load_view()
    elif route == None:
        home.load_view()


navigation()
