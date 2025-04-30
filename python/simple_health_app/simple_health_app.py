import streamlit as st
import random

# Symptom Checker Functions
def check_symptom(symptom):
    symptoms_database = {
        "fever" : "You might have an infection. Please stay hydrated and monitor your temperature.",
        "headache" : "It could be stress or dedydration. Try resting and drinking water.",
        "cough" : "Possible common cold or respiratory infection. If persistent, seek medical advice.",
        "stomach ache" : "Could be indigestion or food-related. Watch your diet and stay hydrated.",
        "fatigue" : "Might be due to lack of sleep or stress. Ensure proper rest."
    }
    return symptoms_database.get(symptom.lower(), "Symptom not recognized. Please consult a healthcare provider.")

def run_symptom_checker():
    st.subheader("Symptom Checker")
    symptom  = st.text_input("Enter your symptom: ").lower()
    st.write("Symptoms include fever, headache, cough, stomach ache, and fatigue")
    if st.button("Check Symptom"):
        result = check_symptom(symptom)
        st.write(result)
        
        
# Sleep Tracker Functions
def add_sleep_record(hours, sleep_records):
    sleep_records.append(hours)
    
def average_sleep(sleep_records):
    if not sleep_records:
        return 0
    return sum(sleep_records) / len(sleep_records)

def run_sleep_tracker():
    st.subheader("Sleep Tracker")
    if "sleep_records" not in st.session_state:
        st.session_state.sleep_records = []
        
    hours = st.number_input("Enter hours of sleep last night: ", min_value=0.0, step=0.5)
    if st.button("Add Sleep Record"):
        add_sleep_record(hours, st.session_state.sleep_records)
        st.success(f"Recorded {hours} hours of sleep.")
        
    if st.session_state.sleep_records:
        avg_sleep = average_sleep(st.session_state.sleep_records)
        st.info(f"Average Sleep Duration: {avg_sleep:.2f} hours")
        
# Health Tip Generator Functions
def generate_health_tip():
    health_tips = [
        "Drink plenty of water daily.",
        "Exercise regularly to maintain your health.",
        "Eat a balanced diet rich in fruits and vegetables.",
        "Get at least 7-8 hours of sleep each night.",
        "Take short breaks during work to avoid burnout.",
        "Practice mindfulness and stress-reducing activities.",
        "Avoid excessive sugar and processed foods."
    ]
    
    return random.choice(health_tips)

def run_health_tip_generator():
    st.subheader("Health Tip Generator")
    if st.button("Get Health Tip"):
        tip = generate_health_tip()
        st.success(tip)
        
# BMI Calculator Functions
def calculate_bmi(weight, height):
    if height <= 0:
        return 0
    return(weight / (height ** 2))

def run_bmi_calculator():
    st.subheader("BMI Calculator")
    weight = st.slider("Enter your weight (in Kilograms):", min_value=1, max_value=200, value=70)
    height = st.slider("Enter your height (in meters): ", min_value=0.0, max_value=3.0, step=0.01)
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        if bmi == 0:
            st.error("Height must be greater than zero.")
        else:
            st.success(f"Your BMI is: {bmi:.2f}")
            
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.info("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.info("You are overweight.")
            else: 
                st.info("You are obese")
                
# Main Streamlit App
def main():
    st.title("Simple Health App")
    st.sidebar.title("Navigation")
    
    app_options = ["Symptom Checker", "Sleep Tracker", "Health Tip Generator", "BMI Calculator"]
    choice = st.sidebar.selectbox("Choose an app:", app_options)
    
    if choice == "Symptom Checker":
        run_symptom_checker()
    elif choice == "Sleep Tracker":
        run_sleep_tracker()
    elif choice == "Health Tip Generator":
        run_health_tip_generator()
    elif choice == "BMI Calculator":
        run_bmi_calculator()

if __name__ == "__main__":
    main()
