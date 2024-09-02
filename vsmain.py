from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import sqlite3

screen =Tk()
screen.geometry("600x600")
screen.title("Registration Form")
screen.config(bg="Yellow")

def database1():
    full_name=fn.get()
    Country=var.get()
    varc1=var_c1.get()
    varc2=var_c2.get()
    varc3=var_c3.get()
    char1=c1.cget("text")#accessing the text value of checkbutton
    char2=c2.cget("text")
    char3=c3.cget("text")
    Game_role=[[varc1,char1],[varc2,char2],[varc3,char3]]#var_c1 and all have intvar() value
    Level=var_r1.get()


    listGR=[]
    for i in Game_role:
        if(i[0]>=1):
            listGR.append(i[1])

    strGR= " ".join(listGR)
    GRole=strGR

    CNN=sqlite3.connect("Registration_form.dp")
    with CNN:
        cursor1=CNN.cursor()
        cursor1.execute("CREATE TABLE IF NOT EXISTS Player (Name TEXT,Country TEXT,GRole TEXT,Level TEXT)")
        cursor1.execute("INSERT INTO Player(Name,Country,GRole,Level) VALUES (?,?,?,?)",
                        (full_name,Country,GRole,Level))
        CNN.commit()


#function for accessing and printing the data the registration form have
def prilog():
    full_name=fn.get()
    Country=var.get()
    varc1=var_c1.get()
    varc2=var_c2.get()
    varc3=var_c3.get()
    char1=c1.cget("text")#accessing the text value of checkbutton
    char2=c2.cget("text")
    char3=c3.cget("text")
    Game_role=[[varc1,char1],[varc2,char2],[varc3,char3]]#var_c1 and all have intvar() value


    Level=var_r1.get()
    print(f"You are {full_name} from {Country}")
    listGR=[]
    for i in Game_role:
        if(i[0]>=1):
            listGR.append(i[1])

    strGR= " ".join(listGR)
    print(f"You are " + strGR)

    print(f"You are a {Level} player")
    tkinter.messagebox.showinfo("OKay h","You are successfully registered!!")
    
def abbt():
    tkinter.messagebox.showinfo("Attention!!",
                       "Register on this form as for trails happening for Hinderland Scotland program")

def exiting():
    exit()

def second_window():
    screen2=Tk()
    screen2.geometry("300x300")
    screen2.config(bg="blue")
    
    def status():
        slabel1=Label(screen2,text="You have registered wait for date of trail",font=("arial",8,"bold"),bg="white",fg="black")
        slabel1.pack()

    sbutton1=Button(screen2,text="Status",font=("arial",12,"bold"),fg="black",bg="white",width=5,
                relief=RAISED,command=status)
    sbutton1.pack(anchor="center",pady=50)



#menubar
minutus=Menu(screen)
screen.config(menu=minutus)

submenu1=Menu(minutus)
minutus.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="exit",command=exiting)
submenu1.add_command(label="whatsUp bukers")

submenu2=Menu(minutus)
minutus.add_cascade(label="Option",menu=submenu2)
submenu2.add_command(label="About",command=abbt)





#image
imageMan = Image.open("cricletbatsmanlogo.png")
imageMan_resized =imageMan.resize((140,140))
photoMan = ImageTk.PhotoImage(imageMan_resized)

lab =Label(image=photoMan)
lab.place(x=250,y=50)


#heading
label = Label(screen,text="Registration Form",font=("arial",12,"bold"),fg="black",bg="sky blue",
              relief="solid")
label.place(x=250,y=20)


#Names etc labels and entry
fn=StringVar()
var=StringVar()
var_c1=IntVar()
var_c2=IntVar()
var_c3=IntVar()
var_r1=StringVar(value="Dummy Value")


##Full name
label1=Label(text="Full name",width =10,font=("arial",8,"bold"),bg="white",fg="black")
label1.place(x=160,y=250)
entry1 =Entry(screen, textvariable=fn)
entry1.place(x=250,y=250,width=200)

##Country
label2=Label(text="Country",width =10,font=("arial",8,"bold"),bg="white",fg="black")
label2.place(x=160,y=300)

ListCountry=["India","Pakistan","USA ","Ireland","Canada","New Zealand","South Africa",
             "Afghanistan","Sri Lanka"]
dropdownlist =OptionMenu(screen, var,*ListCountry)
var.set("Select country")
dropdownlist.config(width=15)
dropdownlist.place(x=250,y=300)

#checkbox
label3=Label(text="Game role",width =10,font=("arial",8,"bold"),bg="white",fg="black")
label3.place(x=160,y=350)
c1=Checkbutton(screen,text="Batsman", variable=var_c1)
c1.place(x=250,y=350)
c2=Checkbutton(screen,text="Bowler", variable=var_c2)
c2.place(x=330,y=350)
c3=Checkbutton(screen,text="Wicketkeeper", variable=var_c3)
c3.place(x=400,y=350)

#radiobutton
label4=Label(text="Level",width =10,font=("arial",8,"bold"),bg="white",fg="black")
label4.place(x=160,y=400)
r1=Radiobutton(screen,text="Professional",variable=var_r1,value="Professional").place(x=270,y=400)
r2=Radiobutton(screen,text="Amateur",variable=var_r1,value="Amateur").place(x=370,y=400)#notice that here variable is same as var_r1  


#login button
button1 =Button(screen,text="Login",font=("arial",12,"bold"),fg="black",bg="white",width=5,
                relief=RAISED,command=database1)
button1.place(x=120,y=450)
screen.bind("<Return>",database1)


#exit button
button2 =Button(screen,text="Exit",font=("arial",12,"bold"),fg="black",bg="white",width=5,
                relief=SUNKEN,command=exiting)
button2.place(x=450,y=450)

#finish button
button3 =Button(screen,text="Finish",font=("arial",12,"bold"),fg="black",bg="Light green",width=5,
                relief=GROOVE,command=second_window)
button3.pack(anchor="e")



screen.mainloop()