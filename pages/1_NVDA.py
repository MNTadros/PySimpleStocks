import pandas as pd
import streamlit as st
import altair as alt

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Price Change %'] = df['Close'].pct_change() * 100
    return df

st.set_page_config(page_title="NVDA Stock Analysis", page_icon="📊", layout="wide")

banner_html = """
<div style="background-color:red; padding:20px; text-align:center; font-size:20px; color:white;">
    <strong>⚠️ DISCLAIMER: None of this is financial advice. Treat this information as educational only! 
                            All this information is as of November 2024.⚠️</strong>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

nvda_path = './data/NVDA.csv'
df = load_data(nvda_path)

@st.cache_data
def calculate_technical_indicators(df):
    short_window = 20
    long_window = 50
    shares_outstanding = 2.5e9
    df['20-Day MA'] = df['Close'].rolling(window=short_window).mean()
    df['50-Day MA'] = df['Close'].rolling(window=long_window).mean()
    df['Market Cap ($B)'] = (df['Close'] * shares_outstanding) / 1e9
    return df

df = calculate_technical_indicators(df)

st.title("NVIDIA :green[[NVDA]] Stock Analysis")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Key Financial Ratios", divider="green")
    st.write(""" 
    - P/E Ratio: 92.3
    - EPS: 3.12
    - Dividend Yield: 0.12%
    - ROE: 45.6%
    - Debt to Equity: 0.41
    """)

with col2:
    st.subheader("Definitions", divider="green")
    st.write("""
    - **P/E Ratio (Price-to-Earnings)**: A ratio that compares a company’s share price to its earnings per share, showing how much investors are willing to pay for each dollar of earnings.
    - **EPS (Earnings Per Share)**: A company’s profit divided by the number of outstanding shares, indicating how much profit is attributed to each share.
    - **Dividend Yield**: A financial ratio that shows how much cash a company returns to shareholders in the form of dividends, relative to its stock price.
    - **ROE (Return on Equity)**: A measure of financial performance, calculated by dividing net income by shareholders’ equity, indicating how efficiently a company uses equity to generate profits.
    - **Debt to Equity**: A ratio indicating the proportion of debt a company uses to finance its assets compared to the equity provided by shareholders.
    """)

with col1:
    st.subheader("Closing Price Over Time with Moving Averages", divider="green")
    closing_price_chart = alt.Chart(df).mark_line(color='green').encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Close:Q', title='Close Price'),
        tooltip=['Date:T', 'Close:Q']
    )

    ma_20_chart = alt.Chart(df).mark_line(color='blue').encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('20-Day MA:Q', title='20-Day Moving Average'),
        tooltip=['Date:T', '20-Day MA:Q']
    )

    ma_50_chart = alt.Chart(df).mark_line(color='red').encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('50-Day MA:Q', title='50-Day Moving Average'),
        tooltip=['Date:T', '50-Day MA:Q']
    )

    combined_chart = alt.layer(closing_price_chart, ma_20_chart, ma_50_chart).properties(
        width=800,
        height=400,
        title="NVIDIA (NVDA) Closing Price with 20-Day and 50-Day Moving Averages"
    ).interactive()

    legend_data = pd.DataFrame({
        'Line': ['Close Price', '20-Day Moving Avg', '50-Day Moving Avg'],
        'Color': ['green', 'blue', 'red']
    })
    legend_chart = alt.Chart(legend_data).mark_rect().encode(
        y=alt.Y('Line:N', title='Legend', axis=alt.Axis(labelAngle=0)),
        color=alt.Color('Color:N', scale=None, legend=None)
    ).properties(height=100)
    
    st.altair_chart(combined_chart & legend_chart, use_container_width=True)

    st.write("""
    **Analysis**: The green line represents the stock's closing price, while the blue and red lines represent the 20-day and 50-day moving averages, respectively. 
    - **What to look out for**: 
        - A stock price crossing above the 20-day moving average (MA) may indicate an upward trend or buying signal.
        - A crossover of the 20-day MA above the 50-day MA is known as a "golden cross" and is often viewed as a bullish signal.
        - A crossover below these moving averages may indicate a downtrend or bearish signal.
    - **Importance**: Moving averages help smooth out price action and make it easier to spot trends.
    """)

    st.subheader("Daily Price Change Percentage", divider="green")
    price_change_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Price Change %:Q', title='Daily Price Change (%)'),
        tooltip=['Date:T', 'Price Change %:Q']
    ).properties(
        width=800,
        height=300,
        title="Daily Price Change Percentage"
    ).interactive()
    st.altair_chart(price_change_chart, use_container_width=True)

    st.write("""
    **Analysis**: This bar chart shows the daily percentage change in the stock price. Each bar represents how much the stock price changed from the previous day, as a percentage.
    - **What to look out for**: 
        - Large positive or negative changes in price could indicate high volatility or significant market news.
        - Consistently high positive percentage changes may indicate strong bullish sentiment, while negative changes might signal bearish sentiment or sell-offs.
    - **Importance**: Understanding daily fluctuations helps to assess short-term momentum and potential volatility in the stock price.
    """)

with col2:
    max_day = df.loc[df['Close'].idxmax()].copy()
    min_day = df.loc[df['Close'].idxmin()].copy()

    max_day['Close'] = round(max_day['Close'], 2)
    min_day['Close'] = round(min_day['Close'], 2)

    max_day_date = max_day['Date'].strftime('%Y-%m-%d')
    min_day_date = min_day['Date'].strftime('%Y-%m-%d')

    st.subheader("Highest and Lowest Price Days", divider="green")
    st.write(f"Highest Price Day: {max_day_date} | Close Price: {max_day['Close']} $")
    st.write(f"Lowest Price Day: {min_day_date} | Close Price: {min_day['Close']} $")

    st.subheader("Market Capitalization Over Time", divider="green")
    market_cap_chart = alt.Chart(df).mark_area().encode(
        x='Date:T',
        y='Market Cap ($B):Q',
        tooltip=['Date:T', 'Market Cap ($B):Q']
    ).properties(
        width=800,
        height=300,
        title="Market Capitalization Over Time (in Billions)"
    ).interactive()
    st.altair_chart(market_cap_chart, use_container_width=True)

    st.write("""
    **Analysis**: The market capitalization chart shows how the company's market cap has evolved over time. The market cap is calculated by multiplying the stock price by the total number of shares outstanding.
    - **What to look out for**:
        - Significant increases in market cap can indicate strong growth, attracting investor interest.
        - A decrease in market cap may indicate a loss of investor confidence or a market correction.
    - **Importance**: Market cap is a key metric for evaluating the size of a company and can influence investor decisions regarding the risk and potential of the stock.
    """)

    st.subheader("Stock Metrics", divider="green")
    col1, col2, col3 = st.columns(3, border=True)
    col1.metric("Stock Price", "140.22$")
    col2.metric("Days Since Public", "9,461")
    col3.metric("Current Marketcap", "3.23T ")

    col4, col5, col6 = st.columns(3, border=True)
    col4.metric("52 Week High", "315.76$")
    col5.metric("52 Week Low", "124.46$")
    col6.metric("Volume", "1.2M")
