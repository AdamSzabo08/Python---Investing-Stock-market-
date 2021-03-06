import streamlit as st
import numpy as np
import yfinance as yf

st.write("""
# Hello this is my first stock monitoring website with Python (yfinance, streamlit, numpy) 
#### By Adam Szabo
####
""")
''
ticker = ['AAPL','MSFT','NKE','NOW','GOOGL','AMZN','FB','PYPL','TSLA']

option = st.selectbox(
    'Which stock do you want to analyze?',
     ticker)
'You selected: ', option

select = yf.Ticker(option)

''

'Price:'
select.info["bid"]


'Forward P/E'
select.info['forwardPE']

'Dividend rate:'
select.info['dividendRate']

'Fiftytwo week high:'
select.info["fiftyTwoWeekHigh"]

'Fiftytwo week low:'
select.info["fiftyTwoWeekLow"]

''
''

period = ['1y','6mo','1mo','1d']

option2 = st.selectbox(
    'Which period do you want to see?',
     period)
'You selected: ', option
'You selected: ', option2

select2 = select.history(period=option2)
st.line_chart(select2.Close)
st.line_chart(select2.Volume)