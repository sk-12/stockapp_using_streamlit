

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
st.write("""
*STOCK MARKET APP*






Here are the closing price,opening price and volume of Catterpillar,Google,Microsoft
"""

)
st.title('my_first_app')

st.write('#Microsoft')

ticker_symbol1='MSFT'
ticker_data1=yf.Ticker(ticker_symbol1)
ticker_df1=ticker_data1.history(period='1d',start='2020-01-01',end='2021-01-01')
st.line_chart(ticker_df1.Close)
st.line_chart(ticker_df1.Volume)
st.line_chart(ticker_df1.Open)
ticker_data1.recommendations

st.write('#Google')

ticker_symbol2='GOOGL'
ticker_data2=yf.Ticker(ticker_symbol2)
ticker_df2=ticker_data2.history(period='1d',start='2020-01-01',end='2021-01-01')
st.line_chart(ticker_df2.Close)
st.line_chart(ticker_df2.Volume)
st.line_chart(ticker_df2.Open)
ticker_data2.recommendations

st.write('#Catterpillar')

ticker_symbol3='CAT'
ticker_data3=yf.Ticker(ticker_symbol3)
ticker_df3=ticker_data3.history(period='1d',start='2020-01-01',end='2021-01-01')
st.line_chart(ticker_df3.Close)
st.line_chart(ticker_df3.Volume)
st.line_chart(ticker_df3.Open)
ticker_data3.recommendations

