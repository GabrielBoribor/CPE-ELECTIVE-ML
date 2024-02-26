import tkinter as tk
from tkinter import messagebox

def add_entry():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()

    if name and phone:
        if phone.isdigit():  # Check if phone number contains only digits
            if len(phone) == 11:
                if not phone_exists(phone):  # Check if phone number already exists
                    try:
                        with open("phone_directory.txt", "a") as file:
                            file.write(f"{name},{phone}\n")
                        messagebox.showinfo("Success", "Entry added successfully!")
                        clear_fields()
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {e}")
                else:
                    messagebox.showerror("Error", "Phone number already exists.")
            else:
                messagebox.showerror("Error", "Phone number must be exactly 11 digits.")
        else:
            messagebox.showerror("Error", "Phone number must contain only digits.")
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

def phone_exists(phone):
    try:
        with open("phone_directory.txt", "r") as file:
            for line in file:
                entry = line.strip().split(",")
                if len(entry) >= 2 and entry[1] == phone:
                    return True
    except FileNotFoundError:
        pass  # If file not found, entry does not exist
    return False

def search_entry():
    name = entry_name.get().strip()
    if not name:
        messagebox.showerror("Error", "Please enter a name to search.")
        return

    try:
        with open("phone_directory.txt", "r") as file:
            for line in file:
                entry = line.strip().split(",")
                if entry[0].lower() == name.lower():
                    messagebox.showinfo("Search Result", f"Phone number: {entry[1]}")
                    return
            messagebox.showinfo("Search Result", "Phone number not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Phone directory file not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def confirm_quit():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.quit()

def entry_exists(name):
    try:
        with open("phone_directory.txt", "r") as file:
            for line in file:
                entry = line.strip().split(",")
                if entry[0].lower() == name.lower():
                    return True
    except FileNotFoundError:
        pass  # If file not found, entry does not exist
    return False

root = tk.Tk()
root.title("Phone Directory")
root.config(bg="black")  # Background color
root.geometry("500x300")  # Larger window size

custom_font = ('Arial', 12)  # Larger font size

label_name = tk.Label(root, text="Name:", bg="black", fg="yellow", font=custom_font)
label_name.pack(side=tk.TOP, padx=10, pady=10)
entry_name = tk.Entry(root, font=custom_font)
entry_name.pack(side=tk.TOP, padx=10, pady=10)

label_phone = tk.Label(root, text="Phone Number:", bg="black", fg="yellow", font=custom_font)
label_phone.pack(side=tk.TOP, padx=10, pady=10)
entry_phone = tk.Entry(root, font=custom_font)
entry_phone.pack(side=tk.TOP, padx=10, pady=10)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(side=tk.TOP, padx=10, pady=10)

add_button = tk.Button(button_frame, text="Add", command=add_entry, bg="#007bff", fg="white", font=custom_font)
add_button.pack(side=tk.LEFT, padx=10, pady=10)

search_button = tk.Button(button_frame, text="Search", command=search_entry, bg="#28a745", fg="white", font=custom_font)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, bg="#6c757d", fg="white", font=custom_font)
clear_button.pack(side=tk.LEFT, padx=10, pady=10)

quit_button = tk.Button(button_frame, text="Quit", command=confirm_quit, bg="#dc3545", fg="white", font=custom_font)
quit_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
