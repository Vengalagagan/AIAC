import pandas as pd
import numpy as np
def standardize_department(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().lower()
    if s == '':
        return np.nan
    if 'human' in s or s == 'hr' or s.startswith('hr') or 'human resources' in s or 'human_resource' in s:
        return 'HR'
    if 'information' in s or s == 'it' or 'technology' in s or 'tech' in s:
        return 'IT'
    if 'finance' in s or 'account' in s:
        return 'Finance'
    if 'sales' in s:
        return 'Sales'
    if 'market' in s:
        return 'Marketing'
    if 'admin' in s or 'administration' in s:
        return 'Administration'
    # fallback: title case
    return s.title()
def clean_employee_dataset(path='sample_employees.csv', out_path='employee_dataset_cleaned.csv'):
    df = pd.read_csv(path)   
    # Salary: remove currency symbols/commas and convert to numeric, impute median
    if 'salary' in df.columns:
        df['salary'] = df['salary'].astype(str).str.replace(r'[\$,]', '', regex=True).str.replace(',', '', regex=False)
        df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
        median_salary = df['salary'].median()
        df['salary'].fillna(median_salary, inplace=True)   
    # Department: standardize names and fill missing with mode (most common)
    if 'department' in df.columns:
        df['department'] = df['department'].apply(standardize_department)
        if df['department'].mode().size > 0:
            mode_dept = df['department'].mode().iloc[0]
        else:
            mode_dept = 'Unknown'
        df['department'].fillna(mode_dept, inplace=True)    
    # Joining date: parse to datetime, fill invalid/missing with median date
    if 'joining_date' in df.columns:
        df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce', infer_datetime_format=True)
        if df['joining_date'].notna().any():
            median_date = df['joining_date'].dropna().median()
            df['joining_date'].fillna(median_date, inplace=True)
        else:
            # if no parsable dates, leave as NaT or set to today's date
            df['joining_date'] = pd.to_datetime(df['joining_date'])   
    # Encode categorical variables: department and job_role using factorize (returns ints)
    if 'department' in df.columns:
        df['department_encoded'], dept_uniques = pd.factorize(df['department'])
    if 'job_role' in df.columns:
        df['job_role'] = df['job_role'].fillna('Unknown')
        df['job_role_encoded'], job_uniques = pd.factorize(df['job_role'])    
    # Save cleaned dataset
    df.to_csv(out_path, index=False)
    return df
if __name__ == '__main__':
    cleaned_df = clean_employee_dataset()
    # show a quick summary
    print("Cleaned dataset saved to employee_dataset_cleaned.csv")
    print(cleaned_df.head())
    print("\nDtypes:\n", cleaned_df.dtypes)