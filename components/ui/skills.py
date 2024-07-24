import streamlit as st

def skills_section():

    st.write("## Skills")

    def onchange_skill_checkbox(skill_id):

        if st.session_state[skill_id]:
            return

        skill_to_remove = skill_id.split("_")[0]
        st.session_state.candidate_data["skills"] = [skill for skill in st.session_state.candidate_data["skills"] if skill != skill_to_remove]


    def add_new_skill():

        if st.session_state.new_skill_input == '':
            return
        
        new_skill = st.session_state.new_skill_input.strip().lower()
        
        if "skills" not in st.session_state.candidate_data:
            st.session_state.candidate_data["skills"] = []

        skills = [skill.lower() for skill in st.session_state.candidate_data["skills"]]

        if new_skill not in skills:
            st.session_state.candidate_data["skills"].append(new_skill.capitalize())
        
        st.session_state.new_skill_input = ''


    with st.container(border= True):

        #skills = st.session_state.skills

        col1, col2, col3, col4 = st.columns(4)
        if "skills" in st.session_state.candidate_data:
            for i, skill in enumerate(st.session_state.candidate_data["skills"]):
                skill_id = f"{skill}_{i}"
                if i % 4 == 0:
                    col1.checkbox(skill, key=skill_id, value=True, on_change=onchange_skill_checkbox, args=(skill_id,))
                elif i % 4 == 1:
                    col2.checkbox(skill, key=skill_id, value=True, on_change=onchange_skill_checkbox, args=(skill_id,))
                elif i % 4 == 2:
                    col3.checkbox(skill, key=skill_id, value=True, on_change=onchange_skill_checkbox, args=(skill_id,))
                elif i % 4 == 3:
                    col4.checkbox(skill, key=skill_id, value=True, on_change=onchange_skill_checkbox, args=(skill_id,))

        st.write("#### Add Skill")
        col1, col2 = st.columns(2)
        new_skill_input = col1.text_input("Add a new skill", label_visibility="collapsed", key="new_skill_input", on_change=add_new_skill)
        add_skill_button = col2.button("Add Skill", on_click=add_new_skill)