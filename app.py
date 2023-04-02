from streamlit_echarts import st_echarts
import streamlit as st
import pandas as pd
import numpy as np

col1, col2 = st.columns((3, 2))
with col1:

    chart_data = pd.DataFrame(
        np.random.randn(20, 1),
        columns=['Adani Enterprise'])

    st.line_chart(chart_data)

with col2:
    option = {
        "tooltip": {
            "trigger": 'item'
        },
        "legend": {
            "top": '0%',
            "margin-bottom": 10,
            "left": 'center'
        },
        "series": [
            {
                "name": 'Access From',
                "type": 'pie',
                "radius": ['40%', '70%'],
                "avoidLabelOverlap": True,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": '#fff',
                    "borderWidth": 2
                },
                "label": {
                    "show": False,
                    "position": 'center'
                },
                "emphasis": {
                    "label": {
                        "show": True,
                        "fontSize": 40,
                        "fontWeight": 'bold'
                    }
                },
                "labelLine": {
                    "show": False
                },
                "data": [
                    {"value": 1048, "name": 'Adani Enterprise'},
                    {"value": 735, "name": 'Adani Ports'},
                    {"value": 580, "name": 'Adani Power'},
                    {"value": 484, "name": 'Adani Willmare'},
                    {"value": 300, "name": 'Adani Green'}
                ]
            }
        ]
    }
    st_echarts(options=option)

_, col1, __ = st.columns((1, 15, 1))

with col1:

    option = {
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
            }
        },
        "legend": {},
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "xAxis": [
            {
                "type": 'category',
                "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            }
        ],
        "yAxis": [
            {
                "type": 'value'
            }
        ],
        "series": [
            {
                "name": 'Direct',
                "type": 'bar',
                "emphasis": {
                    "focus": 'series'
                },
                "data": [320, 332, 301, 334, 390, 330, 320]
            },
            {
                "name": 'Email',
                "type": 'bar',
                "stack": 'Ad',
                "emphasis": {
                    "focus": 'series'
                },
                "data": [120, 132, 101, 134, 90, 230, 210]
            },
            {
                "name": 'Union Ads',
                "type": 'bar',
                "stack": 'Ad',
                "emphasis": {
                    "focus": 'series'
                },
                "data": [220, 182, 191, 234, 290, 330, 310]
            },
            {
                "name": 'Google',
                "type": 'bar',
                "stack": 'Search Engine',
                "emphasis": {
                    "focus": 'series'
                },
                "data": [120, 132, 101, 134, 290, 230, 220]
            },
        ]
    }
    st_echarts(options=option)
