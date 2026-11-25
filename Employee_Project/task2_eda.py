import pandas as pd

# Load the cleaned dataset created in Task 1
df = pd.read_csv('clean_data.csv')

# 1. SUMMARY STATISTICS (Mean, Median, Min, Max, Std)

print("--- 1. SUMMARY STATISTICS ---")
summary_stats = df[['Age', 'Salary']].agg(['mean', 'median', 'min', 'max', 'std']).round(2)
print(summary_stats)

# 2. GROUPBY COMPARISON (Department & City)

print("\n--- 2. GROUPBY COMPARISON (BY DEPARTMENT) ---")
dept_comparison = df.groupby('Department').agg(
    Employee_Count=('Employee_ID', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Avg_Age=('Age', 'mean')
).round(2)
print(dept_comparison)

print("\n--- GROUPBY COMPARISON (BY CITY) ---")
city_comparison = df.groupby('City').agg(
    Employee_Count=('Employee_ID', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Max_Salary=('Salary', 'max')
).round(2)
print(city_comparison)

# 3. CORRELATIONS BETWEEN NUMERIC COLUMNS (Top 3 Relationships)

print("\n--- 3. CORRELATIONS (NUMERIC COLUMNS) ---")
# Create 'Tenure_Years' from Join_Date to have 3 numeric columns for correlation
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Tenure_Years'] = ((pd.Timestamp('2026-01-01') - df['Join_Date']).dt.days / 365.25).round(1)

corr_matrix = df[['Age', 'Salary', 'Tenure_Years']].corr().round(4)
print(corr_matrix)

# Extract and list the top 3 relationships
corr_pairs = corr_matrix.unstack().drop_duplicates()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]
top_3_corr = corr_pairs.reindex(corr_pairs.abs().sort_values(ascending=False).index).head(3)

print("\nTop 3 Relationships:")
for idx, val in top_3_corr.items():
    print(f"- {idx[0]} & {idx[1]}: {val}")

# 4. ANSWER AT LEAST 3 BUSINESS QUESTIONS WITH NUMBERS

print("\n--- 4. BUSINESS QUESTIONS & NUMERIC ANSWERS ---")

# Question 1
highest_dept = dept_comparison['Avg_Salary'].idxmax()
highest_dept_sal = dept_comparison['Avg_Salary'].max()
print(f"Q1. Which department has the highest average salary?\nAnswer: {highest_dept} (${highest_dept_sal:,.2f})")

# Question 2
city_payroll = df.groupby('City')['Salary'].sum()
top_city = city_payroll.idxmax()
top_city_cost = city_payroll.max()
print(f"\nQ2. Which city accounts for the highest total salary expenditure?\nAnswer: {top_city} (${top_city_cost:,.2f})")

# Question 3
overall_avg_sal = df['Salary'].mean()
above_avg_count = len(df[df['Salary'] > overall_avg_sal])
print(f"\nQ3. How many employees earn above the overall average salary (${overall_avg_sal:,.2f})?\nAnswer: {above_avg_count} employees")

# 5. MERGE A SECOND SMALL TABLE (Department Budget)
print("\n--- 5. MERGING DEPARTMENT BUDGET TABLE ---")
dept_budgets = pd.DataFrame({
    'Department': df['Department'].unique(),
    'Annual_Budget': [5000000 + (i * 1500000) for i in range(len(df['Department'].unique()))]
})

df_merged = pd.merge(df, dept_budgets, on='Department', how='left')
print(df_merged[['Employee_ID', 'Name', 'Department', 'Salary', 'Annual_Budget']].head())

# BONUS CHALLENGE: PIVOT TABLE (Two Categorical Columns)
print("\n--- BONUS CHALLENGE: PIVOT TABLE (DEPARTMENT vs CITY) ---")
pivot_table = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='City',
    aggfunc='mean',
    fill_value=0
).round(2)
print(pivot_table)