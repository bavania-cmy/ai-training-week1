import csv
from collections import defaultdict
import matplotlib.pyplot as plt

# Read data using built-in csv module (no pandas required)
ids = []
salaries = []
departments = []
dept_salaries = defaultdict(list)

with open('employees.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp_id = int(row['id'])
        dept = row['department']
        sal = float(row['salary'])
        
        ids.append(emp_id)
        departments.append(dept)
        salaries.append(sal)
        dept_salaries[dept].append(sal)

# ---------------------------------------------------------
# 1. Bar Chart: Average Salary per Department
# ---------------------------------------------------------
dept_names = list(dept_salaries.keys())
avg_salaries = [sum(sals) / len(sals) for sals in dept_salaries.values()]

plt.figure(figsize=(8, 5))
bars = plt.bar(dept_names, avg_salaries, color='skyblue', edgecolor='black')

plt.title('Average Salary per Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + (yval * 0.01), f'{yval:,.2f}', 
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('1_avg_salary_bar.png')
plt.close()

# ---------------------------------------------------------
# 2. Histogram: Distribution of Salaries (5 Bins)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(salaries, bins=5, color='lightgreen', edgecolor='black')

plt.title('Salary Distribution (5 Bins)')
plt.xlabel('Salary')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('2_salary_histogram.png')
plt.close()

# ---------------------------------------------------------
# 3. Scatter Plot: ID vs Salary Coloured by Department
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))

for dept in dept_names:
    dept_ids = [ids[i] for i in range(len(ids)) if departments[i] == dept]
    dept_sals = [salaries[i] for i in range(len(salaries)) if departments[i] == dept]
    plt.scatter(dept_ids, dept_sals, label=dept, alpha=0.8)

plt.title('Employee ID vs Salary by Department')
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.legend(title='Department')

plt.tight_layout()
plt.savefig('3_id_vs_salary_scatter.png')
plt.close()

# ---------------------------------------------------------
# 4. Line Chart: Monthly Sales (Jan to Jun)
# ---------------------------------------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='coral', linewidth=2, markersize=8)

plt.title('Monthly Sales (Jan to Jun)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('4_monthly_sales_line.png')
plt.close()

print("All 4 charts have been saved successfully!")