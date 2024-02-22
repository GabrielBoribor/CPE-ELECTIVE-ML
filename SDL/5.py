import tkinter as tk
from tkinter import messagebox

class PhoneDirectoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Phone Directory")
        self.master.geometry("300x150")

        # Set background color
        self.master.config(bg="#f0f0f0")

        # Create and place widgets
        self.label_name = tk.Label(master, text="Name:", bg="#f0f0f0")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(master, text="Phone Number:", bg="#f0f0f0")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add", command=self.add_entry, bg="#007bff", fg="white")
        self.add_button.grid(row=2, column=0, padx=50, pady=5)

        self.search_button = tk.Button(master, text="Search", command=self.search_entry, bg="#28a745", fg="white")
        self.search_button.grid(row=2, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="#dc3545", fg="white")
        self.quit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_entry(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()

        if name and phone:
            try:
                with open("phone_directory.txt", "a") as file:
                    file.write(f"{name},{phone}\n")
                messagebox.showinfo("Success", "Entry added successfully!")
                self.entry_name.delete(0, tk.END)
                self.entry_phone.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
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

def main():
    root = tk.Tk()
    app = PhoneDirectoryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
