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

Referential integrity enforced using foreign keys.  
ER diagram designed using MySQL Workbench . 

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
## key SQL Queries

### Create Tables
<pre>
CREATE TABLE Students(
StudentID INT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Gender VARCHAR(10),
DeptID INT,
FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);
-- SUBJECTS
CREATE TABLE Subjects(
SubjectID INT PRIMARY KEY,
SubjectName VARCHAR(50),
MaxMarks int);
-- MARKS
CREATE TABLE Marks(
MarkID INT PRIMARY KEY,
StudentID INT,
SubjectID INT,
MarksObtained INT,
FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);</pre>  


---

## Full SQL Code

- [student_result_management_system.sql](https://github.com/user-attachments/files/24140982/student_result_management_system.sql)– Database schema & logic


---

## Project Structure
Student-Result-Management-System/
├── README.md
├── student_result_management_system.sql
├── ER_Diagram.png
└── outputs/
    ├── department_wise_toppers.png
    └── overall_ranking.png

---

## outputs/results
### department-wise toppers : 
<img width="481" height="135" alt="department_wise_toppers" src="https://github.com/user-attachments/assets/b2426ace-1030-4793-ad07-9e9e126c7744" />

### overall ranking :
<img width="406" height="168" alt="overall_ranking" src="https://github.com/user-attachments/assets/8ac05149-55f5-4828-b659-98dfb065206e" />

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

## What I Learned
- How to design an ER diagram and convert it into tables
- Writing complex JOIN queries
- Using RANK() for ranking logic
- Applying triggers to maintain data integrity
- Structuring a SQL project for GitHub

---

## Author
*Dubbaka Meghana*

