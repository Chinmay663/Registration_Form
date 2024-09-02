from tkinter import *

window =Tk()
window.geometry("300x300")
window.config(bg="blue")

def printo():
    v1=var1.get()
    v2=var2.get()
    print(f"the check {v1} {v2}")

def printobol():
    v3=stateCh1.get()
    v4=stateCh2.get()

    char1=check3.cget("text")
    char2=check4.cget("text")
    l3=[[v3,char1],[v4,char2]]
    for i in l3:
        if(i[0]>=1):
            print(f"{i[1]} is checked.")





var1 =StringVar()
var2=StringVar()
stateCh1=IntVar()
stateCh2=IntVar()



check1=Checkbutton(window, text="Ch1",variable=var1, onvalue="Ch1",offvalue="").pack()
check2=Checkbutton(window, text="Ch2",variable=var2, onvalue="Ch2",offvalue="").pack()


check3=Checkbutton(window, text="Ch3",variable=stateCh1)
check3.pack()
check4=Checkbutton(window, text="Ch4",variable=stateCh2)
check4.pack()



but1=Button(window,text="Login",font=("arial",12,"bold"),fg="black",bg="white",width=5,
                relief=RAISED,command=printo).pack()
but2=Button(window,text="Login2",font=("arial",12,"bold"),fg="black",bg="white",width=5,
                relief=RAISED,command=printobol).pack()





window.mainloop()
