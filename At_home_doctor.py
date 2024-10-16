
# Symptom-to-condition dictionary (you can expand this)
symptom_conditions = {
    "fever": "flu or cold",
    "headache": "migraine or dehydration",
    "stomach pain": "indigestion or food poisoning",
    "cough": "common cold or respiratory infection",
    "fatigue": "stress or lack of sleep",
    "bloating": "gas or poor digestion",
    "sore throat": "throat infection or flu"
}

# Basic symptom input system
def get_symptom():
    print("Welcome to the At-Home Doctor AI!")
    print("Please enter the symptoms you're experiencing, separated by commas.")
    symptoms_input = input("Symptoms: ").lower()
    symptoms = symptoms_input.split(",")  # Split symptoms by comma
    return [symptom.strip() for symptom in symptoms]  # Remove extra spaces

# Function to match symptoms to conditions
def diagnose(symptoms):
    conditions = []
    for symptom in symptoms:
        condition = symptom_conditions.get(symptom, "Unknown condition")
        conditions.append(f"Symptom: {symptom}, Possible Condition: {condition}")
    return conditions

# Main program
user_symptoms = get_symptom()  # Get user input
diagnosis = diagnose(user_symptoms)  # Get diagnosis based on symptoms

print("\nHere are your results:")
for result in diagnosis:
    print(result)
