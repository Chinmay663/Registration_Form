# from tkinter import *
# screen =Tk()
# screen.geometry("400x400")
# screen.title("Welcome")

# label1 =Label(text="test", font=("arial",12,),bg="white",fg="black").pack()
# Checkbutton

# screen.mainloop()
import tkinter as tk

def get_checkbutton_values():
    # Retrieve the values from the variables and print them
    print("Option 1:", var1.get())
    print("Option 2:", var2.get())
    print("Option 3:", var3.get())

# Create the main Tkinter window
root = tk.Tk()
root.title("Checkbutton Example")

# Variables to store the state of each Checkbutton
var1 = tk.StringVar(value="Off")  # Default value "Off"
var2 = tk.StringVar(value="Off")  # Default value "Off"
var3 = tk.StringVar(value="Off")  # Default value "Off"

# Create Checkbuttons and associate them with variables
checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=var1, onvalue="On", offvalue="Off")
checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=var2, onvalue="On", offvalue="Off")
checkbutton3 = tk.Checkbutton(root, text="Option 3", variable=var3, onvalue="On", offvalue="Off")

# Grid layout for the Checkbuttons
checkbutton1.grid(row=0, column=0, sticky="w")
checkbutton2.grid(row=1, column=0, sticky="w")
checkbutton3.grid(row=2, column=0, sticky="w")

# Button to retrieve values
btn_get_values = tk.Button(root, text="Get Values", command=get_checkbutton_values)
btn_get_values.grid(row=3, column=0, pady=10)

# Start the main Tkinter event loop
root.mainloop()
