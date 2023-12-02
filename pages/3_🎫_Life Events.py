from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.title("Life Events")

# ---- LOAD ASSETS ----
video1 = open("video/Classmates.mp4", "rb")
video2 = open("video/Besties.mp4", "rb")

# ---- LIFE EVENTS ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.video(video1)
    with text_column:
        st.subheader("Mabua Beach")
        st.write(
            """
            October 17, 2023, This is the day we just finished the midterm exam and my classmates planned for us to take a bath in Mabua where the scenery is so beautiful, you can really feel the sea breeze and the pebbles on your feet
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.video(video2)
    with text_column:
        st.subheader("Punta Bilar")
        st.write(
            """
            November 12, 2023, Winter is almost here but I can still feel the warmth of the weather. So here we are, with my friends and here bathing in the sea at Punta Bilar where my friend Pychine lives nearby
            """
        )

