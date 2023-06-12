import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles and subtitles
st.title("Cryptocurrency Historical & Daily Prices")
st.header ("Main Dashboard")

# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Polygon = 'MATIC-USD'
Ripple = 'XRP-USD'
Binance = 'BNB-USD'
Solana = 'SOL-USD'
Avalanche = 'AVAX-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
MATIC_Data = yf.Ticker(Polygon)
XRP_Data = yf.Ticker(Ripple)
BNB_Data = yf.Ticker(Binance)
SOL_Data = yf.Ticker(Solana)
AVAX_Data = yf.Ticker(Avalanche)

# Fetch history data from Yahoo Finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
MATICHis = MATIC_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BNBHis = BNB_Data.history(period="max")
SOLHis = SOL_Data.history(period="max")
AVAXHis = AVAX_Data.history(period="max")

# Fetching crypto data frame
BTC = yf.download(Bitcoin, start="2023-06-09")
ETH = yf.download(Ethereum, start="2023-06-09")
MATIC = yf.download(Polygon, start="2023-06-09")
XRP = yf.download(Ripple, start="2023-06-09")
BNB = yf.download(Binance, start="2023-06-09")
SOL = yf.download(Solana, start="2023-06-09")
AVAX = yf.download(Avalanche, start="2023-06-09")

# Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
# Display image
st.image(imageBTC)
# Display dataframe
st.table(BTC)
# Display a chart
st.bar_chart(BTCHis.Close)

# Ethereum
st.write("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
# Display image
st.image(imageETH)
# Display dataframe
st.table(ETH)
# Display a chart
st.bar_chart(ETHHis.Close)

# Polygon
st.write("Polygon ($)")
imageMATIC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png'))
# Display image
st.image(imageMATIC)
# Display dataframe
st.table(MATIC)
# Display a chart
st.bar_chart(MATICHis.Close)

# Ripple
st.write("Ripple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
# Display image
st.image(imageXRP)
# Display dataframe
st.table(XRP)
# Display a chart
st.bar_chart(XRPHis.Close)

# Binance
st.write("Binance ($)")
imageBNB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'))
# Display image
st.image(imageBNB)
# Display dataframe
st.table(BNB)
# Display a chart
st.bar_chart(BNBHis.Close)

# Solana
st.write("Solana ($)")
imageSOL = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png'))
# Display image
st.image(imageSOL)
# Display dataframe
st.table(SOL)
# Display a chart
st.bar_chart(SOLHis.Close)

# Avalanche
st.write("Avalanche ($)")
imageAVAX = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png'))
# Display image
st.image(imageAVAX)
# Display dataframe
st.table(AVAX)
# Display a chart
st.bar_chart(AVAXHis.Close)
