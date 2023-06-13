### Cryptocurrency Historical & Daily Prices Dashboard

This Python code creates a dashboard to display historical and daily prices of cryptocurrencies. It uses the `yfinance` and `streamlit` libraries for data retrieval and visualization.

#### Usage

1. Install the required libraries: `yfinance`, `streamlit`, `PIL`.
2. Run the code using a Python interpreter.
3. The cryptocurrency historical & daily prices dashboard will be displayed, showing the prices for various cryptocurrencies.

#### Functions

- **Sidebar**: The code adds a sidebar tab for "Top News" using the `streamlit` library. It allows users to enter a ticker symbol and select a date range.
- **Data Retrieval**: The code retrieves historical data for various cryptocurrencies using the `yfinance` library. It fetches data for cryptocurrencies like Bitcoin, Ethereum, Polygon, Ripple, Binance, Solana, and Avalanche.
- **Data Visualization**: The code uses the `streamlit` library to display the data in tables and charts.
  - For each cryptocurrency, it displays the image of the cryptocurrency, the current data frame, and a chart of the closing prices over time.

### Stock Trading Data Dashboard

This is a Python code for creating a stock trading data dashboard. The code fetches stock data, displays price activity, fundamental data, and top news articles for a given ticker symbol.

#### Usage

1. Install the required libraries: `pandas`, `numpy`, `yfinance`, `streamlit`, `plotly.express`, `requests`, `alpha_vantage`, and `stocknews`.
2. Run the code using a Python interpreter.
3. Enter the ticker symbol and select the desired date range using the sidebar inputs.
4. The stock trading data dashboard will be displayed, providing the following information:

- **Stock Data Fetching**: The code imports the necessary libraries (`pandas`, `numpy`, `yfinance`, `streamlit`, `plotly.express`, `requests`) to fetch stock data and visualize it.
- **User Input**: The code prompts the user to enter a ticker symbol and select a start and end date using the `streamlit` library.
- **Data Retrieval**: The code retrieves stock data using the `yfinance` library for the specified ticker symbol and date range. It stores the data in a `pandas` DataFrame.
- **Price Activity Visualization**: The code uses `plotly.express` to create a line plot of the adjusted close prices for the selected ticker symbol.
- **Tabs for Data Categories**: The code utilizes the `streamlit` library to create tabs for pricing data, fundamental data, and news.
- **Pricing Data**: The code calculates and displays the percent change, annual return, standard deviation, and risk-adjusted return based on the stock's price activity using the `pandas` and `numpy` libraries.
- **Fundamental Data**: The code retrieves fundamental data (balance sheet, income statement, cash flow statement) using the Alpha Vantage API. It utilizes the `requests` library to make HTTP requests and the `alpha_vantage.fundamentaldata` module to extract the data. The data is displayed using `pandas` DataFrame.
- **News Articles**: The code imports the `stocknews` library to fetch and display top news articles related to the selected ticker symbol. It extracts the publication date, title, summary, title sentiment, and news sentiment from the news articles using the `stocknews` library and displays them using `streamlit`.
