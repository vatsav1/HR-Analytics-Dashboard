# HR-Analytics-Dashboard
This project examines attrition, salary distribution, and performance metrics using MySQL and Python visualization tools (Seaborn, Matplotlib). Includes database normalization and queries for efficient HR decision-making.

FINAL PROJECT
Team
Srivatsav Yallapragada
Mohit Kale
Geeta Sai Sneha Bankuru
Deepak Vital Patil


Dataset considered:
HR_Analytics | HR Analytics Dataset
The HR Analytics dataset provides comprehensive insights into employee attributes and organizational dynamics, enabling data-driven decisions to enhance employee satisfaction, retention, and performance.

Attributes in the dataset :
1.	EmpID: A unique identifier assigned to each employee.
2.	Age: Age of the employee (numerical value).
3.	AgeGroup: Categorized representation of employee age (e.g., 20–30, 31–40).
4.	Attrition: Indicates whether an employee has left the organization (Yes/No).
5.	BusinessTravel: Frequency of business travel (e.g., Rarely, Frequently).
6.	DailyRate: Daily rate of payment for an employee in numerical terms.
7.	Department: Department where the employee is assigned (e.g., HR, Sales, R&D).
8.	DistanceFromHome: Distance between the employee’s home and workplace (in kilometers/miles).
9.	EmployeeCount: Total number of employees in the dataset (constant).
10.	EmployeeNumber: Another identifier for employees (numerical).
11.	EnvironmentSatisfaction: Employee's satisfaction with the work environment (scale: 1–4).
12.	Gender: Employee's gender (Male/Female).
13.	HourlyRate: Hourly rate of pay for an employee.
14.	JobInvolvement: Level of involvement in the job (scale: 1–4).
15.	JobLevel: Hierarchical level of the job (e.g., 1–5).
16.	JobRole: The specific role of the employee in the organization (e.g., Manager, Technician).
17.	JobSatisfaction: Satisfaction level regarding the job role (scale: 1–4).
18.	MaritalStatus: Employee's marital status (e.g., Single, Married, Divorced).
19.	MonthlyIncome: Monthly earnings of the employee.
20.	SalarySlab: Categorization of monthly income into slabs.
21.	MonthlyRate: Monthly rate of pay.
22.	NumCompaniesWorked: Total number of companies the employee has worked for.
23.	Over18: Indicates if the employee is over 18 years old (constant, typically Yes).
24.	OverTime: Indicates whether the employee works overtime (Yes/No).
25.	PercentSalaryHike: Percentage increase in salary during appraisals.
26.	PerformanceRating: Performance evaluation rating (scale: 1–4).
27.	RelationshipSatisfaction: Satisfaction with relationships at work (scale: 1–4).
28.	StandardHours: Standard number of working hours per week (constant, typically 40).
29.	StockOptionLevel: Level of stock options assigned to the employee (scale: 0–3).
30.	TotalWorkingYears: Total years of professional experience.
31.	TrainingTimesLastYear: Number of training sessions attended in the previous year.
32.	WorkLifeBalance: Level of balance between work and personal life (scale: 1–4).
33.	YearsAtCompany: Total years the employee has been with the current organization.
34.	YearsInCurrentRole: Years spent in the current job role.
35.	YearsSinceLastPromotion: Years since the last promotion was received.
36.	YearsWithCurrManager: Years spent working under the current manager.
Normalization
1NF (First Normal Form)
Goal: Ensure that all columns contain atomic values (indivisible data) and no repeating groups exist.
1.	Employee Table:
o	Attributes like Age, Gender, and MaritalStatus are already atomic.
o	Ensured there are no repeating groups (e.g., multiple departments or job roles for a single employee).
2.	Department Table:
o	Extracted unique Department names to ensure no repetition in the original table.
3.	JobRole Table:
o	Ensured that JobRole is stored as a unique entity to prevent redundancy.
4.	EmployeePerformance Table:
o	Split attributes such as PerformanceRating, EnvironmentSatisfaction, and JobSatisfaction into separate rows for each employee, ensuring atomicity.
5.	EmployeeSalary Table:
o	Made sure salary components (MonthlyIncome, DailyRate, etc.) are atomic and stored distinctly.
6.	Attrition Table:
o	Ensured every employee has a single value for AttritionStatus, avoiding multi-valued attributes.
7.	Experience Table:
o	Split experience metrics (YearsAtCompany, YearsInCurrentRole, etc.) into atomic attributes.
8.	BusinessTravel Table:
o	Created unique rows for BusinessTravelType for each employee, eliminating redundancy.
________________________________________
2NF (Second Normal Form)
Goal: Ensure all non-prime attributes are fully dependent on the whole primary key (eliminate partial dependency).
1.	Employee Table:
o	Removed attributes such as Department and JobRole (partial dependency) and replaced them with foreign keys (DepartmentID and JobRoleID).
2.	Department Table:
o	Created a standalone table for DepartmentID and DepartmentName, ensuring DepartmentName depends only on DepartmentID.
3.	JobRole Table:
o	Moved JobRole into a separate table with JobRoleID as the primary key to avoid partial dependency on EmpID.
4.	EmployeePerformance Table:
o	Detached performance metrics (e.g., EnvironmentSatisfaction, JobSatisfaction) into a separate table fully dependent on EmpID.
5.	EmployeeSalary Table:
o	Moved salary attributes (e.g., MonthlyIncome, DailyRate) into a separate table tied directly to EmpID.
6.	Attrition Table:
o	Created a distinct table for attrition status, ensuring it directly depends on EmpID.
7.	Experience Table:
o	Extracted experience-related attributes into a new table linked to EmpID, removing redundancy.
8.	BusinessTravel Table:
o	Moved BusinessTravelType to a standalone table, ensuring no attribute is partially dependent on EmpID.

________________________________________
3NF (Third Normal Form)
Goal: Remove transitive dependencies (non-prime attributes should depend only on the primary key).
1.	Employee Table:
o	Ensured all remaining attributes (e.g., Age, Gender) are directly dependent on EmpID.
o	Removed transitive dependencies (e.g., DepartmentName was moved to the Department table).
2.	Department Table:
o	DepartmentName depends only on DepartmentID.
3.	JobRole Table:
o	JobRoleName depends only on JobRoleID.
4.	EmployeePerformance Table:
o	Introduced PerformanceID as the primary key to handle multiple performance reviews per employee.
5.	EmployeeSalary Table:
o	Introduced SalaryID as the primary key to separate salary records uniquely.
6.	Attrition Table:
o	Added AttritionID as the primary key to uniquely identify attrition records.
7.	Experience Table:
o	Introduced ExperienceID as the primary key to uniquely identify each employee’s experience data.
8.	BusinessTravel Table:
o	Introduced TravelID as the primary key to uniquely identify each business travel record.
Entity-Relationship Diagram for the database:

 

This diagram illustrates a normalized relational database schema for an HR Analytics system with the following key highlights:
1.	Normalization and Data Consistency: The database adheres to Third Normal Form (3NF), ensuring data is atomic, redundancy is minimized, and referential integrity is maintained. Core entities such as Employee, Job Role, Department, Employee Performance, Experience, Employee Salary, Attrition, and Business Travel are organized into separate tables, with clear distinctions and minimal data duplication.

2.	Structured Relationships: Logical relationships between tables are established through primary and foreign key constraints, with EmpID serving as the central attribute linking related data. This structure enhances data accuracy, supports efficient querying, and ensures scalability for future enhancements.


Creation of Database in MySQL workbench:

CREATE DATABASE `empolyeemanagement
USE empolyeemanagement;
•	It creates a new database named employeemanagement and sets it as the active workspace, enabling structured storage and management of employee-related data.

-- Create tables
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    Department VARCHAR(255)
);
•	It creates the Department table to store unique department IDs and names, ensuring organized department categorization.

CREATE TABLE JobRole (
    JobRoleID INT PRIMARY KEY,
    JobRole VARCHAR(255)
);
•	It creates the JobRole table to store unique job role IDs and their corresponding names, ensuring proper categorization of job roles.

CREATE TABLE Employee (
    EmpID VARCHAR(255) PRIMARY KEY,
    Age INT,
    Gender VARCHAR(50),
    MaritalStatus VARCHAR(50),
    DepartmentID INT,
    JobRoleID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID),
    FOREIGN KEY (JobRoleID) REFERENCES JobRole(JobRoleID)
);
•	It creates the Employee table, storing employee details such as ID, age, gender, marital status, and linking DepartmentID and JobRoleID as foreign keys to ensure relational integrity with the Department and JobRole tables.

CREATE TABLE Attrition (
    AttritionID INT PRIMARY KEY,
    EmpID VARCHAR(255),
    Attrition VARCHAR(50),
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);
•	It creates the Attrition table to track employee attrition status, linking EmpID as a foreign key to the Employee table.

CREATE TABLE BusinessTravel (
    TravelID INT PRIMARY KEY,
    EmpID VARCHAR(255),
    BusinessTravel VARCHAR(255),
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);
•	It creates the BusinessTravel table to store employee travel information, linking EmpID as a foreign key to the Employee table.

CREATE TABLE EmployeePerformance (
    PerformanceID INT PRIMARY KEY,
    EmpID VARCHAR(255),
    PerformanceRating INT,
    EnvironmentSatisfaction INT,
    JobInvolvement INT,
    JobSatisfaction INT,
    RelationshipSatisfaction INT,
    WorkLifeBalance INT,
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);
•	It creates the EmployeePerformance table to store performance-related metrics, linking EmpID as a foreign key to the Employee table.


CREATE TABLE EmployeeSalary (
    SalaryID INT PRIMARY KEY,
    EmpID VARCHAR(255),
    MonthlyIncome DECIMAL(10, 2),
    DailyRate DECIMAL(10, 2),
    HourlyRate DECIMAL(10, 2),
    MonthlyRate DECIMAL(10, 2),
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);
•	It creates the EmployeeSalary table to store salary-related details, linking EmpID as a foreign key to the Employee table.

CREATE TABLE Experience (
    ExperienceID INT PRIMARY KEY,
    EmpID VARCHAR(255),
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager DECIMAL(10, 2),
    TotalWorkingYears INT,
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);
•	It creates the Experience table to store employee experience data, linking EmpID as a foreign key to the Employee table, ensuring proper tracking of work history and career progression.


LOAD DATA INFILE 'C/Documents/Department.csv'
INTO TABLE Department
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Department, DepartmentID);
•	It loads data from the Department.csv file into the Department table, specifying field delimiters, text qualifiers, and line terminators, while ignoring the first row (headers) to ensure proper import of department information.

















Schema after creation of Database:
 

•	empolyeemanagement database schema, showcasing the organized structure with tables such as employee, attrition, department, and employeeperformance, along with associated views, stored procedures, and functions for efficient data management and retrieval.








Database to Python connection:

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

•	Establishes a connection between Python and the empolyeemanagement MySQL database using the mysql.connector library, enabling seamless data retrieval and analysis.

Collection of data for the analysis:
1.	Attrition Analysis
Data Collection Query:
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

•	It retrieves the total number of employees and their attrition status for each department by joining the employee, department, and attrition tables, grouped by department and attrition status.



Analysis:
plt.figure(figsize=(10, 6))
sns.barplot(data=attrition_df, x='Department', y='TotalEmployees', hue='Attrition')
plt.title('Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()



 

•	Research & Development has the highest number of employees experiencing attrition, although overall attrition numbers remain low across all departments.

2.	Salary Analysis
Data Collection Query:
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
•	It retrieves the Department, Job Role, and Monthly Income of employees by joining employee, department, job role, and salary tables for salary analysis.
Analysis:
P
lt.figure(figsize=(12, 6))
sns.boxplot(data=salary_df, x='Department', y='MonthlyIncome')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Monthly Income')
plt.xticks(rotation=45)
plt.show()


 

•	The salary distribution shows similar median incomes across departments, but Sales and Human Resources have a higher concentration of outliers at the upper end.











plt.figure(figsize=(12, 6))
sns.boxplot(data=salary_df, x='JobRole', y='MonthlyIncome')
plt.title('Salary Distribution by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Monthly Income')
plt.xticks(rotation=45)
plt.show()

 

•	The salary distribution by job role indicates that Managers and Research Directors earn the highest monthly incomes, while roles like Laboratory Technicians and Sales Representatives have significantly lower salaries with minimal variation.


3.	Performance Analysis
Data Collection Query:
SELECT 
    p.PerformanceRating, p.JobSatisfaction, p.WorkLifeBalance, d.Department
FROM 
    employeeperformance p
JOIN 
    employee e ON p.EmpID = e.EmpID
JOIN 
    department d ON e.DepartmentID = d.DepartmentID;

Analysis:
# Heatmap for correlations between performance metrics
plt.figure(figsize=(8, 6))
corr = performance_df[['PerformanceRating', 'JobSatisfaction', 'WorkLifeBalance']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Performance Metrics')
plt.show()
 

It reveals negligible correlations between Performance Rating, Job Satisfaction, and Work-Life Balance, indicating that these performance metrics are largely independent of each other.


# Boxplot for Job Satisfaction by Department
plt.figure(figsize=(10, 6))
sns.boxplot(data=performance_df, x='Department', y='JobSatisfaction')
plt.title('Job Satisfaction by Department')
plt.xlabel('Department')
plt.ylabel('Job Satisfaction')
plt.xticks(rotation=45)
plt.show()
 


•	Job satisfaction levels are consistent across all departments, with a median score of 3 and a similar range of variability, indicating no significant department-specific differences.

4.	Experience and Attrition Analysis
Data Collection Query:
SELECT 
    exp.YearsAtCompany, exp.YearsInCurrentRole, exp.TotalWorkingYears, a.Attrition
FROM 
    experience exp
JOIN 
    attrition a ON exp.EmpID = a.EmpID;

•	It retrieves employee experience metrics (Years at Company, Years in Current Role, Total Working Years) and Attrition status to analyze the relationship between experience and attrition trends.

Analysis:
plt.figure(figsize=(8, 6))
sns.boxplot(data=experience_df, x='Attrition', y='YearsAtCompany')
plt.title('Years at Company by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Years at Company')
plt.show()


 

•	Employees who left the company (Yes) tend to have fewer years at the company compared to those who stayed (No), indicating higher attrition among less tenured employees.

CONCLUSION 

The analysis of attrition trends highlights a clear correlation between employee tenure and attrition rates. Employees with shorter tenures are more prone to leaving, as reflected in the lower median values within the "Yes" group. This emphasizes the need for effective engagement and retention strategies during the early stages of employment to mitigate turnover. In contrast, longer-tenured employees demonstrate greater stability, underscoring the value of providing opportunities for long-term career growth and job satisfaction. Leveraging these insights enables organizations to develop targeted initiatives that enhance retention, particularly for newer employees, ultimately promoting workforce stability and overall productivity.



