import tkinter as tk
from tkinter import messagebox

class PhoneDirectoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Phone Directory")
        self.master.geometry("400x200")  # Change width and height as needed
        self.master.config(bg="#f0f0f0")

        # Define font style and size
        self.custom_font = ('Helvetica', 10, 'bold')  # Change the font family, size, and style as needed

        self.create_widgets()

    def create_widgets(self):
        # Use custom font for labels, entries, and buttons
        self.label_name = tk.Label(self.master, text="Name:", bg="#f0f0f0", font=self.custom_font)
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(self.master, font=self.custom_font)
        self.entry_name.grid(row=0, column=1, padx=15, pady=15)

        self.label_phone = tk.Label(self.master, text="Phone Number:", bg="#f0f0f0", font=self.custom_font)
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_phone = tk.Entry(self.master, font=self.custom_font)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.master, text="Add", command=self.add_entry, bg="#007bff", fg="white", font=self.custom_font)
        self.add_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.search_button = tk.Button(self.master, text="Search", command=self.search_entry, bg="#28a745", fg="white", font=self.custom_font)
        self.search_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_fields, bg="#6c757d", fg="white", font=self.custom_font)
        self.clear_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.quit_button = tk.Button(self.master, text="Quit", command=self.confirm_quit, bg="#dc3545", fg="white", font=self.custom_font)
        self.quit_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

    def add_entry(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()

        if name and phone:
            if len(phone) == 11 and phone.isdigit():
                try:
                    with open("phone_directory.txt", "a") as file:
                        file.write(f"{name},{phone}\n")
                    messagebox.showinfo("Success", "Entry added successfully!")
                    self.clear_fields()
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")
            else:
                messagebox.showerror("Error", "Phone number must be exactly 11 digits.")
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def search_entry(self):
        name = self.entry_name.get().strip()
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

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

    def confirm_quit(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.master.quit()

def main():
    root = tk.Tk()
    app = PhoneDirectoryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
