import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st
import plotly.express as px
import requests

# Set the title for the dashboard
st.title('Stock Trading Data Dashboard')

# Get user input for ticker and date range
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

# Define a list of tickers to retrieve data for
tickers = ['TSLA']  # Add more tickers as needed
# Set the start and end dates if not provided by the user
start_date = '2022-01-01'
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')

# Create an empty dataframe to store the data
data = pd.DataFrame() 

# Retrieve data for each ticker and add it to the dataframe
for ticker in tickers:
    ticker_data = yf.download(tickers=ticker, start=start_date, end=end_date)
    # Add a column to identify the ticker
    ticker_data['Ticker'] = ticker  
    data = pd.concat([data, ticker_data])

# Create a line plot using the adjusted close prices
fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)

# Create tabs for pricing data, fundamental data, and news
pricing_data, fundamental_data, news = st.tabs(['Pricing Data', 'Fundamental Data', 'Top 10 News'])

# Pricing Data tab
with pricing_data:
    st.header('Price Activity')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = data2['% Change'].mean()*252*100
    st.write('Annual Return is', annual_return, '%')
    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is', stdev*100, '%')
    st.write('Risk Adj. Return is', annual_return/(stdev*100))

# Fundamental Data tab
from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    key = 'JN50EMSVSK3QFY5K'
    url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=TSLA&apikey=JN50EMSVSK3QFY5K'
    url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=TSLA&apikey=JN50EMSVSK3QFY5K'
    url = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=TSLA&apikey=JN50EMSVSK3QFY5K'
    r = requests.get(url)
    fd = FundamentalData(key, output_format = 'pandas')
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual('TSLA')[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual('TSLA')[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)

from stocknews import StockNews

# News tab
with news:
    # Display the header for the news section with the selected ticker
    st.header(f'News of {ticker}')
    # Create a StockNews object to retrieve news for the selected ticker
    sn = StockNews(ticker, save_news=False)
    # Read the RSS feed for news articles
    df_news = sn.read_rss()

    # Display the top 10 news articles
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')