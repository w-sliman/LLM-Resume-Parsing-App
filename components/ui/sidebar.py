import streamlit as st
from components.utils import extract_resume_text, convert_dates_to_datetime, is_valid_email
from components.llm_resume_parser import llm_resume_parser
from components.utils import read_pdf_text


resumes_for_testing = {"resume1": "./resumes_for_testing/resume1.pdf",
                       "resume2": "./resumes_for_testing/resume2.pdf",
                       "resume3": "./resumes_for_testing/resume3.pdf"}

def sidebar_section(job_title):

    with st.sidebar:

        resume_file = st.file_uploader("**Upload Your Resume (PDF, Word)**", type=["pdf","docx"])


        if 'candidate_data' not in st.session_state:
            st.session_state.candidate_data = {}

        if resume_file:
            resume_text = extract_resume_text(resume_file)
            
            parsed_candidate_data = llm_resume_parser.invoke({"job_title": job_title, "resume_text":resume_text})
            
            if "parsed_candidate_data" not in st.session_state:
                st.session_state.parsed_candidate_data = parsed_candidate_data
                st.session_state.candidate_data = convert_dates_to_datetime(parsed_candidate_data)

                if ("email" in st.session_state.candidate_data) and not is_valid_email(st.session_state.candidate_data["email"]):
                    st.session_state.candidate_data["email"] = ""