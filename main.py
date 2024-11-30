# Import the Streamlit library
import streamlit as st

# Set the title of the app
st.title("Welcome to My Simple Streamlit App!")

# Add a text input for the user's name
name = st.text_input("Enter your name:")

# Add a button to greet the user
if st.button("Submit"):
    if name:
        st.write(f"Hello, {name}! 👋 Welcome to Streamlit!")
    else:
        st.write("Please enter your name to proceed.")
