from tkinter import *
from tkinter import messagebox
import numpy as np

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()
root.title("연습")
root.geometry("640x400+100+100")
root.resizable(False, False)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="상단메뉴1", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
menubar.add_cascade(label="상단메뉴2", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="상단메뉴3", menu=helpmenu)

root.config(menu=menubar)


num1 = 2
num2 = 1

def showUp():
    global num1, num2 
    num1 = np.random.randint(9) + 1
    num2 = np.random.randint(9) + 1
    
    label.config(text=str(num1) + "x" + str(num2)) 

    label.grid( row = 0, column = 0  )
    button1.grid( row = 1, column = 0  )
    button2.grid( row = 2, column = 0  )
    textbox.grid( row = 3, column = 0  )

def checkUp():
    global num1, num2
    answer = textbox.get()

    if( int(answer) == int(num1*num2) ):
        messagebox.showinfo( "결과", "정답입니다.")
    else:
        messagebox.showinfo( "결과", "오답입니다.")

    button1.grid( row = 0, column = 0  )
    button2.grid( row = 1, column = 0  )
    textbox.grid( row = 2, column = 0  )
    textbox.delete(0, END);

    
    root.event_generate('<<showUp>>', when='head')



label= Label(root, text="0")


button1 = Button( root, text="시작", overrelief = "solid", width = 15, command=showUp, repeatdelay=1000, repeatinterval=100)
button1.grid( row = 0, column = 0  )

button2 = Button( root, text="제출(확인)", overrelief = "solid", width = 15, command=checkUp, repeatdelay=1000, repeatinterval=100)
button2.grid( row = 1, column = 0  )

textbox = Entry( root, width=20 )
textbox.grid( row = 2, column = 0  )


root.mainloop()

