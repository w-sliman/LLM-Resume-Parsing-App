import streamlit as st
from components.utils import is_valid_email

def personal_data_section():
    
    st.write("## Personal Data")

    with st.container(border= True):

        col1, col2 = st.columns(2)
        st.session_state.candidate_data["first_name"] = col1.text_input("**First Name**", st.session_state.candidate_data.get("first_name", ""))
        st.session_state.candidate_data["last_name"] = col2.text_input("**Last Name**", st.session_state.candidate_data.get("last_name", ""))
        
        col1, col2 = st.columns(2)
        st.session_state.candidate_data["country_phone_code"] = col1.text_input("**Country Code**", st.session_state.candidate_data.get("country_phone_code", ""))
        st.session_state.candidate_data["phone_number"] = col2.text_input("**Phone Number**", st.session_state.candidate_data.get("phone_number", ""))
        
        col1, col2 = st.columns(2)
        st.session_state.candidate_data["email"] = st.text_input("**Email**", st.session_state.candidate_data.get("email", ""))
        st.session_state.candidate_data["country"] = st.text_input("**Country**", st.session_state.candidate_data.get("country", ""))