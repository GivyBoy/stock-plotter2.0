# note that if you want to change the name of this file you should also change the name in the `Procfile`

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.write("simple stock price app")

ticker = st.text_input("Enter a stock ticker")

if ticker or (st.button("Get Stock Price") and ticker != ""):
    data = yf.download(ticker, start="2020-01-01")["Adj Close"]

    # st.line_chart(data)
    fig, ax = plt.subplots()
    plt.figure(figsize=(12, 8))
    ax.plot(data)
    st.pyplot(fig)
