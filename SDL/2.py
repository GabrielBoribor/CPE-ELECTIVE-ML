import tkinter as tk


def compute_Ave():
    students = []
    for i in range(len(student_entries)):
        name = student_entries[i].get()
        grades = [int(entry.get()) for entry in grade_entries[i]]
        students.append({"name": name, "grades": grades})

    num_quizzes = len(students[0]["grades"])
    quiz_totals = [0] * num_quizzes

    for student in students:
        total_grade = sum(student["grades"])
        student["average"] = total_grade / len(student["grades"])
        for i, grade in enumerate(student["grades"]):
            quiz_totals[i] += grade

    class_averages = [total / len(students) for total in quiz_totals]

    output_text.set("Individual Quiz Grades:\n")
    for i in range(num_quizzes):
        output_text.set(output_text.get() + f"Quiz {i + 1}: {[student['grades'][i] for student in students]}\n")
    output_text.set(output_text.get() + "\nStudent Averages:\n")
    for student in students:
        output_text.set(output_text.get() + f"{student['name']}: {student['average']:.2f}\n")
    output_text.set(output_text.get() + "\nClass Averages for Each Quiz:\n")
    for i, avg in enumerate(class_averages):
        output_text.set(output_text.get() + f"Quiz {i + 1}: {avg:.2f}\n")


# GUI setup
root = tk.Tk()
root.title("Class Grades Overview")

# Student entry
num_students = 3
student_entries = []
for i in range(num_students):
    label = tk.Label(root, text=f"Student {i + 1} Name:")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    student_entries.append(entry)

# Grade entry
grade_entries = []
for i in range(num_students):
    label = tk.Label(root, text=f"Student {i + 1} Grades (comma separated):")
    label.grid(row=i, column=2, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=5, pady=5)
    grade_entries.append(entry)

# Compute button
compute_button = tk.Button(root, text="Compute Averages", command=compute_Ave)
compute_button.grid(row=num_students, column=0, columnspan=4, padx=5, pady=10)

# Output text
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, justify="left")
output_label.grid(row=num_students + 1, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
