import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="NVDA Stock Analysis", page_icon="📊", layout="wide")
nvda_path = './data/NVDA.csv'

df = pd.read_csv(nvda_path)

df['Date'] = pd.to_datetime(df['Date'])

st.title("NVIDIA :green[[NVDA]] Stock Analysis")

# Create a two-column layout: one for the text and graph, and one for the data and metrics
col1, col2 = st.columns([2, 1])

# The left side
with col1:
    # st.subheader("Stock Data Overview", divider="green")

    # st.write("""
    # NVIDIA Corporation (NVDA) is a leading tech company based in Santa Clara, California. 
    # It designs GPUs for gaming and professional markets, and SoCs for mobile and automotive markets. 
    # NVIDIA is also a major player in AI hardware and software.

    # Key Numbers:
    # - Stock Ticker: NVDA
    # - Market Cap: $3.23T
    # - 52 Week High: $315.76
    # - 52 Week Low: $124.46
    # - Volume: 1.2M
    # """)
    st.subheader("Key Financial Ratios", divider="green")

    st.write("""
    - P/E Ratio: 92.3
    - EPS: 3.12
    - Dividend Yield: 0.12%
    - ROE: 45.6%
    - Debt to Equity: 0.41
    """)
    st.subheader("Closing Price Over Time", divider="green")

    line_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Close:Q', title='Close Price'),
        tooltip=['Date:T', 'Close:Q']
    ).properties(
        width=800,
        height=400,
        title="NVIDIA (NVDA) Closing Price Over Time"
    ).interactive()

    st.altair_chart(line_chart, use_container_width=True)

# The right side
with col2:
    # Highest and lowest price days
    max_day = df.loc[df['Close'].idxmax()].copy()
    min_day = df.loc[df['Close'].idxmin()].copy()

    max_day['Close'] = round(max_day['Close'], 2)
    min_day['Close'] = round(min_day['Close'], 2)

    max_day_date = max_day['Date'].strftime('%Y-%m-%d')
    min_day_date = min_day['Date'].strftime('%Y-%m-%d')

    st.subheader("Highest and Lowest Price Days", divider="green")
    st.write(f"Highest Price Day: {max_day_date} | Close Price: {max_day['Close']} $")
    st.write(f"Lowest Price Day: {min_day_date} | Close Price: {min_day['Close']} $")

    # Metrics for stock info
    st.subheader("Stock Metrics", divider="green")
    
    col1, col2, col3 = st.columns(3, border=True)
    col1.metric("Stock Price", "140.22$", "+341,702.12%")
    col2.metric("Days Since Public", "9,461")
    col3.metric("Current Marketcap", "3.23T ")
    
    col4, col5, col6 = st.columns(3, border=True)
    col4.metric("52 Week High", "315.76$")
    col5.metric("52 Week Low", "124.46$")
    col6.metric("Volume", "1.2M")

    # df_snippet = df.tail(50)
    # st.dataframe(df_snippet, use_container_width=True)
