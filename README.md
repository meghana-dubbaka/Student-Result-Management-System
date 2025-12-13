#  Student Result Management System (SQL)

This project was built to understand how student academic data can be managed using SQL in a real-world scenario. It focuses on storing student details,marks, and generating results such as rankings and department-wise toppers.

---

## Project Overview
I created this project to practice SQL concepts like joins, foreign keys,window functions, and triggers using a practical example.Instead of simple queries, I wanted a project that shows how data is connected and how meaningful results can be generated from it.

---

## Database Design
The database is normalized and consists of the following entities:

- *Departments* – Stores department details
- *Students* – Stores student information
- *Subjects* – Stores subject details
- *Marks* – Junction table storing student marks per subject

Referential integrity enforced using foreign keys  
ER diagram designed using MySQL Workbench  

---

## ER Diagram
<img width="556" height="595" alt="ER_diagram_student_result_management_system" src="https://github.com/user-attachments/assets/1adb5b48-d35b-411c-81c5-c1f2d884c2df" />



---

## Key Features
- Normalized relational database (3NF)
- GPA and percentage calculation
- Grade assignment using CASE statements
- Overall ranking using window functions
- Department-wise toppers
- SQL Views for consolidated results
- Stored Procedures for automation
- Triggers for data validation

---

## Views & Reports
- *student_complete_output*
  - Consolidated student result view
  - Combines students, departments, subjects, and marks
  - Calculates total marks, GPA, and grades

---

##  Tools & Technologies
- MySQL
- MySQL Workbench
- SQL (DDL, DML, Joins, Subqueries, Window Functions)

---

## Files Included
- [student_result_management_system.sql](https://github.com/user-attachments/files/24140982/student_result_management_system.sql)– Database schema & logic
- <img width="556" height="595" alt="ER_diagram_student_result_management_system" src="https://github.com/user-attachments/assets/42ba703c-ed76-42f7-818c-964ad1afb3e4" /> – ER diagram

---

## What I Learned
- How to design an ER diagram and convert it into tables
- Writing complex JOIN queries
- Using RANK() for ranking logic
- Applying triggers to maintain data integrity
- Structuring a SQL project for GitHub

---

## Author
*Dubbaka Meghana*

