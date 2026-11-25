import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# TASK 1: DATA CLEANING
# ==========================================================

# 1. Load the dataset and capture "Before" metrics
df = pd.read_csv('employee_dirty_data.csv')

before_rows = len(df)
before_missing = df.isnull().sum().sum()
before_duplicates = df.duplicated().sum()

print("--- 1. INITIAL DATA OVERVIEW ---")
print(df.info())

# 2. Remove exact duplicates first (1480 -> 1470 rows)
df = df.drop_duplicates()

# 3. Fix Data Types and Standardize Text
# Clean 'Salary': remove '$' and ',' symbols and convert from text to float
df['Salary'] = df['Salary'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Convert 'Join_Date' with mixed formats into standard datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'], format='mixed', dayfirst=True, errors='coerce')

# Standardize text columns: trim extra spaces and apply Title Case
df['Name'] = df['Name'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

# 4. Handle Missing Values (with clear reasons)
# Numeric columns: Fill with Median (robust against outliers)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Categorical columns: Fill with Mode (most frequent category)
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])

# 5. Detect and Handle Outliers using the IQR Rule
def cap_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    print(f"Outliers detected in {series.name}: {len(outliers)}")
    # Cap outliers at upper/lower bounds so row count stays 1470
    return series.clip(lower=lower_bound, upper=upper_bound)

print("\n--- 2. OUTLIER DETECTION ---")
df['Age'] = cap_outliers_iqr(df['Age'])
df['Salary'] = cap_outliers_iqr(df['Salary'])

# 6. Create Before / After Summary Table & Save Clean CSV
after_rows = len(df)
after_missing = df.isnull().sum().sum()
after_duplicates = df.duplicated().sum()

summary_table = pd.DataFrame({
    'Metric': ['Rows', 'Missing Values', 'Duplicates'],
    'Before': [before_rows, before_missing, before_duplicates],
    'After': [after_rows, after_missing, after_duplicates]
})

print("\n--- 3. BEFORE / AFTER SUMMARY TABLE ---")
print(summary_table.to_string(index=False))

# Export cleaned data
df.to_csv('clean_data.csv', index=False)
print("\nSuccess: 'clean_data.csv' has been saved!")

# ==========================================================
# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================

print("\n--- 4. SUMMARY STATISTICS ---")
print(df.describe())

print("\n--- 5. AVERAGE SALARY BY DEPARTMENT ---")
print(df.groupby('Department')['Salary'].mean().round(2))

# Visualize distributions using Box Plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(y=df['Salary'], ax=axes[0], color='skyblue')
axes[0].set_title('Salary Distribution (Cleaned)')

sns.boxplot(y=df['Age'], ax=axes[1], color='lightgreen')
axes[1].set_title('Age Distribution (Cleaned)')

plt.tight_layout()
plt.show()