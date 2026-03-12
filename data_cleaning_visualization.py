
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("raw_employee_data.csv")

print("Original Shape:", df.shape)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())
df["experience_years"] = df["experience_years"].fillna(df["experience_years"].median())

# 3. Remove outliers using IQR
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["salary"] >= Q1 - 1.5*IQR) & (df["salary"] <= Q3 + 1.5*IQR)]

print("Cleaned Shape:", df.shape)

# Save cleaned data
df.to_csv("cleaned_employee_data.csv", index=False)

# ---- Visualizations ----
sns.set()

# Salary distribution
plt.figure()
sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.savefig("salary_distribution.png")

# Department count
plt.figure()
sns.countplot(x="department", data=df)
plt.title("Employees per Department")
plt.savefig("department_count.png")

# Age vs Salary
plt.figure()
sns.scatterplot(x="age", y="salary", hue="department", data=df)
plt.title("Age vs Salary")
plt.savefig("age_salary_scatter.png")

print("Visualization files saved.")
