import streamlit as st
import requests
from io import BytesIO

# Backend API URL
API_URL = "http://127.0.0.1:8000/api"

# Sidebar Navigation
st.sidebar.title("AI Assistant Diagnosis Tool")
page = st.sidebar.radio("Go to", ["Patient Interface", "Doctor Assistant Interface", "Main Doctor Interface"])

# Patient Interface
if page == "Patient Interface":
    st.title("Patient Registration & Diagnosis")
    with st.form("patient_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        mobile = st.text_input("Mobile Number")
        address = st.text_area("Address")
        height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
        weight = st.number_input("Weight (kg)", min_value=10, max_value=200, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        symptoms = st.text_area("Describe Your Symptoms")
        medical_history = st.text_area("Medical History")
        files = st.file_uploader("Upload Medical Reports", accept_multiple_files=True)
        submit = st.form_submit_button("Submit")
    
    if submit:
        patient_data = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "address": address,
            "height": height,
            "weight": weight,
            "gender": gender,
            "symptoms": symptoms,
            "medical_history": medical_history
        }
        response = requests.post(f"{API_URL}/patients/", json=patient_data)
        if response.status_code == 201:
            st.success("Patient Data Submitted Successfully!")
        else:
            st.error("Failed to Submit Data")

# Doctor Assistant Interface
elif page == "Doctor Assistant Interface":
    st.title("Doctor Assistant Dashboard")
    
    response = requests.get(f"{API_URL}/patients/")
    if response.status_code == 200:
        patients = response.json()
        if patients:
            patient_options = {f"{p['name']} (ID: {p['id']})": p["id"] for p in patients}
            selected_patient = st.selectbox("Select Patient", list(patient_options.keys()))
            patient_id = patient_options[selected_patient]

            # Fetch Patient Data
            if st.button("Fetch Patient Data"):
                patient_response = requests.get(f"{API_URL}/patients/{patient_id}")
                if patient_response.status_code == 200:
                    st.json(patient_response.json())
                else:
                    st.error("Patient Not Found")
        else:
            st.warning("No patients found. Please add a patient first.")
    else:
        st.error("Failed to fetch patient data.")
    
    with st.form("medical_form"):
        blood_pressure = st.text_input("Blood Pressure")
        temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
        diabetes_status = st.selectbox("Diabetes Status", ["Normal", "Pre-Diabetes", "Diabetic"])
        submit_medical = st.form_submit_button("Submit Medical Data")
    
    if submit_medical:
        medical_data = {
            "patient": patient_id,
            "blood_pressure": blood_pressure,
            "temperature": temperature,
            "diabetes_status": diabetes_status
        }
        response = requests.post(f"{API_URL}/medical/", json=medical_data)
        if response.status_code == 201:
            st.success("Medical Data Submitted Successfully!")
        else:
            st.error("Failed to Submit Medical Data")

# Main Doctor Interface
elif page == "Main Doctor Interface":
    st.title("Doctor's Review Panel")
    response = requests.get(f"{API_URL}/patients/")
    if response.status_code == 200:
        patients = response.json()
        if patients:
            patient_options = {f"{p['name']} (ID: {p['id']})": p["id"] for p in patients}
            selected_patient = st.selectbox("Select Patient", list(patient_options.keys()))
            patient_id = patient_options[selected_patient]

            if st.button("Get Full Patient Record"):
                patient_response = requests.get(f"{API_URL}/patients/{patient_id}/full")
                if patient_response.status_code == 200:
                    st.json(patient_response.json())
                else:
                    st.error("Patient Data Not Found")
    else:
        st.error("Failed to fetch patient data.")
    
    diagnosis = st.text_area("Final Diagnosis")
    treatment_plan = st.text_area("Treatment Plan")
    if st.button("Submit Diagnosis & Treatment"):
        diagnosis_data = {"patient": patient_id, "diagnosis": diagnosis, "treatment_plan": treatment_plan}
        response = requests.post(f"{API_URL}/diagnosis/", json=diagnosis_data)
        if response.status_code == 201:
            st.success("Diagnosis Submitted Successfully!")
        else:
            st.error("Failed to Submit Diagnosis")
    
    st.subheader("Communication Tools")
    if st.button("Start Video Call"):
        st.write("Launching Video Call...")
    chat_message = st.text_input("Send a message")
    if st.button("Send Message"):
        st.write(f"Sent: {chat_message}")