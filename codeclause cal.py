import tkinter as tk

def on_button_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons in the grid
for (text, row, column) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear_entry, width=5, height=2)
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate, width=5, height=2)
    else:
        button = tk.Button(root, text=text, command=lambda value=text: on_button_click(value), width=5, height=2)
    
    button.grid(row=row, column=column)

# Run the application
root.mainloop()
