import streamlit as st

st.set_page_config(page_title="About WhatIS NVDA", page_icon="📊", layout="wide")

st.title("About: :rainbow[WhatIS][:green[NVDA]]")

st.markdown("---")

st.write("""
### WhatIS is a platform designed to provide comprehensive information on a wide range of topics.
My goal is to offer clear, concise, and accurate explanations to help you understand complex subjects with ease, using data visualization and practical examples.
""")

st.subheader("About Me / Why")
st.write("""
I started WhatIS NVDA with the intention of creating a platform that simplifies learning by breaking down complex ideas into bite-sized, digestible pieces. 
I am passionate about making information accessible to everyone, regardless of their background or prior knowledge. By focusing on clear, understandable explanations and effective visual aids, I aim to empower individuals to grasp difficult concepts and apply that knowledge in their own lives.
""")

st.write("""
I encourage you to get involved by providing feedback, suggesting new topics, and sharing my content with others. 
Together, I believe we can build a community of learners and knowledge seekers. Contact me below!
""")

st.subheader("What You Will Find Here")
st.write("""
- Access to more detailed articles on various topics
- Visual aids like charts, graphs, and diagrams to help clarify concepts
- Useful definitions and relevant (in my opinion) information
""")

st.write("""
I encourage you to get involved by providing feedback, suggesting new topics, and sharing my content with others. 
Together, I believe we can build a community of learners and knowledge seekers. Contact me below!
""")

st.markdown("### Contact Me")

form_css = """
<style>
form {
    max-width: 400px;
    margin-left: 0;
}
input, textarea {
    width: 100%;
    margin: 5px 0;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
button {
    background-color: #16a819;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
}
button:hover {
    background-color: #45a049;
}
</style>
"""
st.markdown(form_css, unsafe_allow_html=True)

# Contact form
contact_form = """
<form action="https://formsubmit.co/3fe49783a31e2c06d7bea8b630e73076" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Type your message here..." required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
