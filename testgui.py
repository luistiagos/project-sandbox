import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, 'values')
    print("Selected Item:", values)

def on_search():
    search_text = search_entry.get().lower()
    for item in tree.get_children():
        values = tree.item(item, 'values')
        if search_text in values[0].lower():
            tree.selection_set(item)
            tree.focus(item)
        else:
            tree.selection_remove(item)

# Create the main window
root = tk.Tk()
root.title("Responsive List with Search Box")

# Create a search box
search_label = tk.Label(root, text="Search:")
search_label.grid(row=0, column=0, pady=5)

search_entry = tk.Entry(root)
search_entry.grid(row=0, column=1, pady=5, padx=(0, 10), sticky='ew')

search_button = tk.Button(root, text="Search", command=on_search)
search_button.grid(row=0, column=2, pady=5)

# Create a Treeview widget with two columns
tree = ttk.Treeview(root, columns=('Column 1', 'Column 2'), show='headings')

# Set column headings
tree.heading('Column 1', text='Column 1')
tree.heading('Column 2', text='Column 2')

# Insert some sample data
data = [('Row 1', 'Value 1'), ('Row 2', 'Value 2'), ('Row 3', 'Value 3')]
for item in data:
    tree.insert('', 'end', values=item)

# Bind the selection event
tree.bind('<<TreeviewSelect>>', on_select)

# Use the grid geometry manager to make the Treeview responsive
tree.grid(row=1, column=0, columnspan=3, sticky='nsew')

# Set column weights to make the search box take up half of the window width
root.columnconfigure(1, weight=1)

# Set row weight to make the Treeview take up the remaining space
root.rowconfigure(1, weight=1)

# Start the main loop
root.mainloop()
