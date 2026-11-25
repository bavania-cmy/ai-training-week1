# Employee Data Cleaning & Exploratory Data Analysis (Part 1)

## 1. Project Overview
This project focuses on cleaning a raw, messy employee dataset (`employee_dirty_data.csv`) containing **1,480 records** across 7 attributes (`Employee_ID`, `Name`, `Age`, `Department`, `Salary`, `Join_Date`, and `City`) and performing initial Exploratory Data Analysis (EDA). The final cleaned dataset is exported as `clean_data.csv`.

---

## 2. Data Cleaning Decisions & Justification (Task 1)

### A. Duplicate Removal
* **Issue:** The raw dataset contained **10 exact duplicate rows**.
* **Action Taken:** Removed duplicate rows using `df.drop_duplicates()` before imputing missing values to prevent skewed statistical calculations (median/mode).
* **Result:** Row count reduced from **1,480 to 1,470**.

### B. Data Type Fixes & Text Standardization
* **`Salary`:** Stored as formatted text strings containing `$` and `,` symbols (e.g., `"$65,000"`). Stripped currency symbols/commas and converted the column to numeric (`float`).
* **`Join_Date`:** Contained mixed date formats (`YYYY-MM-DD` and `DD/MM/YYYY`). Standardized all entries to proper `datetime` objects using `pd.to_datetime(..., format='mixed')`.
* **`Name`, `Department`, `City`:** Contained leading/trailing whitespace and inconsistent capitalization (e.g., `"  sales  "`, `"SALES"`). Applied `.str.strip().str.title()` to standardize all text values.

### C. Handling Missing Values
The dataset contained **214 missing values** across four columns:
* **`Age` & `Salary` (Numeric Columns):** Filled missing entries with the **Median** of each column. *Reason:* The median is robust against extreme outliers present in raw salary and age records, preventing distortion of the distribution.
* **`Department` & `City` (Categorical Columns):** Filled missing entries with the **Mode** (most frequent category). *Reason:* Preserves all 1,470 employee records without dropping valuable data from other valid columns.

### D. Outlier Detection & Treatment
* **Method:** Detected extreme values in `Age` and `Salary` using the **Interquartile Range (IQR) Rule** ($Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$) and verified visually via Box Plots.
* **Action Taken:** Applied **Winsorization (Capping)** at the lower and upper IQR bounds rather than deleting rows. *Reason:* Retains all 1,470 employee records while eliminating the distorting effect of unrealistic data-entry typos (e.g., ages over 100 or extreme salary spikes).

---

## 3. Before & After Summary Table

| Metric | Before Cleaning | After Cleaning |
| :--- | :---: | :---: |
| **Total Rows** | 1,480 | 1,470 |
| **Missing Values** | 214 | 0 |
| **Duplicate Rows** | 10 | 0 |

---

## 4. Exploratory Data Analysis (Task 2)
* **Summary Statistics:** Calculated mean, median, standard deviation, min, and max values across numeric fields (`Age` and `Salary`) using `df.describe()`.
* **Departmental Breakdown:** Grouped cleaned data by `Department` to compare average employee compensation across teams.
* **Visual Verification:** Generated side-by-side Box Plots for `Salary` and `Age` to confirm that all extreme outliers were successfully handled.

---

## 5. How to Run the Project
1. Place `employee_dirty_data.csv` and `project.py` in the same project directory.
2. Install required dependencies:
   ```bash
   python -m pip install pandas numpy matplotlib seaborn
   ```
3. Execute the script:
   ```bash
   python project.py
   ```
4. View the summary table in the terminal and check the generated `clean_data.csv` output file.
