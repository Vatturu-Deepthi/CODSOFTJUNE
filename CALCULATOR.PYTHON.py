import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Cannot divide by zero")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")  # Default operation choice

# Create operation choice dropdown
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)

# Create a button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)

# Place widgets on the window
entry_num1.pack()
operation_menu.pack()
entry_num2.pack()
calculate_button.pack()
result_label.pack()

# Start the main loop
root.mainloop()
        
    
    
    
   
    
