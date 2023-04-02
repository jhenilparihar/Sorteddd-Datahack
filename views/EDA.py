# Import streamlit and other libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

def load_view():
    # st.set_page_config(layout="wide")

    # Set the title of the app
    st.title("OpenAI Graphs")


    # Create a sidebar for selecting the graph type
    graph_type = st.sidebar.selectbox("Select a graph type", ["Bar chart", "Line chart", "Scatter plot", "Radar chart"])

    # Create some dummy data for the graphs
    gpt_data = pd.DataFrame({
        "model": ["GPT-1", "GPT-2", "GPT-3", "GPT-3.5", "GPT-4"],
        "parameters": [117, 1542, 175, 350, 700]
    })

    customer_data = pd.DataFrame({
        "industry": ["Education", "Health care", "Finance", "Entertainment", "Gaming", "E-commerce", "Social media", "Other"],
        "customers": [15, 12, 10, 8, 7, 6, 5, 4]
    })

    revenue_data = pd.DataFrame({
        "year": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        "revenue": [0.5, 1.2, 2.5, 4.0, 6.5, 8.0, 10.0],
        "donations": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    })

    quality_data = pd.DataFrame({
        "model": ["GPT-1", "GPT-2", "GPT-3", "GPT-3.5", "GPT-4"],
        "quality": [0.6, 0.7, 0.8, 0.85, 0.9],
        "diversity": [0.4, 0.5, 0.6, 0.65, 0.7]
    })

    rating_data = pd.DataFrame({
        "stakeholder": ["Researchers", "Developers", "Customers", "Media", "Policymakers", "Public"],
        "rating": [4.5, 4.2, 4.0, 3.8, 3.5, 3.2]
    })

    # Define a function to create a radar chart
    def radar_chart(data):
        # Calculate the angle for each variable
        angle = np.linspace(0 ,2 * np.pi , len(data), endpoint=False)
        
        # Repeat the first value to close the circle
        values = data["rating"]

        # Initialize a plot
        fig = plt.figure(figsize=(4 ,4)) # Change the figsize here

        # Add axes
        ax = fig.add_subplot(111 , polar=True)

        # Plot the values
        ax.plot(angle , values , color="blue" , linewidth=2)

        # Fill the area
        ax.fill(angle , values , color="blue" , alpha=0.25)

        # Set the labels
        ax.set_xticks(angle)
        ax.set_xticklabels(data["stakeholder"])

        # Set the title and show the plot
        plt.title("Stakeholder Ratings")

        return fig

    # Display the graph based on the selected type
    if graph_type == "Bar chart":
        st.write("A bar chart that shows the number of parameters of different versions of GPT models")
        st.altair_chart(alt.Chart(gpt_data).mark_bar().encode(
            x="model",
            y="parameters"
        ).properties(
            width=600 # adjust this value as needed
        ))
    elif graph_type == "Line chart":
        st.write("A line chart that shows the trend of OpenAI's revenue and donations over time")
        st.altair_chart(alt.Chart(revenue_data).mark_line().encode(
            x="year",
            y=alt.Y("revenue", axis=alt.Axis(title="Revenue (in millions)")),
            color=alt.value("green")
        ) + alt.Chart(revenue_data).mark_line().encode(
            x="year",
            y=alt.Y("donations", axis=alt.Axis(title="Donations (in millions)")),
            color=alt.value("blue")
        ))
    elif graph_type == "Scatter plot":
        st.write("A scatter plot that shows the relationship between the text generation quality and diversity of different versions of GPT models")
        st.altair_chart(alt.Chart(quality_data).mark_circle(size=60).encode(
            x="quality",
            y="diversity",
            color="model",
            tooltip=["model", "quality", "diversity"]
        ).interactive())
    elif graph_type == "Radar chart":
        st.write("A radar chart that shows the ratings of OpenAI's reputation by different stakeholders")
        st.pyplot(radar_chart(rating_data))