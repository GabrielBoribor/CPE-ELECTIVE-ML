import tkinter as tk
import random

def randomQ():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

def checkIftama():
    global score
    user_answer = int(entry.get())
    if user_answer == correct_answer:
        result_label.config(text="You are correct!")
        score += 5
        score_label.config(text="Your score: " + str(score))
        askQ()
    else:
        result_label.config(text="Incorrect. Please try again.")
        score -= 5
        if score < 0:
            result_label.config(text="Game over! You have run out of points.")
            entry.config(state=tk.DISABLED)
            check_button.config(state=tk.DISABLED)
            try_again_button.config(state=tk.DISABLED)
        else:
            score_label.config(text="Your score: " + str(score))
            entry.delete(0, tk.END)

def askQ():
    global correct_answer
    num1, num2 =randomQ()
    correct_answer = num1 * num2
    question_label.config(text="How much is " + str(num1) + " times " + str(num2) + "?")
    entry.delete(0, tk.END)
    entry.focus()

def try_again():
    global score
    score = 0
    score_label.config(text="Your score: " + str(score))
    entry.delete(0, tk.END)
    askQ()


# GUIco
root = tk.Tk()
root.title("Multiplication Game")


question_label = tk.Label(root, text="")
question_label.pack(pady=(20))

entry = tk.Entry(root)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

check_button = tk.Button(button_frame, text="Check", command=checkIftama)
check_button.pack(side=tk.LEFT, padx=5)

try_again_button = tk.Button(button_frame, text="Try Again", command=try_again)
try_again_button.pack(side=tk.RIGHT, padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score = 0
score_label = tk.Label(root, text="Your score: " + str(score))
score_label.pack()

askQ()

root.mainloop()
