
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "/Users/nishanttiwari/Desktop/Disease_symptom_and_patient_profile_dataset.csv"
df = pd.read_csv(file_path)
print(df.head())

# Checking the data structure
print(df.columns)
print(df.info())

# Replace 'Yes' with 1 and 'No' with 0 for symptom columns
symptom_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']
df[symptom_columns] = df[symptom_columns].replace({'Yes': 1, 'No': 0}).astype(int)

# Group by 'Disease' and sum the occurrences
symptom_counts = df.groupby('Disease')[symptom_columns].sum()
print(symptom_counts)

# Plot the frequency of 'Fever' across different diseases
plt.figure(figsize=(12, 6))  # Adjust the figure size
sns.countplot(x='Disease', hue='Fever', data=df)
plt.xticks(rotation=90)  # Rotate x-axis labels
plt.tight_layout()  # Ensure the layout fits well
plt.show()

# Filter to get top 10 most frequent diseases
top_diseases = df['Disease'].value_counts().head(10).index
df_top_diseases = df[df['Disease'].isin(top_diseases)]

# Plot again with the top 10 diseases
plt.figure(figsize=(12, 6))
sns.countplot(x='Disease', hue='Fever', data=df_top_diseases)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

