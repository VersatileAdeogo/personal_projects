# Import required libraries
import streamlit as st

# Initialize patient records
if "patients" not in st.session_state:
    st.session_state.patients = {}

# Functions
def add_patient(name, age, gender, condition):
    if name in st.session_state.patients:
        return False
    st.session_state.patients[name] = {"Age": age, "Gender": gender, "Condition": condition}
    return True

def edit_patient(name, age, gender, condition):
    if name in st.session_state.patients:
        st.session_state.patients[name] = {"Age": age, "Gender": gender, "Condition": condition}
        return True
    return False

def delete_patient(name):
    if name in st.session_state.patients:
        del st.session_state.patients[name]
        return True
    return False

def view_patients():
    if not st.session_state.patients:
        st.write("No patient records found.")
    else:
        for name, details in st.session_state.patients.items():
            st.write(f"**Name:** {name}")
            st.write(f"Age: {details['Age']}")
            st.write(f"Gender: {details['Gender']}")
            st.write(f"Gender: {details['Condition']}")
            st.markdown("---")
            
# Pages
def add_patient_page():
    st.subheader("Add Patient Record")
    name = st.text_input("Patient Name")
    age = st.slider("Patient Age",  min_value=1, max_value=130, value=40)
    gender = st.selectbox("Gender", ["Male", "Female"])
    condition = st.text_input("Medical Condition")
    
    if st.button("Add Patient"):
        success = add_patient(name, age, gender, condition)
        if success:
            st.success(f"Patient '{name}' added successfully.")
        else:
            st.error(f"Patient '{name}' already exists.")
            
def edit_delete_patient_page():
    st.subheader("Edit or Delete Patient Record")
    if not st.session_state.patients:
        st.write("No patients available to edit or delete.")
        return

    patient_names = list(st.session_state.patients.keys())
    selected_patient = st.selectbox("Select Patient", patient_names)
    patient_data = st.session_state.patients[selected_patient]
    new_name = st.text_input("Patient Name", value = selected_patient)
    new_age = st.slider("Patient Age",  min_value=1, max_value=130, value=patient_data['Age'])
    new_gender = st.selectbox("Gender", ["Male", "Female"], index=["Male", "Female"].index(patient_data['Gender']))
    new_condition = st.text_input("Medical Condition", value=patient_data['Condition'])
                               
    col1, col2 = st.columns(2)
                               
    with col1:
        if st.button("Update Patient"):
            #Handle if patient name changes
            if new_name != selected_patient:
                delete_patient(selected_patient)
            add_patient(new_name, new_age, new_gender, new_condition)
            st.success(f"Patient '{new_name}' update successfully.")
            
    with col2:
        if st.button("Delete Patient"):
            delete_patient(selected_patient)
            st.success(f"Patient '{selected_patient}' deleted successfully.")
            
def view_patient_page():
    st.subheader("View Patient Records")
    view_patients()
        
    
    
# Main App
def main():
    st.title("Patient Record Management System")
    
    menu = ["Add Patient Record", "Edit/Delete Patient Record", "View Patient Records"]
    choice = st.sidebar.selectbox("Navigate", menu)
    
    if choice == "Add Patient Record":
        add_patient_page()
    elif choice == "Edit/Delete Patient Record":
        edit_delete_patient_page()
    elif choice == "View Patient Records":
        view_patient_page()
        
if __name__ == "__main__":
    main()
