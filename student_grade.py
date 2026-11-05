# Student Grade Management System

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student(students):
    name = input("Enter student name: ")

    subjects = ["Python", "Mathematics", "Database"]
    marks = []

    for subject in subjects:
        mark = float(input("Enter marks in " + subject + ": "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    students[name] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    print("Student record added successfully!")


def display_students(students):
    if not students:
        print("No student records available.")
        return

    for name, details in students.items():
        print("\nStudent Name:", name)
        print("Marks:", details["marks"])
        print("Total:", details["total"])
        print("Average:", round(details["average"], 2))
        print("Grade:", details["grade"])


def main():
    students = {}

    while True:
        print("\n===== STUDENT GRADE MANAGEMENT =====")
        print("1. Add Student")
        print("2. Display Student Records")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
