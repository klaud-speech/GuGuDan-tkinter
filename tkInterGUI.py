from tkinter import *

count = 0

def calc(event):
    lb2.config(text=str(eval(txt.get())))

def countplus():
    global count
    count+=1
    lb1.config(text=str(count))

def countminus():
    global count
    count-=1
    lb1.config(text=str(count))



w = Tk()
w.title("연습창입니다")
w.geometry('300x200')

lb1 = Label(w, text='0'); lb1.pack()
txt = Entry(w); txt.bind('<Return>', calc); txt.pack()
lb2 = Label(w, text='0'); lb2.pack()

btn1 = Button( w, text='+', width=15, command=countplus); btn1.pack()
btn2 = Button( w, text='-', width=15, command=countminus); btn2.pack()

w.mainloop()
