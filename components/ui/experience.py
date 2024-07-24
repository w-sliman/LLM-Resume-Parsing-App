import streamlit as st

def experience_section():

    st.write("## Experience")

    with st.container(border= True):
        if st.session_state.candidate_data.get("jobs"):
            for i, item in enumerate(st.session_state.candidate_data["jobs"]):

                col1, col2 = st.columns(2)
                col1.markdown("##### Work Experience " + str(i + 1))
                
                
                current_job = col2.checkbox("**Current Job**", key="current_job" + str(i), value=item.get("current_job", False))

                col1, col2 = st.columns(2)
                started_at = col1.date_input("**From**", key="started_at" + str(i), value=item.get("started_at", None))
                
                
                if not st.session_state["current_job" + str(i)]:
                    ended_at = col2.date_input("**To**", key="ended_at" + str(i), value=item.get("ended_at", None))
                else:
                    ended_at = None

                col1, col2 = st.columns(2)
                job_title = col1.text_input("**Job Title**", key="job_title" + str(i), value=item.get("job_title", ""))
                description = col2.text_area("**Job Description**", key="description" + str(i), value=item.get("job_description", ""))
                
                #col1, col2 = st.columns(2)
                remove_experience_button = st.button(f"Remove Experience {i + 1}", key=f"remove_experience_{i}")
                
                st.session_state.candidate_data["jobs"][i] = {
                    "job_title": job_title,
                    "job_description": description,
                    "started_at": started_at,
                    "ended_at": ended_at,
                    "current_job": current_job
                }
                
                if remove_experience_button:
                    st.session_state.candidate_data["jobs"].pop(i)
                    st.rerun()

        if "new_experience" not in st.session_state:
                st.session_state.new_experience = {}

        if "new_experience_clicked" not in st.session_state:
            st.session_state.new_experience_clicked = False
        
        if st.session_state.new_experience_clicked:
            
            st.write("#### Update New Experience")

            col1, col2 = st.columns(2)
            st.session_state.new_experience["started_at"] = col1.date_input("**From**", key="from", value= st.session_state.new_experience.get("started_at",None))
            st.session_state.new_experience["ended_at"] = col2.date_input("**To**", key="to", value= st.session_state.new_experience.get("ended_at",None))

            col1, col2 = st.columns(2)
            st.session_state.new_experience["job_title"] = col1.text_input("**Job Title**", key="job_title", value= st.session_state.new_experience.get("job_title",""))
            st.session_state.new_experience["job_description"] = col2.text_area("**Job Description**", key="job_description", value= st.session_state.new_experience.get("job_description",""))


        new_experience_button = st.button("Add New Experience" if not st.session_state.new_experience_clicked else "Save")

        if new_experience_button:
            if st.session_state.new_experience_clicked:
                if "jobs" not in st.session_state.candidate_data:
                    st.session_state.candidate_data["jobs"] = []
                
                st.session_state.candidate_data["jobs"].append(st.session_state.new_experience.copy())
                st.session_state.new_experience = {}
                st.session_state.new_experience_clicked = False

            else:
                st.session_state.new_experience_clicked = True

            st.rerun()