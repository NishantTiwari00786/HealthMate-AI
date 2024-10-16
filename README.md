
# **HealthMate-AI**

**HealthMate-AI** is an AI-powered virtual doctor that helps users diagnose common health conditions based on symptoms. It leverages machine learning models to analyze user input and provides possible diagnoses, over-the-counter medication recommendations, and additional advice, such as when to seek medical help. This model is currently under construction, and its estimated completion date is December 2024. 

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Folder Structure](#folder-structure)
- [Current Work in Progress](#current-work-in-progress)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

---

## **Project Overview**
HealthMate-AI provides a virtual healthcare assistant that allows users to input their symptoms and receive potential diagnoses. The goal is to make basic healthcare more accessible by using AI to reduce the barrier to medical advice. This project currently includes:

- Symptom-to-condition mapping based on predefined datasets.
- Machine learning models, such as RandomForestClassifier, to provide predictions based on symptoms.
- A flexible system to add more symptoms and conditions over time.
  
---

## **Installation**

To install and set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/NishantTiwari00786/HealthMate-AI.git
    cd HealthMate-AI
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scriptsctivate
    ```

---

## **Usage**

To run HealthMate-AI locally:

1. **Run the Symptom Diagnosis Application**:
    ```bash
    python At_home_doctor.py
    ```
    This script allows you to input symptoms and provides a diagnosis based on predefined symptom-to-condition mapping.

2. **Train the Model**:
    You can retrain the Random Forest model with new data using the following:
    ```bash
    python Model_training.py
    ```
    This script handles the model training and saves the trained model for later use.

3. **Handling Datasets**:
    Use the `Handling_dataset.py` script to manage and preprocess datasets.

---

## **Model Information**

The core machine learning model used in this project is a **Random Forest Classifier**. It has been trained on a dataset that maps various symptoms to diseases.

### **Model Features**:
- The model takes in symptoms such as "Fever", "Cough", "Fatigue", etc.
- Provides a potential diagnosis based on the presence of these symptoms.
  
To adjust the model parameters or retrain it with new data, edit the file `Model_training.py`.

---

## **Folder Structure**

```
HealthMate-AI/
│
├── At_home_doctor.py             # Symptom diagnosis code
├── Handling_dataset.py           # Dataset processing and handling
├── Model_training.py             # Model training code
├── README.md                     # Project overview (this file)
└── data/                         # Datasets and data files
```

---

## **Current Work in Progress**

- **Improving Symptom Database**: Adding more comprehensive symptoms and conditions.
- **Model Enhancements**: Improving the accuracy of the Random Forest model by fine-tuning parameters and adding more training data.
- **Integrating a Feedback System**: Creating a feedback loop where users can provide real-time feedback on the accuracy of their diagnosis.

---

## **Future Plans**

Here are some additional features and enhancements being planned:

1. **Symptom Scraping from Reputable Sources**:
   - Plan to implement web scraping to automatically update the symptom-to-condition dictionary from medical websites.
   - Sources under consideration include sites like Mayo Clinic and WebMD.
   
2. **Web Interface**:
   - Build a web-based interface using Flask or Django to make the platform more accessible.
   - Users will be able to input symptoms through a user-friendly web interface.
   
3. **Integration with APIs**:
   - Connect to existing medical databases via APIs to provide more accurate and updated diagnoses.

4. **AI Expansion**:
   - Explore more advanced machine learning models such as **Neural Networks** to enhance the prediction capabilities.
   - Investigate the use of **NLP (Natural Language Processing)** to allow users to input symptoms in natural language format (e.g., "I have a headache and a sore throat").

---

## **Contributing**

This project is closed for contributions; once the model works as per my expectations, the codebase will be available. 

---
