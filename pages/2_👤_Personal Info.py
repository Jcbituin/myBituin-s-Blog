import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Personal Info")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/db9ae4cd-a20b-407c-811e-4b9065073aec/7EbxAXNC8o.json")

# ---- PERSONAL INFO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            - Name: James Carl Edradan Bituin
            - Age: 18 years old
            - Address: Brgy. Poctoy, Surigao City
            - Birth Place: Surigao City, Surigao Del Norte
            - Graduated in J.R. Clavero Memorial Elementary School
            - Graduated in Surigao del Norte National High School
            - Currently at Surigao del Norte State University as a 1st year collage
            - Course: BSCpE - Bachelor of Science in Computer Engineering
            """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
