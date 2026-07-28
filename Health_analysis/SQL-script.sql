--renaming COLUMN names
--ALTER TABLE ocd RENAME "y-bocs_score_(compulsions)" TO compulsion_score

--Questions

--1 Count of males and females with ocd and their average obsession score.
SELECT gender AS Gender,count(*) AS patient_count,round(avg(obsession_score ),2) AS Avg_Obsession_Score FROM ocd GROUP BY gender;

--2 Find count & avg obsession score by ethinicity
SELECT ethnicity AS Ethinicty,count(*) AS patient_count,round(avg(obsession_score ),2) AS Avg_Obsession_Score FROM ocd GROUP BY ethnicity;

--3 Find number of diagnosed month over month
SELECT diagnosis_month AS MONTH,count(*) AS Total_Patients 
FROM (SELECT *, (EXTRACT(MONTH FROM ocd_diagnosis_date::date)) AS Diagnosis_Month FROM ocd) GROUP BY diagnosis_month ORDER BY Month;

--4 What is the most common obsession type and it's corresponsing avg obsession score
SELECT obsession_type AS Obsession_Type , count(*) AS Total_patients,Round(Avg(obsession_score),2) AS Avg_Obsession_Score  
FROM ocd GROUP BY obsession_type ORDER BY total_patients DESC LIMIT 1;

--5 What is the most common Compulsion type and it's corresponsing avg obsession score
SELECT compulsion_type AS Compulsion_Type , count(*) AS Total_patients,Round(Avg(obsession_score),2) AS Avg_Obsession_Score  
FROM ocd GROUP BY compulsion_type ORDER BY total_patients DESC LIMIT 1;



