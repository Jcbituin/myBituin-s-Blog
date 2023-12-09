import streamlit as st


st.title("Personal Info")

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
    
