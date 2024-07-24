import streamlit as st

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from components.ui.sidebar import sidebar_section
from components.ui.personal_data import personal_data_section
from components.ui.education import education_section
from components.ui.experience import experience_section
from components.ui.skills import skills_section

# This job_title variable will show up in the page title and will be used by LLM to determine relevant skills:
job_title= "Data Scientist"

# App configuration
st.set_page_config(page_title=f"Applying to {job_title} Vacancy", layout="wide")

st.title(f"Applying to {job_title} Vacancy", anchor="center")

st.write("### *This is a demo for resume parsing with Large Language Models.*")
st.write("Upload your resume on the left sidebar to automatically parse your data.")
st.write("*Warning: the contents of the file you upload will be sent to Groq-API for inference*")

# Sidebar
sidebar_section(job_title= job_title)

# Personal Data Section
personal_data_section()

# Education Section
education_section()

# Experience Section
experience_section()

# Skills Section
skills_section()


st.write("* Clicking the submit button below will only show you the final data dictionary after parsing the resume and performing manual edits on it.*")
submit = st.button('Submit', key="sumbit")

if submit:
    st.divider()
    st.write("### Final Candidate Data:")
    st.write(st.session_state.candidate_data)

