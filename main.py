from openai import OpenAI
import streamlit as st
import yfinance as yf
import pandas as pd

# Function to fetch stock data
def get_stock_data(ticker, start_date='2024-01-01', end_date='2024-02-01'):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Streamlit app layout
st.title('Interactive Financial Market Analysis')

# Sidebar for user inputs
st.sidebar.header('User Input Options')
selected_stock = st.sidebar.text_input('Enter Stock Ticker', 'AAPL').upper()  # Default to Apple Inc.

# Fetch and display the stock data
stock_data = get_stock_data(selected_stock)
st.write(f"Displaying data for: {selected_stock}")
st.write(stock_data)