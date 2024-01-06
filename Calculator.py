import tkinter as tk

def on_click(event):
    current_text = result_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to store the result
result_var = tk.StringVar()

# Entry widget to display the result
result_entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 18), justify="right", bd=10)
result_entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Helvetica", 14), padx=20, pady=20)
    button.grid(row=row_val, column=col_val, sticky="nsew")
    button.bind("<Button-1>", on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights to make buttons expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
