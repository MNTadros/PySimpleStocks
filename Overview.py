import streamlit as st
import pandas as pd

st.set_page_config(page_title="WhatIS NVDA", page_icon="📊", layout="centered")

st.image("./data/imgs/NVDA_FINAL.png", use_container_width=False)
# Article: NVIDIA's Role in the Tech Sector

st.header("NVIDIA's Strategic Position in the Tech World")
st.markdown(""" 
    NVIDIA is one of the most influential tech companies today because of its leading role in artificial intelligence (AI), data centers, and gaming. 
    Led by CEO Jensen Huang, NVIDIA has evolved from focusing on graphics cards to becoming a cornerstone of AI technology. 
    Its advanced GPUs, like the A100 and H100, power AI systems used by major companies like OpenAI, Google, and Microsoft. 
    With its strong hold on AI hardware, NVIDIA remains a key player in this rapidly growing field.
""")
# Full-Stack Leadership in AI and Hardware

st.header("NVIDIA: Leading AI Innovation with a Complete Stack")
st.markdown(""" 
    One of NVIDIA's biggest advantages is offering both hardware and software solutions. 
    Its platform **CUDA** is vital for creating AI and machine learning applications, enabling faster and smarter development. 
    This complete-package approach sets NVIDIA apart, making it a leader in AI by providing tools that span both hardware and software.
""")
# Exploding Stock Price Driven by AI Demand

st.header("Why NVIDIA's Stock Price Is Soaring")
st.markdown(""" 
    NVIDIA's stock price has surged in recent years due to the growing demand for AI technology. 
    Industries like healthcare, autonomous vehicles, and cloud computing depend on NVIDIA's products. 
    As AI adoption spreads, NVIDIA's role as a top supplier of AI hardware further increases its market value.
""")
# The Impact of Passive Investing

st.header("How Passive Investing Affects NVIDIA's Value")
st.markdown(""" 
    Passive investing significantly influences NVIDIA's stock price. Many investors use index funds that automatically include large companies like NVIDIA. 
    Since NVIDIA is part of major indices like the **S&P 500**, its stock benefits from these investments even if people aren't specifically choosing to buy it. 
    Some analysts believe this trend has driven NVIDIA's valuation higher than its core earnings justify.
""")

# The Consequences of Passive Buying

st.header("AI Hype and Passive Buying: A Powerful Combo")
st.markdown(""" 
    The combination of AI enthusiasm and passive buying has propelled NVIDIA's stock to record highs. 
    While its dominance in AI hardware supports a higher price, the rapid rise has raised concerns. 
    Some wonder if the stock truly reflects the company’s future earnings or if it's partly driven by market speculation and automated investments.
""")

# Why Choose WhatIS NVDA?

st.header("Why Use WhatIS NVDA?")
st.markdown(""" 
    WhatIS NVDA offers a detailed analysis of NVIDIA’s strategic position and market performance. Here's what you can expect:
    
    - **In-depth Analysis**: Understand NVIDIA's role in AI, data centers, and gaming.
    - **Historical Context**: See how NVIDIA's stock has evolved over the years.
    - **Investment Insights**: Learn about the factors driving NVIDIA's stock price.
""")

st.header("What Could You Have Bought with a $1,000 Investment in NVDA (2014-2024)?")

st.markdown(""" 
    <style>
        .streamlit-expanderHeader {
            font-size: 1.5rem;
            color: #4CAF50;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            font-size: 1.2rem;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #007BB5;
        }
        .investment-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .investment-year {
            width: 48%;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

price_legend = """
### Price per Object (USD)
<div style="text-align: center;">
    <p><strong><span style="color:red">1 KitKat</span></strong> = $1.50 </p>
    <p><strong><span style="color:green">1 Basketball</span></strong> = $30.00 </p>
    <p><strong><span style="color:grey">1 Smartphone</span></strong> = $500.00 </p>
    <p><strong><span style="color:blue">1 Laptop</span></strong> = $1,000.00 </p>
    <p><strong><span style="color:orange">1 Electric Vehicle</span></strong> = $30,000.00</p>
</div>
"""

st.markdown(price_legend, unsafe_allow_html=True)

investment_explanation = """
<div class="investment-section" style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2015:</strong><br>
        - <span style="color:red">1,163 KitKats</span><br>
        - <span style="color:green">58 Basketballs</span><br>
        - <span style="color:grey">3.5 Smartphones</span><br>
        - <span style="color:blue">1.7 Laptops</span><br>
        - <span style="color:orange">0.05 Electric Cars</span><br>
        <br>Current stock value: <strong>$1,744.84</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2016:</strong><br>
        - <span style="color:red">3,766 KitKats</span><br>
        - <span style="color:green">188 Basketballs</span><br>
        - <span style="color:grey">11.3 Smartphones</span><br>
        - <span style="color:blue">5.7 Laptops</span><br>
        - <span style="color:orange">0.16 Electric Cars</span><br>
        <br>Current stock value: <strong>$5,650.61</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2017:</strong><br>
        - <span style="color:red">6,823 KitKats</span><br>
        - <span style="color:green">341.2 Basketballs</span><br>
        - <span style="color:grey">20.5 Smartphones</span><br>
        - <span style="color:blue">10.3 Laptops</span><br>
        - <span style="color:orange">0.29 Electric Cars</span><br>
        <br>Current stock value: <strong>$10,243.52</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2018:</strong><br>
        - <span style="color:red">4,711 KitKats</span><br>
        - <span style="color:green">235.6 Basketballs</span><br>
        - <span style="color:grey">14.1 Smartphones</span><br>
        - <span style="color:blue">7.1 Laptops</span><br>
        - <span style="color:orange">0.2 Electric Cars</span><br>
        <br>Current stock value: <strong>$7,067.23</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2019:</strong><br>
        - <span style="color:red">8,304 KitKats</span><br>
        - <span style="color:green">415.2 Basketballs</span><br>
        - <span style="color:grey">24.9 Smartphones</span><br>
        - <span style="color:blue">12.5 Laptops</span><br>
        - <span style="color:orange">0.36 Electric Cars</span><br>
        <br>Current stock value: <strong>$12,456.33</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2020:</strong><br>
        - <span style="color:red">18,429 KitKats</span><br>
        - <span style="color:green">921.5 Basketballs</span><br>
        - <span style="color:grey">55.3 Smartphones</span><br>
        - <span style="color:blue">27.7 Laptops</span><br>
        - <span style="color:orange">0.79 Electric Cars</span><br>
        <br>Current stock value: <strong>$27,644.26</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2021:</strong><br>
        - <span style="color:red">41,518.9 KitKats</span><br>
        - <span style="color:green">2,075.9 Basketballs</span><br>
        - <span style="color:grey">124.6 Smartphones</span><br>
        - <span style="color:blue">62.3 Laptops</span><br>
        - <span style="color:orange">1.78 Electric Cars</span><br>
        <br>Current stock value: <strong>$62,278.45</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2022:</strong><br>
        - <span style="color:red">20,630.3 KitKats</span><br>
        - <span style="color:green">1,031.5 Basketballs</span><br>
        - <span style="color:grey">61.9 Smartphones</span><br>
        - <span style="color:blue">31.0 Laptops</span><br>
        - <span style="color:orange">0.89 Electric Cars</span><br>
        <br>Current stock value: <strong>$30,945.47</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2023:</strong><br>
        - <span style="color:red">69,909.3 KitKats</span><br>
        - <span style="color:green">3,495.5 Basketballs</span><br>
        - <span style="color:grey">209.8 Smartphones</span><br>
        - <span style="color:blue">104.9 Laptops</span><br>
        - <span style="color:orange">3.0 Electric Cars</span><br>
        <br>Current stock value: <strong>$104,863.95</strong>
    </div>
    <div class="investment-year" style="border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 5px; width: 200px;">
        <strong>2014 - 2024:</strong><br>
        - <span style="color:red">189,574.7 KitKats</span><br>
        - <span style="color:green">9,478.7 Basketballs</span><br>
        - <span style="color:grey">568.8 Smartphones</span><br>
        - <span style="color:blue">284.4 Laptops</span><br>
        - <span style="color:orange">8.12 Electric Cars</span><br>
        <br>Current stock value: <strong>$284,362.10</strong>
    </div>
</div>
"""

st.markdown(investment_explanation, unsafe_allow_html=True)
