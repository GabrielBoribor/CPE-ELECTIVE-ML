import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        # Styling
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#b5e7a0')
        self.style.configure('TLabel', background='#e1d8b9')
        self.style.configure('Header.TLabel', font=('ROG Fonts', 35, 'bold'))

        self.item_names = ["Motherboard", "Hard Disk", "Diskette", "Compact Disk", "Memory Cards"]
        self.items = [f"{i+1}. {name}" for i, name in enumerate(self.item_names)]
        self.inventory = {item: 0 for item in self.items}

        # Load inventory from file
        self.load_items_from_file()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        header_label = ttk.Label(main_frame, text="Inventory Management", style='Header.TLabel')
        header_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.inventory_text = tk.Text(main_frame, height=10, width=40)
        self.inventory_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.update_inventory_text()

        self.style.configure('Large.TButton', font=('ROG Fonts', 16))
        add_button = ttk.Button(main_frame, text="Add Items", command=self.add_items, style='Large.TButton')
        add_button.grid(row=2, column=0, padx=5, pady=5)

        self.style.configure('gg.TButton', font=('ROG Fonts', 16))
        remove_button = ttk.Button(main_frame, text="Remove Items", command=self.remove_items, style='gg.TButton')
        remove_button.grid(row=2, column=1, padx=5, pady=5)

        self.style.configure('Custom.TButton', font=('ROG Fonts', 16))
        save_button = ttk.Button(main_frame, text="Save Inventory", command=self.save_items_to_file, style='Custom.TButton')
        save_button.grid(row=2, column=2, padx=20, pady=10)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure((0, 1, 2), weight=1)

    def update_inventory_text(self):
        self.inventory_text.delete(1.0, tk.END)
        for item, quantity in self.inventory.items():
            self.inventory_text.insert(tk.END, f"{item}: {quantity}\n")

        self.inventory_text.config(font=('ROG Fonts', 16))

    def add_items(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Items")
        add_window.transient(self.root)

        item_label = ttk.Label(add_window, text="Enter the number of the item to add:", state='readonly')
        item_label.grid(row=0, column=0, padx=10, pady=5)

        item_entry = ttk.Entry(add_window)
        item_entry.grid(row=0, column=1, padx=10, pady=5)
        item_entry.focus_set()

        def deselect_text(event):
            item_entry.selection_clear()

        item_entry.bind("<FocusIn>", deselect_text)

        quantity_label = ttk.Label(add_window, text="Enter quantity to add:", state='readonly')
        quantity_label.grid(row=1, column=0, padx=10, pady=5)

        quantity_entry = ttk.Entry(add_window)
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_item():
            choice = item_entry.get()
            if choice.isdigit():
                choice = int(choice)
                if 0 < choice <= len(self.item_names):
                    item = self.item_names[choice - 1]
                    quantity = int(quantity_entry.get())
                    if quantity:
                        self.inventory[f"{choice}. {item}"] += quantity
                        self.update_inventory_text()
                        add_window.destroy()
                    else:
                        messagebox.showerror("Error", "Quantity should be a positive integer.")
                else:
                    messagebox.showerror("Error", "Invalid item number.")
            else:
                messagebox.showerror("Error", "Please enter a valid number for the item.")

        add_button = ttk.Button(add_window, text="Add", command=add_item)
        add_button.grid(row=2, columnspan=2, padx=10, pady=10)

        cancel_button = ttk.Button(add_window, text="Cancel", command=add_window.destroy)
        cancel_button.grid(row=2, column=1, padx=10, pady=10)

    def remove_items(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Items")
        remove_window.transient(self.root)

        item_label = ttk.Label(remove_window, text="Enter the number of the item to remove:", state='readonly')
        item_label.grid(row=0, column=0, padx=10, pady=5)

        item_entry = ttk.Entry(remove_window)
        item_entry.grid(row=0, column=1, padx=10, pady=5)
        item_entry.focus_set()

        def deselect_text(event):
            item_entry.selection_clear()

        item_entry.bind("<FocusIn>", deselect_text)

        quantity_label = ttk.Label(remove_window, text="Enter quantity to remove:", state='readonly')
        quantity_label.grid(row=1, column=0, padx=10, pady=5)

        quantity_entry = ttk.Entry(remove_window)
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        def remove_item():
            choice = item_entry.get()
            if choice.isdigit():
                choice = int(choice)
                if 0 < choice <= len(self.item_names):
                    item = self.item_names[choice - 1]
                    quantity = int(quantity_entry.get())
                    if quantity:
                        inventory_key = f"{choice}. {item}"
                        if inventory_key in self.inventory:
                            if self.inventory[inventory_key] >= quantity:
                                self.inventory[inventory_key] -= quantity
                                self.update_inventory_text()
                                remove_window.destroy()
                            else:
                                messagebox.showerror("Error", "Insufficient quantity in inventory.")
                        else:
                            messagebox.showerror("Error", "Invalid item.")
                    else:
                        messagebox.showerror("Error", "Quantity should be a positive integer.")
                else:
                    messagebox.showerror("Error", "Invalid item number.")
            else:
                messagebox.showerror("Error", "Please enter a valid number for the item.")

        remove_button = ttk.Button(remove_window, text="Remove", command=remove_item)
        remove_button.grid(row=2, columnspan=2, padx=10, pady=10)

        cancel_button = ttk.Button(remove_window, text="Cancel", command=remove_window.destroy)
        cancel_button.grid(row=2, column=1, padx=10, pady=10)

    def save_items_to_file(self):
        with open("inventory.txt", "w") as file:
            for item, quantity in self.inventory.items():
                file.write(f"{item}: {quantity}\n")
        messagebox.showinfo("Success", "Inventory saved to file.")

    def load_items_from_file(self):
        try:
            with open("inventory.txt", "r") as file:
                for line in file:
                    item, quantity = line.strip().split(": ")
                    self.inventory[item] = int(quantity)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Inventory file not found. Starting with empty inventory.")

def main():
    root = tk.Tk()
    root.geometry("900x600")
    app = InventoryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
