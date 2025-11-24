import pandas as pd
import numpy as np
# Read the dataset
df = pd.read_csv('healthcare_patients.csv')
# Function to standardize gender labels
def standardize_gender(gender):
    gender = str(gender).lower().strip()
    if gender in ['m', 'male']:
        return 'Male'
    elif gender in ['f', 'female']:
        return 'Female'
    return 'Other'
# Fill missing values in numeric columns with mean
numeric_columns = df.select_dtypes(include=[np.number]).columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())
# Convert height from cm to meters
if 'height' in df.columns:
    df['height'] = df['height'] / 100
# Standardize gender labels
if 'gender' in df.columns:
    df['gender'] = df['gender'].apply(standardize_gender)
# Drop patient_id column
if 'patient_id' in df.columns:
    df = df.drop('patient_id', axis=1)
# Save the cleaned dataset
df.to_csv('cleaned_healthcare_records.csv', index=False)
# Display the first few rows of cleaned data
print("First few rows of cleaned data:")
print(df.head())
# Display information about the cleaned dataset
print("\nDataset Info:")
print(df.info())