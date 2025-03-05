from random import choice
import streamlit as st
import helper
# Streamlit app
st.title("Sentiment Analysis App")
choice = st.selectbox("Choose a model", ["torch nn", "Random Forest"])
def analyse():
    if st.button("Analyze"):
        if user_input:
            sentiment = helper.predict_sentiment(user_input)
            st.write(f"Sentiment: {sentiment}")
        else:
            st.write("Please enter some text to analyze.")
examples = [
    "The stock market crashed today, causing widespread panic among investors.", 
    "A new species of bird has been discovered in the Amazon rainforest.", 
    "The local football team won the championship after a thrilling match.",
    "The weather today is sunny with a chance of rain.",
    "The new restaurant in town has received excellent reviews.",
    "The government has announced a new policy to boost the economy.",
    "Custom Input"
]
example_choice = st.selectbox("choose a example news", examples)
if example_choice:
    user_input = example_choice
    if example_choice == "Custom Input":
        user_input = st.text_area("Input Text")
        analyse()
    else:
        st.write(f"Input: {user_input}")
        analyse()
