# # import tkinter as tk

# # def show_selected():
# #     selected = []
# #     for var, text, on_val in zip(vars, checkbox_texts, on_values):
# #         if var.get() == on_val:
# #             selected.append(text)
# #     if selected:
# #         print("Selected options:", ", ".join(selected))
# #     else:
# #         print("No options selected.")

# # # Initialize tkinter
# # root = tk.Tk()
# # root.title("Check Button Example with onvalue and offvalue")

# # # Create tkinter variables to store the state of check buttons
# # var1 = tk.BooleanVar(value="Option 1")
# # var2 = tk.BooleanVar(value="Option 2")
# # var3 = tk.BooleanVar(value="Option 3")

# # vars = [var1, var2, var3]
# # checkbox_texts = ["Option 1", "Option 2", "Option 3"]
# # on_values = ["Option 1", "Option 2", "Option 3"]

# # # Create check buttons
# # for i, text in enumerate(checkbox_texts):
# #     cb = tk.Checkbutton(root, text=text, variable=vars[i], onvalue=on_values[i], offvalue="")
# #     cb.pack(anchor=tk.W)

# # # Create a button to show selected options
# # show_button = tk.Button(root, text="Show Selected", command=show_selected)
# # show_button.pack()

# # # Run the tkinter main loop
# # root.mainloop()

# import tkinter as tk

# def get_checkbutton_values():
#     # Retrieve the values from the variables
#     print("Option 1:", var1.get())
#     print("Option 2:", var2.get())
#     print("Option 3:", var3.get())

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Checkbutton Example")

# # Variables to store the state of each Checkbutton
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# var3 = tk.IntVar()

# # Create Checkbuttons and associate them with variables
# checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=var1)
# checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=var2)
# checkbutton3 = tk.Checkbutton(root, text="Option 3", variable=var3)

# # Grid layout for the Checkbuttons
# checkbutton1.grid(row=0, column=0, sticky="w")
# checkbutton2.grid(row=1, column=0, sticky="w")
# checkbutton3.grid(row=2, column=0, sticky="w")

# # Button to retrieve values
# btn_get_values = tk.Button(root, text="Get Values", command=get_checkbutton_values)
# btn_get_values.grid(row=3, column=0, pady=10)

# # Start the main Tkinter event loop
# root.mainloop()
import tkinter as tk

def print_selection():
    selected_value = var.get()
    if selected_value == "":
        print("No option selected.")
    else:
        print(f"Selected option: {selected_value}")

root = tk.Tk()
root.geometry("300x200")
root.title("Radiobutton Demo")

# Dummy option to represent initial unchecked state
var = tk.StringVar() 
var.set("")# Initialize with an empty string

# Radiobuttons
rb1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
rb1.pack(anchor=tk.W)

rb2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
rb2.pack(anchor=tk.W)

rb3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3")
rb3.pack(anchor=tk.W)

# Print button
print_btn = tk.Button(root, text="Print Selection", command=print_selection)
print_btn.pack(pady=10)

root.mainloop()