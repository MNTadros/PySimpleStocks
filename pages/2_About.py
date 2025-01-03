import streamlit as st

st.set_page_config(page_title="About WhatIS NVDA", page_icon=":books:", layout="wide")

st.title("About: :rainbow[WhatIS][:green[NVDA]]")

st.markdown("---")

st.write("""
### WhatIS is a platform designed to provide comprehensive information on a wide range of topics.
Our goal is to offer clear, concise, and accurate explanations to help you understand complex subjects with ease with a little bit of humor and some data visualization.
""")

st.subheader("Our Mission")
st.write("""
Our mission is to make knowledge accessible to everyone. We believe that understanding is the key to progress, 
and we strive to break down barriers to information by providing high-quality content that is easy to understand.
""")

st.subheader("What You Will Find Here")
st.write("""
- Access to more detailed articles on various topics
- Some fun facts about the topic
- Up-to-date information and updates
- Interactive tools and features to enhance your learning experience
""")

st.subheader("Get Involved")
st.write("""
We encourage you to get involved by providing feedback, suggesting new topics, and sharing our content with others. 
Together, we can build a community of learners and knowledge seekers. Contact us below!
""")

st.markdown("### Contact Us")

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

# Add the contact form
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
