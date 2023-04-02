from PIL import Image
import base64
import seaborn as sns
import os
# The OS module in Python provides functions for interacting with the operating system.
import streamlit as st
# EDA packages : Exploitary data analysis
import pandas as pd
import numpy as np
# Viz packages : Visualization packages
import matplotlib.pyplot as plt
import matplotlib
from streamlit_echarts import st_echarts

matplotlib.use('Agg')  # To help us to prevent erros while trying to plot
# The canonical renderer for user interfaces is Agg which uses the Anti-Grain Geometry C++ library to make a raster (pixel) image of the figure.
# Like in tiknter it is matplotlib.use('TkAgg')


def load_view():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    col1, col2, col3 = st.columns((1, 9, 1))
    with col2:
        st.title("Streamlining financial analysis with data-driven analysis")
        # st.subheader("Problem definition:" )

    st.markdown("#")
    st.markdown("""
      <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
          padding-top: 50px !important;
        }
        section[data-testid="stSidebar"][aria-expanded="false"]{
          padding-top: 50px !important;
        }
      </style>""", unsafe_allow_html=True)

    col1, col2 = st.columns((2, 3))
    with col1:
        st.image("https://cdn.dribbble.com/users/1523313/screenshots/13671653/media/7c52f9d4b1117aa12f3bf9f9c3b9e1aa.gif")
                #  caption="Representation of Financial ")
    with col2:
        original_title = '''<div style="background-color: #CAF0F8; padding: 20px;padding-bottom: 40px; border-radius: 30px">
                            <h3>Abstract</h3>
                            <p> Financials refer to an organization’s various financial aspects, including accounting, investing, budgeting, and financial reporting. These crucial elements disclose a company’s monetary health and position. <br><br>Key components such as balance sheets, income statements, and cash flow statements serve as primary indicators of financial performance, assisting stakeholders in understanding a company’s profitability, liquidity, and efficiency. <br><br>Proper financial management enables organizations to make informed decisions, allocate resources effectively, and ensure sustainable growth and long-term stability.</p>
                            </div>
                            '''
        st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("#")
    col4, col5, col6 = st.columns((1,5,1))
    with col5:
        st.subheader("Scan To View External Dashboard")
    # with col6:    
        st.image("./qr.png")


    # col1, col2, _ = st.columns((3, 10, 3))
    # with col2:
    #     st.title("Adani Vs Other Similar Companies")
    #     st.markdown('<br>', unsafe_allow_html=True)

    # _, col1, col2, __ = st.columns((1, 2, 10, 1))
    # with col1:

    #     st.metric("Adani", "42%", "-8%")
    #     st.metric("Reliance", "74%", "6%")
    #     st.metric("Tata", "86%", "4%")

    # with col2:
    #     chart_data = pd.DataFrame(
    #         np.random.randn(20, 3),
    #         columns=['Adani', 'Tata', 'Reliance'])

    #     st.markdown('<br>', unsafe_allow_html=True)
    #     st.line_chart(chart_data)

    # col1, col2 = st.columns((2, 3))
    # with col1:
        
    #     st.subheader("Adani Enterprise")
    #     st.markdown('#')

    #     chart_data = pd.DataFrame(
    #         np.random.randn(20, 1),
    #         columns=['Adani Enterprise'])

    #     st.line_chart(chart_data)
    # with col2:
    #     from plotly.subplots import make_subplots
    #     import plotly.graph_objects as go

    #     fig = make_subplots(rows=1, cols=2, specs=[
    #                         [{'type': 'domain'}, {'type': 'domain'}]])

    #     labels = ['ADANIENT', 'ADANIPOWER', 'ADANIGREEN', 'ADANITRANS']
    #     values = [4500, 2500, 1053, 500]

    #     fig.add_trace(go.Pie(labels=labels, values=values, name="Pie Chart Adani"),
    #                   1, 2)
    #     # make donut chart
    #     fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    #     st.plotly_chart(fig, use_container_width=True)

