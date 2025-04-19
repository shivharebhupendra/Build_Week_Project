# 💼 SAL_BW_Project_1 – Job Descriptions Analysis

## 📌 Project Overview  
This project focuses on analyzing job description data to derive meaningful insights. It includes:
- Downloading the dataset from Kaggle  
- Cleaning and preprocessing the data  
- Loading the cleaned data into SQL  
- Performing SQL-based analysis  
- Conducting Exploratory Data Analysis (EDA) with visualizations  

---

## 🔄 Project Workflow

### 1. *Data Cleaning*  
- Cleaned the dataset using *Pandas*  
- Extracted relevant columns  
- Saved the cleaned data as clean_job_descriptions.csv  

### 2. *SQL Insights*  
- Loaded cleaned data into *SQL Workbench* using a connection setup  
- Executed queries to extract insights:  
  - Most common job titles  
  - Count of jobs per location  
  - Jobs with salary >10 LPA  
  - Frequently hiring companies  

### 3. *EDA & Visualization*  
Used Python libraries (e.g., Matplotlib, Seaborn, WordCloud) to explore and visualize:  
- Jobs by location  
- Salary ranges  
- Trends in job postings  
- Common keywords in job titles  

---

## 📁 Dataset  
*File:* clean_job_descriptions.csv  
*Columns:*  
- Title: Job title  
- Company Name: Hiring company  
- Location: Job location  
- Salary: Average salary  
- Date Posted: Date the job was listed  

---

## ⚙ How to Run the Project

1. *Data Loading & Cleaning*  
   - Download job_descriptions_not_clean.csv from Kaggle  
   - Load and clean data using Pandas  
   - Save cleaned file as clean_job_descriptions.csv  

2. *SQL Setup*  
   - Create a database and empty table in SQL Workbench  
   - Use 2 - SQL_Connection script to connect Jupyter to SQL  
   - Import cleaned data into SQL  

3. *SQL Analysis*  
   - Run 3 - SQL_Analysis notebook  
   - Perform queries to generate job market insights  

4. *EDA & Visualization*  
   - Run 4 - EDA Data Visualization notebook  
   - Generate visualizations:  
     - 📊 Bar chart: Top job locations  
     - ☁ Word cloud: Common keywords  
     - 📦 Box plot: Salary distribution  
     - 📈 Trend chart: Job postings over time  

---

## 🔍 Insights from Analysis  
- 👔 Most Common Job Titles
Identified the top 10 recurring job titles to understand what roles are in high demand.

- 📍 Count of Jobs per Location
Aggregated job postings by location. Metro cities usually lead the count.

- 💰 Jobs with Salaries Greater than ₹10 LPA
Filtered listings to show only high-paying jobs, helping to identify roles and companies offering premium compensation.

- 🏢 Most Frequently Hiring Companies
Ranked companies based on how often they post jobs, highlighting the most active recruiters in the market.

---

## 🔗 Project Repository  
> [GitHub Repository] (https://github.com/Manishdebnath99/Build_Week_Project)

---

## 👥 Contributors  
- [Er. Manish Debnath]  (https://github.com/Manishdebnath99)
- [Er. Bhupendra Shivhare] (https://github.com/shivharebhupendra)
- [Er. Ashwin Kumar] (https://github.com/Ashwin1238-stack)

