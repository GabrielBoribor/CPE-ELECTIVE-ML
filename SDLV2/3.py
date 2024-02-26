import tkinter as tk

def encrypt_text():
    text = entry_text.get()
    encrypted_text = encrypt(text)
    result_label.config(text=encrypted_text)

def encrypt(text):
    encrypted_text = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Shift the character to the next character in the alphabet
            if char == 'z':
                encrypted_text += 'a'  # Wrap around for 'z'
            elif char == 'Z':
                encrypted_text += 'A'  # Wrap around for 'Z'
            else:
                encrypted_text += chr(ord(char) + 1)
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char
    return encrypted_text

root = tk.Tk()
root.title("Encryption")
root.geometry("900x450+370+250")
root.resizable(False, False)


root.configure(bg='black')

font_style = ("Fixedsys", 20)
button_style = ("Fixedsys", 40)
input_style = ("Fixedsys", 30)
button_style = ("Fixedsys", 10)
output_style = ("Fixedsys", 40)

label_text = tk.Label(root, text="Enter the text to encrypt:", font=font_style, bg='black', fg='yellow')
label_text.pack(pady=70)

entry_text = tk.Entry(root, width=30, font=input_style, bg='black', fg='green', justify='center')
entry_text.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text, font=button_style, bg='black', fg='white')
encrypt_button.pack(pady=20)

result_label = tk.Label(root, text="", font=output_style, bg='black', fg='green')
result_label.pack(pady=40)

root.mainloop()