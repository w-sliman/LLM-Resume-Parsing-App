import streamlit as st

def education_section():

    st.write("## Education")

    with st.container(border= True):
        if st.session_state.candidate_data.get("degrees"):
            for i, item in enumerate(st.session_state.candidate_data["degrees"]):

                st.markdown("#### Education " + str(i + 1))

                col1, col2 = st.columns(2)
                degree_type = col1.text_input("**Degree Type**", key="degree_type" + str(i), value=item.get("degree_type", ""))
                major = col2.text_input("**Major**", key="major" + str(i), value=item.get("major", ""))

                col1, col2 = st.columns(2)
                university = col1.text_input("**University**", key="university" + str(i), value=item.get("university", ""))
                graduation_date = col2.date_input("**Graduation Date**", key="graduation_date" + str(i), value=item.get("graduation_date", ""))

                st.session_state.candidate_data["degrees"][i] = {
                    "degree_type": degree_type,
                    "major": major,
                    "university": university,
                    "graduation_date": graduation_date
                }
                
                if st.button(f"Remove Education {i + 1}", key=f"remove_education_{i}"):
                    st.session_state.candidate_data["degrees"].pop(i)
                    st.rerun()

        if "new_education" not in st.session_state:
                st.session_state.new_education = {}

        if "new_education_clicked" not in st.session_state:
            st.session_state.new_education_clicked = False
        
        if st.session_state.new_education_clicked:
            
            st.write("#### New Education")

            col1, col2 = st.columns(2)
            st.session_state.new_education["degree_type"] = col1.text_input("**Degree Type**", key="degree_type", value= st.session_state.new_education.get("degree_type",""))
            st.session_state.new_education["major"] = col2.text_input("**Major**", key="major", value= st.session_state.new_education.get("major",""))

            col1, col2 = st.columns(2)
            st.session_state.new_education["university"] = col1.text_input("**University**", key="university", value= st.session_state.new_education.get("university",""))
            st.session_state.new_education["graduation_date"] = col2.date_input("**Graduation Date**", key="graduation_date", value= st.session_state.new_education.get("graduation_date",None))


        new_education_button = st.button("Add New Education" if not st.session_state.new_education_clicked else "Save")

        if new_education_button:
            if st.session_state.new_education_clicked:
                if "degrees" not in st.session_state.candidate_data:
                    st.session_state.candidate_data["degrees"] = []
                
                st.session_state.candidate_data["degrees"].append(st.session_state.new_education.copy())
                st.session_state.new_education = {}
                st.session_state.new_education_clicked = False

            else:
                st.session_state.new_education_clicked = True

            st.rerun()