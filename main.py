import yfinance as yf
import streamlit as st

st.markdown("<h1><ins>Streamlit Tutorial #1</ins></h1>", unsafe_allow_html=True)
st.header("Simple Stock Price App")
st.write("Shown are the stock closing price and volume of Google!")

ticker_data = yf.Ticker('GOOGL')

ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

st.header("Closing Price")
st.line_chart(ticker_df.Close)
st.header("Volume Price")
st.line_chart(ticker_df.Volume)