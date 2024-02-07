import streamlit as st
import yfinance as yf

# Title and introduction
st.write("""
# Welcome to Stock Analyzer
#### Your tool for stock monitoring and analysis
""")

# Function to fetch stock information for a given symbol or company name


def fetch_stock_info(symbol_or_name):
    try:
        # Try to fetch stock information based on symbol
        return yf.Ticker(symbol_or_name)
    except:
        try:
            # Try to fetch stock information based on company name
            symbol = yf.Tickers(symbol_or_name).tickers[0].info.get('symbol')
            if symbol:
                return yf.Ticker(symbol)
            else:
                return None
        except:
            return None

# Function to display stock information with error handling


def display_info(info_name, info_value):
    if info_value is not None:
        st.write(f'**{info_name}:** {info_value}')
    else:
        st.write(f'**{info_name}:** Information not available')


# Default value for the company symbol
default_symbol = "AAPL"

# Search bar for company symbols or names
search_query = st.text_input(
    'Enter the company symbol or name (e.g., AAPL or Apple Inc.):', default_symbol, key='search_query', autocomplete='on')

# Fetch stock information based on search query
if search_query:
    # Fetch stock information for the given symbol or name
    selected_stock = fetch_stock_info(search_query)

    if selected_stock:
        # Display company symbol
        company_symbol = selected_stock.info.get('symbol', 'N/A')
        st.write(f'**Company Symbol:** {company_symbol}')

        # Display various information about the stock
        st.write('## Stock Information')

        # Display Price
        display_info('Bid', selected_stock.info.get('bid'))
        display_info('Ask', selected_stock.info.get('ask'))

        # Display Forward P/E
        display_info('Forward P/E', selected_stock.info.get('forwardPE'))

        # Display Dividend rate
        display_info('Dividend Rate', selected_stock.info.get('dividendRate'))

        # Display Fiftytwo week high
        display_info('52-Week High',
                     selected_stock.info.get('fiftyTwoWeekHigh'))

        # Display Fiftytwo week low
        display_info('52-Week Low', selected_stock.info.get('fiftyTwoWeekLow'))

        # Selectbox for choosing the period
        selected_period = st.selectbox('Select the period to analyze:', [
                                       '5y', '1y', '6mo', '1mo', '1d'])

        # Display the selected period
        st.write('You selected:', selected_period)

        # Fetch historical data for the selected period
        try:
            historical_data = selected_stock.history(period=selected_period)
            # Display line chart for closing prices
            st.write(f'## Closing Prices Over Time: {
                     selected_stock.info.get("longName", "N/A")} ({company_symbol})')
            st.line_chart(historical_data['Close'])

            # Display line chart for volume
            st.write(f'## Volume Over Time: {selected_stock.info.get(
                "longName", "N/A")} ({company_symbol})')
            st.line_chart(historical_data['Volume'])
        except:
            st.error("Error fetching historical data. Please try again later.")
    else:
        st.error(
            "Invalid company symbol or name. Please enter a valid symbol or name.")
else:
    st.write("Enter a company symbol or name to search for stock information.")

# Footer
st.write("""
---
Developed by Adam Szabo.
""")
