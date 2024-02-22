import tkinter as tk

def encrypt_text():
    text = entry_text.get()
    encrypted_text = encrypt(text)
    result_label.config(text="Encrypted text: " + encrypted_text)

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


label_text = tk.Label(root, text="Enter the text to encrypt:")
label_text.pack()

entry_text = tk.Entry(root, width=50)
entry_text.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
