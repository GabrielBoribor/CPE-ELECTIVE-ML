import tkinter as tk
import random
import pygame
from PIL import ImageTk, Image

def randomQ():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

def checkIftama():
    global score
    user_answer = int(selected_numbers_label.cget("text"))
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
            disable_number_buttons()
            try_again_button.config(state=tk.NORMAL)
        else:
            score_label.config(text="Your score: " + str(score))
            clear_selected_numbers()

def askQ():
    global correct_answer
    num1, num2 = randomQ()
    correct_answer = num1 * num2
    question_label.config(text="How much is " + str(num1) + " times " + str(num2) + "?")
    clear_selected_numbers()

def try_again():
    global score
    if result_label.cget("text") == "Game over! You have run out of points.":
        askQ()
        enable_number_buttons()
        try_again_button.config(state=tk.DISABLED)
        result_label.config(text="", fg='yellow')
        score = 0
        score_label.config(text="Your score: " + str(score), fg='yellow')
    else:
        result_label.config(text="", fg='yellow')

def select_number(number):
    current_text = selected_numbers_label.cget("text")
    selected_numbers_label.config(text=current_text + str(number))

def clear_selected_numbers():
    selected_numbers_label.config(text="")

def disable_number_buttons():
    for button in number_buttons:
        button.config(state=tk.DISABLED)

def enable_number_buttons():
    for button in number_buttons:
        button.config(state=tk.NORMAL)


pygame.init()
pygame.mixer.music.load("HevAbi.mp3")
pygame.mixer.music.play(loops=-1)

# GUI
root = tk.Tk()
root.title("Multiplication Game")
root.geometry("900x521+370+250")
root.resizable(False, False)

# background image
bg_image = ImageTk.PhotoImage(Image.open("galbg.jpg"))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Font
font_style = ("Fixedsys", 20,)
input_style = ("Fixedsys", 70)
check_style = ("Fixedsys", 15)
button_style = ("Fixedsys", 40)

question_label = tk.Label(root, text="", font=font_style, bg='black', fg='yellow')
question_label.pack(pady=(20))

selected_numbers_label = tk.Label(root, text="", font=input_style, bg='black', fg='yellow')
selected_numbers_label.pack(pady=(20))

# Number buttons
button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=20)

number_buttons = []
for i in range(10):
    button = tk.Button(button_frame, text=str(i), command=lambda num=i: select_number(num), font=button_style,
                       bg='black', fg='yellow')
    number_buttons.append(button)
    button.pack(side=tk.LEFT)

button_frame_horizontal = tk.Frame(root, bg='black')
button_frame_horizontal.pack()

check_button = tk.Button(button_frame_horizontal, text="Check", command=checkIftama, font=check_style, bg='black',
                         fg='white')
check_button.pack(side=tk.LEFT)

try_again_button = tk.Button(button_frame_horizontal, text="Try Again", command=try_again, font=check_style,
                             state=tk.DISABLED, bg='black', fg='white')
try_again_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="", font=font_style, bg='black', fg='yellow')
result_label.pack(pady=10)

score = 0
score_label = tk.Label(root, text="Your score: " + str(score), font=font_style, bg='black', fg='yellow')
score_label.pack()

askQ()

root.mainloop()
