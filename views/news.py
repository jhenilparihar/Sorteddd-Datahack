import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px


def load_view():
    col, __ = st.columns((10, 1))

    with col:
        st.subheader("How did news affect Adani's stock price")
        st.markdown("#")

    col, _ = st.columns((10, 1))

    with col:
        st.header("Adani Repays $500 Million Bridge Loan to Regain Investor Faith")
        st.markdown(
            "[Check full story](https://www.bloomberg.com/news/articles/2023-03-08/adani-repays-500-million-bridge-loan-to-regain-investor-faith)")
        st.markdown("<h5>Date: March 8, 2023</h5>", unsafe_allow_html=True)
        df = px.data.gapminder()

        fig = px.scatter(
            df.query("year==2007"),
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
        )
        df2 = px.data.iris()
        fig2 = px.scatter(
            df2,
            x="sepal_width",
            y="sepal_length",
            color="sepal_length",
            color_continuous_scale="reds",
        )

        tab1, tab2, tab3 = st.tabs(
            ["Adani Enterprise", "Adani Power", "Adani Ports"])
        with tab1:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Enterprise'])
            st.line_chart(chart_data)
        with tab2:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Power'])

            st.line_chart(chart_data)
        with tab3:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Ports'])

            st.line_chart(chart_data)

    with col:
        st.header(
            "Adani Enterprises stock exits NSE’s additional security framework after a month")
        st.markdown("[Check full Story](https://www.financialexpress.com/market/adani-enterprises-exits-nses-additional-security-framework-after-a-month/3001534/)")
        st.markdown("<h5>Date: March 7, 2023</h5>", unsafe_allow_html=True)

        df = px.data.gapminder()

        fig = px.scatter(
            df.query("year==2007"),
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
        )
        df2 = px.data.iris()
        fig2 = px.scatter(
            df2,
            x="sepal_width",
            y="sepal_length",
            color="sepal_length",
            color_continuous_scale="reds",
        )

        tab1, tab2, tab3 = st.tabs(
            ["Adani Enterprise", "Adani Power", "Adani Ports"])
        with tab1:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Ente    rprise'])
            st.line_chart(chart_data)
        with tab2:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Power'])

            st.line_chart(chart_data)
        with tab3:
            chart_data = pd.DataFrame(
                np.random.randn(20, 1),
                columns=['Adani Ports'])

            st.line_chart(chart_data)
