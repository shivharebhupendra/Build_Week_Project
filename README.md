# 💼 SAL_BW_Project – Job Descriptions Analysis

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
*File:* clean_job_descriptions.csv (https://drive.google.com/file/d/1KY-_3MoRYHhgqOorH-PcX4KVy3sciq0f/view?usp=sharing)

*Columns:*  
- Title: Job title  
- Company Name: Hiring company  
- Location: Job location  
- Salary: Average salary  
- Date Posted: Date the job was listed  

---

## ⚙ How to Run the Project

1. *Data Loading & Cleaning*  
   - Download job_descriptions_not_clean.csv from Kaggle (https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
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
📍 Count of Jobs per Location calculated and visualized job posting counts across locations to identify metro city dominance.

💰 Salary Distribution by Range categorized average salaries into defined brackets to understand the spread of compensation levels.

📦 Most Common Keywords in Job Titles extracted the top 10 recurring words in job titles to identify high-demand roles and skills.

🌆 Top 10 Locations for Jobs plotted the top cities by number of job postings, highlighting regional hiring trends.

🔑 Top Keywords in Job Titles (Bar Plot) visualized the frequency of popular keywords to emphasize recurring roles and industry trends.

📉 Salary Outliers Detected created a boxplot to identify outliers and understand salary variation among job listings.

🗓 Daily Job Posting Trends converted and grouped posting dates to reveal patterns in job posting frequency over time.

---

## 🔗 Project Repository  
> GitHub Repository : (https://github.com/Manishdebnath99/Build_Week_Project)

---
## 📁 Project Files
--------------------------------------------------------------------------------------------------------------
| File Name                                | Description                                                     |
|------------------------------------------|-----------------------------------------------------------------|
| 1 - Data Loading, Cleaning, and Representation.ipynb    | Load raw data, clean it, and save as CSV         |
| 2 - SQL_Connection.ipynb                                | Connect Jupyter to SQL and insert data           |
| 3 - SQL_Analysis.sql                                    | SQL queries for job data insights                |
| 4 - EDA Data Visualization.ipynb                        | Visualize trends with charts and plots           |
| clean_job_descriptions.csv                              | Cleaned dataset with key job info                |
| Build_Week_Presentation.pdf                             | Project summary and key insights (presentation)  |
| presentation_job_description_analysis.mp4               | Project presentation video                       |
| job_descriptions_not_clean                              | Data from Kaggle                                 |
--------------------------------------------------------------------------------------------------------------
---
## 👥 Contributors  
- Er. Manish Debnath  (https://github.com/Manishdebnath99)
- Er. Bhupendra Shivhare (https://github.com/shivharebhupendra)
- Er. Ashwin Kumar (https://github.com/Ashwin1238-stack)

