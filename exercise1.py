import tkinter
from tkinter import Button
import tkinter.font as font
from tkinter import messagebox as tkmsg
from tkinter import Label
from tkinter import Entry

window = tkinter.Tk()

# to rename the title of the window
window.title("GUI")
window.geometry('500x200')
myfont=font.Font(family='Times New Roman',size=12)

#function when the button click
def Sum():
    num1=int(ent1.get())
    num2=int(ent2.get())
    result=num1+num2
    info= ent1.get()+"+"+ent2.get()+"="+str(result)+"\n Exit Application?"
    Msg=tkmsg.askyesno("Result",info)
    if Msg==True:
        window.destroy()
    else:
        ent1.delete(0,'end')
        ent2.delete(0,'end')
        ent1.focus()
        
lbl1=Label(window,text="Number1:");
lbl1.place(x=0,y=10)
ent1=Entry(window,width=30)
ent1.place(x=100,y=10)

lbl2=Label(window,text="Number2 :");
lbl2.place(x=0,y=30)
ent2=Entry(window,width=30)
ent2.place(x=100,y=30)

btn=Button(window, text="Sum",font=myfont, command=Sum)
btn.place(x=300, y=10)

window.mainloop()
