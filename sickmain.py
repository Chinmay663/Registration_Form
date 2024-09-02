from tkinter import *

sick = []

# def getChecked():
#    for i in range(len(sick)):
#     selected = ""
#     if sick[i].get() >= 1:
#        selected += str(i)
#        print(selected)
def getChecked():
    for var in sick:
        value = var.get()
        if value:
            print(value)




root = Tk()
root.geometry('850x750')
root.title("Registration Form")

# for i in range(6):
#     option = IntVar()
#     option.set(0)
#     sick.append(option)
for i in range(6):
    option = StringVar(value="")
    sick.append(option)




   # Conditions checkbutton
label_6 = Label(root, text="Have you ever had ( Please check all that apply ) :", width=50, font= 
                 ("bold", 10))
label_6.place(x=35, y=330)

Checkbutton(root, command=getChecked, text="Anemia", variable=sick[0],
            onvalue="Anemia",offvalue="").place(x=130, y=350)

Checkbutton(root, command=getChecked, text="Asthma", variable=sick[1],
            onvalue="Asthma",offvalue="").place(x=270, y=350)

Checkbutton(root, command=getChecked, text="Arthritis", variable=sick[2],
            onvalue="Arthritis",offvalue="").place(x=410, y=350)

Checkbutton(root, command=getChecked, text="Cancer", variable=sick[3],
            onvalue="Cancer",offvalue="").place(x=560, y=350)

Checkbutton(root, command=getChecked, text="Gout", variable=sick[4],
            onvalue="Gout",offvalue="").place(x=130, y=380)

Checkbutton(root, command=getChecked, text="Diabetes", variable=sick[5],
            onvalue="Diabetes",offvalue="").place(x=270, y=380)

# submit button
Button(root, text='Submit', command=getChecked, width=20, bg='brown', fg='white').place(x=180, y=600)

root.mainloop()