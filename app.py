import streamlit as st
import chatter
import os
from dotenv import load_dotenv

load_dotenv()

chat = chatter.Chatter()

# Custom CSS styles
st.markdown(
    """
<style>
    body {
        background-color: #f0f0f5;
    }
    .stButton>button {
        background-color: #4B0082;
        color: white;
    }
    .stButton>button:hover {
        background-color: #6A5ACD;
    }
    .stSidebar .sidebar-collapse {
        background-color: #4B0082;
        color: white;
    }
    .stSidebar .sidebar-content {
        background-color: #6A5ACD;
    }
    .stTextInput>div>div>input, .stTextArea textarea {
    background-color: #E6E6FA;
    }
    .output-box {
        background-color: #D8BFD8;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🐦 Titter GPT")
st.subheader("Generate your tweets and threads with ChatGPT")

with st.form("tweet_form"):
    topic = st.text_input(label="Topic", value="")
    message = st.text_area(label="Message", value="", height=100)
    tone = st.radio("Tone", ("excited", "happy", "neutral", "sad", "angry"), index=2)
    act_like = st.text_input(label="Act like (job title)", value="")
    generate_tweet = st.form_submit_button("Generate Tweets")

if generate_tweet:
    job = {
        "topic": topic,
        "message": message,
        "tone": tone,
        "act_like": act_like,
    }
    tweets = chat.tweets_from_job(job=job)
    for i, tweet in enumerate(tweets):
        with st.container():
            st.subheader(f"Tweet Style {i + 1}")
            st.markdown(
                f'<div class="output-box" style="padding: 10px; border-radius: 5px;">{tweet}</div>',
                unsafe_allow_html=True,
            )

with st.sidebar:
    st.header("Links")
    st.markdown(
        "[About ChatGPT](https://openai.com/blog/chatgpt/)", unsafe_allow_html=True
    )
    st.markdown(
        "[This app on GitHub](https://github.com/rimabuilds/twitter-GPT)",
        unsafe_allow_html=True,
    )
    st.markdown(
        "[rimabuilds GitHub](https://rimabuilds.github.io/)", unsafe_allow_html=True,
    )
