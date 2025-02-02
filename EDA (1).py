import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

# Database connection details
db_config = {
    'host': 'localhost',  # Change if not localhost
    'port': 3306,         # Default MySQL port
    'user': 'root',  # Replace with your username
    'password': 'Sri140299@',  # Replace with your password
    'database': 'empolyeemanagement'  # Replace with your database name
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
print("Connection successful!")
# Query data
query1 = "SELECT * FROM Employee;"

#Fecthing Data for Attrition analysis
attrition_query = """
SELECT 
    e.DepartmentID, d.Department, a.Attrition, COUNT(*) AS TotalEmployees
FROM 
    employee e
JOIN 
    department d ON e.DepartmentID = d.DepartmentID
JOIN 
    attrition a ON e.EmpID = a.EmpID
GROUP BY 
    e.DepartmentID, d.Department, a.Attrition;
"""
#Fecthing Data for Salary analysis
salary_query = """
SELECT 
    d.Department, j.JobRole, s.MonthlyIncome
FROM 
    employee e
JOIN 
    department d ON e.DepartmentID = d.DepartmentID
JOIN 
    jobrole j ON e.JobRoleID = j.JobRoleID
JOIN 
    employeesalary s ON e.EmpID = s.EmpID;
"""
#Fecthing Data for Perfomance analysis
performance_query = """
SELECT 
    p.PerformanceRating, p.JobSatisfaction, p.WorkLifeBalance, d.Department
FROM 
    employeeperformance p
JOIN 
    employee e ON p.EmpID = e.EmpID
JOIN 
    department d ON e.DepartmentID = d.DepartmentID;
"""
#Fecthing Data for Experince analysis
experience_query = """
SELECT 
    exp.YearsAtCompany, exp.YearsInCurrentRole, exp.TotalWorkingYears, a.Attrition
FROM 
    experience exp
JOIN 
    attrition a ON exp.EmpID = a.EmpID;
"""

df_employee = pd.read_sql(query1, conn)
attrition_df = pd.read_sql(attrition_query, conn)
salary_df = pd.read_sql(salary_query, conn)
performance_df = pd.read_sql(performance_query, conn)
experience_df = pd.read_sql(experience_query, conn)


#print(df_employee.head())

#-------------------------------------------------1. Attrition Analysis-------------------------------------------------
print("1. Attrition Analysis")

plt.figure(figsize=(10, 6))
sns.barplot(data=attrition_df, x='Department', y='TotalEmployees', hue='Attrition')
plt.title('Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()

#-------------------------------------------------2. Salary Analysis-------------------------------------------------
print("2. Salary Analysis")

# Plot Salary Distribution by Department
plt.figure(figsize=(12, 6))
sns.boxplot(data=salary_df, x='Department', y='MonthlyIncome')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Monthly Income')
plt.xticks(rotation=45)
plt.show()

# Plot Salary Distribution by Job Role
plt.figure(figsize=(12, 6))
sns.boxplot(data=salary_df, x='JobRole', y='MonthlyIncome')
plt.title('Salary Distribution by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Monthly Income')
plt.xticks(rotation=45)
plt.show()

#-------------------------------------------------3. Performance Analysis-------------------------------------------------
print("3. Performance Analysis")

# Heatmap for correlations between performance metrics
plt.figure(figsize=(8, 6))
corr = performance_df[['PerformanceRating', 'JobSatisfaction', 'WorkLifeBalance']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Performance Metrics')
plt.show()

# Boxplot for Job Satisfaction by Department
plt.figure(figsize=(10, 6))
sns.boxplot(data=performance_df, x='Department', y='JobSatisfaction')
plt.title('Job Satisfaction by Department')
plt.xlabel('Department')
plt.ylabel('Job Satisfaction')
plt.xticks(rotation=45)
plt.show()

#-------------------------------------------------4. Experience and Attrition Analysis-------------------------------------------------
print("4. Experience and Attrition Analysis")

# Plot Years at Company vs Attrition
plt.figure(figsize=(8, 6))
sns.boxplot(data=experience_df, x='Attrition', y='YearsAtCompany')
plt.title('Years at Company by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Years at Company')
plt.show()
