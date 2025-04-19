-- Part 2: SQL Insights

create database buildweek;
use buildweek;

CREATE TABLE clean_job_descriptions (
    Title VARCHAR(400),
    Company VARCHAR(400),
    Location VARCHAR(400),
    `Average Salary` INT,
    `Date Posted` DATE
);

SELECT 
    *
FROM
    clean_job_descriptions;

-- Q1. Find the Most common job titles.
SELECT 
    Title, COUNT(*) AS Count
FROM
    clean_job_descriptions
GROUP BY Title
ORDER BY count DESC
LIMIT 10;

-- This identifies the top 10 most common job titles in the dataset. It groups by 'Title'
-- and sorts the results in descending order of count.

-- Q2. Find the Count of jobs per location.
SELECT 
    Location, COUNT(*) AS count
FROM
    clean_job_descriptions
GROUP BY Location
ORDER BY count DESC;

-- This gives the number of jobs exist in each location. It helps to understand the geographic
-- distribution of job opportunities.

-- Q3. List the Jobs with salaries greater than 10LPA.

SELECT 
    *
FROM
    clean_job_descriptions
WHERE
    (`Average Salary` * 12) > 1000000;
    
-- This filters all the job entries and showing the list where the annual salary exceeds 
-- Rs. 10 Lakhs. 

-- Q4. List Most frequently hiring companies.
SELECT 
    Company, COUNT(*) AS count
FROM
    clean_job_descriptions
GROUP BY Company
ORDER BY count DESC
LIMIT 10;

-- This identifies the top 10 companies posting the most job listings. It helps to highlight 
-- the most active employers in the dataset.
