import streamlit as st
import pandas as pd
import numpy as np


def load_data():
    return pd.DataFrame(
        {
            "Price/Earning": ['815x', '29x', '831x', '312x', '508x', '90x', '35x'],
            "Industry Avg.": ['24x', '24x', '20x', '24x', '12x', '30x', '2x'],
            "Implied Downside": ['-97.10%', '-18.17%', '-97.64%', '-92.43%', '-97.68%', '-67.12%', '-93.26%'],
            "Price/Sale": ['60.6x', '3.9x', '139.3x', '27.3x', '5.7x', '1.3x', '10.5x'],
            "Industry Avg.": ['1.1x', '1.1x', '1.0x', '1.1x', '0.5x', '1.1x', '0.9x'],
            "Implied Downside": ['-98.13%', '-70.68%', '-99.31%', '-95.84%', '-91.33%', '-20.90%', '-91.65%'],
            "EV/EBITDA": ['101x', '13x', '303x', '69x', '66x', '37x', '20x'],
            "Industry Avg.": ['12x', '12x', '9x', '12x', '8x', '15x', '2x'],
            "Implied Downside": ['-88.33%', '-10.42%', '-97.16%', '-83.01%', '-88.16%', '-58.26%', '-88.07%'],

        },
        index=['ADANIGREEN', 'ADANIPOWER', 'ATGL',
               'ADANITRANS', 'ADANIENT', 'AWL', 'ADANIPORTS']
    )


def load_promoter_data():
    return pd.DataFrame(
        {
            "% Shares Publicly held by Promoter Group": ['60.75%', '74.97%', '74.80%', '74.19%', '72.63%', '65.13%', '63.22%', '56.69%', '87.94%'],
            "% Promoter Shares Pledged": ['4.36%', '25.01%', '0%', '6.62%', '2.66%', '17.31%', '0%*', '0%*', '0%'],
        },
        index=['ADANIGREEN', 'ADANIPOWER', 'ATGL',
               'ADANITRANS', 'ADANIENT', 'ADANIPORTS', 'Amnuja Cement', 'ACC', 'AWL']
    )


def load_view():
    _, col, __ = st.columns((1, 8, 1))
    with col:
        with st.container():
            st.header("Hindinburg Report on Adani")
            st.subheader(
                "Adani Group: How The World’s 3rd Richest Man Is Pulling The Largest Con In Corporate History")

        st.markdown("<br><br/><h5>The 7 Listed Companies Of Adani Group Are 85%+ Overvalued.</h5><br>",
                    unsafe_allow_html=True)

        st.checkbox("Use container width", value=False,
                    key="use_container_width")

        df = load_data()

        st.experimental_data_editor(
            df, use_container_width=st.session_state.use_container_width)

        st.markdown("<br><h5>A Portion Of Promoter Equity In Adani Group Listed Entities Is Pledged For Loans, Effectively Leveraging The Group To The Hilt</h5>", unsafe_allow_html=True)

        st.markdown("<p>Equity share pledges are an inherently unstable source of lending collateral because if share prices drop, the lender can make a collateral call. If no additional collateral is available, the lender could require a forced liquidation of shares (often perpetuating a self-fulfilling cycle as stock prices move lower and selling continues).<br><br>Below is a breakdown of the publicly disclosed equity share pledges by promoter group entities for each of its listed companies:</p>", unsafe_allow_html=True)

        df = load_promoter_data()

        st.experimental_data_editor(df)
