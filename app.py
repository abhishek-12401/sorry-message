import streamlit as st

# Page config
st.set_page_config(page_title="Sorry 😬", page_icon="😬", layout="centered")

# Title with emoji
st.markdown("<h1 style='text-align: center; font-size: 72px;'>😬</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>I'm Really Sorry 😔</h2>", unsafe_allow_html=True)

# Some space
st.write("")

# Explanation
st.markdown("<p style='text-align: center; font-size:18px;'>Please forgive me if you can. 🙏</p>", unsafe_allow_html=True)

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Maaf kiya 🥺😌"):
        st.success("Thank you! You're the best ❤️")

with col2:
    if st.button("tune koi galti hi nhi kiya😁"):
        st.warning("It's okay, I understand... 😢")
