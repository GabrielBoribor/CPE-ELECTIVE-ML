import tkinter as tk

def is_valid_name(name):
    return name.isalpha()

def is_valid_grade(grade):
    try:
        grades = [int(g.strip()) for g in grade.split(",")]
        return all(0 <= g <= 100 for g in grades)
    except ValueError:
        return False

def compute_Ave():
    students = []
    for i in range(len(student_entries)):
        name = student_entries[i].get()
        if not is_valid_name(name):
            output_text.set("Error: Student name Invalid.")
            return
        grades_input = grade_entries[i].get()
        if not is_valid_grade(grades_input):
            output_text.set("Error: Invalid grade scores. Please enter scores separated by commas.")
            return
        grades = [int(grade) for grade in grades_input.split(",")]
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

root = tk.Tk()
root.title("Class Grades")
root.configure(bg='#F0F0F0')  # Set background color

entry_style = {"padx": 5, "pady": 5}
button_style = {"padx": 5, "pady": 5}

# Create a frame to contain all the widgets and center it vertically
content_frame = tk.Frame(root, bg='#F0F0F0')
content_frame.pack(expand=True, fill="both", pady=(50, 0))  # Use pady to add space at the top

num_students = 3
student_entries = []
for i in range(num_students):
    label = tk.Label(content_frame, text=f"Student {i + 1} Name:", bg='#F0F0F0')  # Set label background color
    label.grid(row=i, column=0, sticky="w", **entry_style)
    entry = tk.Entry(content_frame)
    entry.grid(row=i, column=1, **entry_style)
    student_entries.append(entry)

grade_entries = []
for i in range(num_students):
    label = tk.Label(content_frame, text=f"Student {i + 1} Quizzes Scores:", bg='#F0F0F0')  # Set label background color
    label.grid(row=i, column=2, sticky="w", **entry_style)
    entry = tk.Entry(content_frame)
    entry.grid(row=i, column=3, **entry_style)
    grade_entries.append(entry)

compute_button = tk.Button(content_frame, text="Compute Averages", command=compute_Ave, bg='#4CAF50', fg='white', **button_style)  # Set button colors
compute_button.grid(row=num_students, column=0, columnspan=4, pady=10)

output_text = tk.StringVar()
output_label = tk.Label(content_frame, textvariable=output_text, justify="left", font=("Arial", 10), bg='#F0F0F0')  # Set label background color
output_label.grid(row=num_students + 1, column=0, columnspan=4, **entry_style)

root.mainloop()
