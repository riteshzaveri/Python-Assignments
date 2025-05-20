# Create the dictionary
student_marks = {
    "Alice": 85,
    "Mike": 92,
    "Nick": 78
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display marks, or show an error if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")