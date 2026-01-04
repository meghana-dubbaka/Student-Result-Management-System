import sqlite3

# ---------------- DATABASE CONNECTION ----------------
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# ---------------- CREATE TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER CHECK(marks BETWEEN 0 AND 100),
    grade TEXT
)
""")
conn.commit()

# ---------------- GRADE LOGIC ----------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

# ---------------- ADD STUDENT ----------------
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ").strip()
        marks = int(input("Enter Marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks range")
            return

        grade = calculate_grade(marks)

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, marks, grade)
        )
        conn.commit()
        print("Student added successfully")

    except sqlite3.IntegrityError:
        print("Roll number already exists")
    except ValueError:
        print("Invalid input")

# ---------------- VIEW ALL STUDENTS ----------------
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No records found")
        return

    print("\nRoll\tName\tMarks\tGrade")
    print("-" * 30)
    for row in records:
        print(row[0], row[1], row[2], row[3], sep="\t")

# ---------------- SEARCH STUDENT ----------------
def search_student():
    roll = int(input("Enter Roll Number: "))
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()

    if student:
        print("\nRoll:", student[0])
        print("Name:", student[1])
        print("Marks:", student[2])
        print("Grade:", student[3])
    else:
        print("Student not found")

# ---------------- UPDATE MARKS ----------------
def update_marks():
    roll = int(input("Enter Roll Number: "))
    new_marks = int(input("Enter New Marks: "))

    grade = calculate_grade(new_marks)

    cursor.execute(
        "UPDATE students SET marks = ?, grade = ? WHERE roll_no = ?",
        (new_marks, grade, roll)
    )

    if cursor.rowcount == 0:
        print("Student not found")
    else:
        conn.commit()
        print("Marks updated successfully")

# ---------------- DELETE STUDENT ----------------
def delete_student():
    roll = int(input("Enter Roll Number: "))
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll,))

    if cursor.rowcount == 0:
        print("Student not found")
    else:
        conn.commit()
        print("Student deleted successfully")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                update_marks()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number")

    conn.close()

# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()
