import tkinter as tk
from tkinter import messagebox

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management")


        self.inventory = {
            'motherboards': 0,
            'hard_disk': 0,
            'diskette': 0,
            'compact_disk': 0,
            'memory_cards': 0
        }


        self.label = tk.Label(master, text="Inventory Management")
        self.label.pack()


        self.display_button = tk.Button(master, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack()


        self.add_frame = tk.Frame(master)
        self.add_frame.pack()


        self.add_label = tk.Label(self.add_frame, text="Add Items:")
        self.add_label.grid(row=0, column=0)
        self.add_item_label = tk.Label(self.add_frame, text="Item:")
        self.add_item_label.grid(row=1, column=0)
        self.add_item_entry = tk.Entry(self.add_frame)
        self.add_item_entry.grid(row=1, column=1)


        self.add_quantity_label = tk.Label(self.add_frame, text="Quantity:")
        self.add_quantity_label.grid(row=2, column=0)
        self.add_quantity_entry = tk.Entry(self.add_frame)
        self.add_quantity_entry.grid(row=2, column=1)


        self.add_button = tk.Button(self.add_frame, text="Add", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2)


        self.remove_frame = tk.Frame(master)
        self.remove_frame.pack()


        self.remove_label = tk.Label(self.remove_frame, text="Remove Items:")
        self.remove_label.grid(row=0, column=0)
        self.remove_item_label = tk.Label(self.remove_frame, text="Item:")
        self.remove_item_label.grid(row=1, column=0)
        self.remove_item_entry = tk.Entry(self.remove_frame)
        self.remove_item_entry.grid(row=1, column=1)


        self.remove_quantity_label = tk.Label(self.remove_frame, text="Quantity:")
        self.remove_quantity_label.grid(row=2, column=0)
        self.remove_quantity_entry = tk.Entry(self.remove_frame)
        self.remove_quantity_entry.grid(row=2, column=1)


        self.remove_button = tk.Button(self.remove_frame, text="Remove", command=self.remove_item)
        self.remove_button.grid(row=3, column=0, columnspan=2)


        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()


    def display_inventory(self):
        inventory_str = "Current Inventory:\n"
        for item, quantity in self.inventory.items():
            inventory_str += f"{item}: {quantity}\n"
        messagebox.showinfo("Inventory", inventory_str)


    def add_item(self):
        item = self.add_item_entry.get().lower()
        quantity = int(self.add_quantity_entry.get())
        if item in self.inventory:
            self.inventory[item] += quantity
            messagebox.showinfo("Success", f"Added {quantity} {item} to inventory.")
        else:
            messagebox.showerror("Error", "Invalid item.")


    def remove_item(self):
        item = self.remove_item_entry.get().lower()
        quantity = int(self.remove_quantity_entry.get())
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                messagebox.showinfo()
                messagebox.showerror("Error", f"Not enough {item} in inventory.")
        else:
            messagebox.showerror("Error", "Invalid item.")


def main():
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
