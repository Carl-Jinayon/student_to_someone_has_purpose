"""
Exercise 2 (zip with three lists):

Given three lists:
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [95, 87, 92]

Use zip to print each student's grade in their subject: "Alice scored 95 in Math".
"""

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [95, 87, 92]

for student, grade, subject in zip(students, grades, subjects):
    print(f"{student} scored {grade} in {subject}.")