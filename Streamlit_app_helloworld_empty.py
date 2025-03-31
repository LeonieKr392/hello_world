#import streamlit

import streamlit as st

# Set page config for a nicer look
st.set_page_config(page_title="Fun Hello World App", page_icon="👋")

# create a title Hello World App with custom styling
st.title("👋 Hello World App")

# Add a sidebar for customization
with st.sidebar:
    st.header("Customize Your Greeting")
    text_color = st.color_picker("Pick a text color", "#000000")
    text_size = st.slider("Text size", 12, 48, 24)

# create a text input for the user to enter their name
name = st.text_input("Enter your name")

# Add some fun emoji reactions
st.write("How are you feeling today?")
col1, col2, col3 = st.columns(3)
with col1:
    happy = st.button("😊 Happy")
with col2:
    excited = st.button("🎉 Excited")
with col3:
    sleepy = st.button("😴 Sleepy")

# create a button to say hello with custom styling
if st.button("Say hello"):
    st.markdown(f'<p style="color: {text_color}; font-size: {text_size}px;">Hello {name}! 👋</p>', unsafe_allow_html=True)
    
    # Show reaction message
    if happy:
        st.balloons()
        st.write("Yay! That's great! 🎈")
    elif excited:
        st.snow()
        st.write("Woo-hoo! Let's celebrate! 🎊")
    elif sleepy:
        st.write("Maybe you need some coffee? ☕")

# Add a fun fact section
with st.expander("Click for a fun fact!"):
    st.write("Did you know? The first computer programmer was a woman named Ada Lovelace! 💻")


