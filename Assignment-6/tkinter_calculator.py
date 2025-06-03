#step1: import tkinter
from tkinter import *

#step2: gui interaction
window = Tk()
window.geometry("600x450")

#step3: adding inputs

# ENTRY BOX
e = Entry(window, width=40, borderwidth=3)
e.place(x=10, y=10)

# BUTTONS
def click(num):
    try:
        result = e.get()
        e.delete(0, END)
        e.insert(0, str(result) + str(num))
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text="1", width=10, command=lambda:click(1))
b.place(x=10, y=50)

b = Button(window, text="2", width=10, command=lambda:click(2))
b.place(x=135, y=50)

b = Button(window, text="3", width=10, command=lambda:click(3))
b.place(x=260, y=50)

b = Button(window, text="4", width=10, command=lambda:click(4))
b.place(x=10, y=100)

b = Button(window, text="5", width=10, command=lambda:click(5))
b.place(x=135, y=100)

b = Button(window, text="6", width=10, command=lambda:click(6))
b.place(x=260, y=100)

b = Button(window, text="7", width=10, command=lambda:click(7))
b.place(x=10, y=150)

b = Button(window, text="8", width=10, command=lambda:click(8))
b.place(x=135, y=150)

b = Button(window, text="9", width=10, command=lambda:click(9))
b.place(x=260, y=150)

b = Button(window, text="0", width=10, command=lambda:click(0))
b.place(x=10, y=200)

# OPERATORS
def add():
    try:
        n1 = e.get()
        global math
        math = "addition"
        global i
        i = int(n1)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text="+", width=10, command=add)
b.place(x=135, y=200)

def sub():
    try:
        n1 = e.get()
        global math
        math = "subtraction"
        global i
        i = int(n1)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text="-", width=10, command=sub)
b.place(x=260, y=200)

def mult():
    try:
        n1 = e.get()
        global math
        math = "multiplication"
        global i
        i = int(n1)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text="*", width=10, command=mult)
b.place(x=10, y=250)

def div():
    try:
        n1 = e.get()
        global math
        math = "division"
        global i
        i = int(n1)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

b = Button(window, text="/", width=10, command=div)
b.place(x=135, y=250)

def equal():
    try:
        n2 = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, i + int(n2))
        elif math == "subtraction":
            e.insert(0, i - int(n2))
        elif math == "multiplication":
            e.insert(0, i * int(n2))
        elif math == "division":
            e.insert(0, i / int(n2))
    except ZeroDivisionError:
        e.insert(0, "Error: Divide by 0")
    except:
        e.insert(0, "Error")

b = Button(window, text="=", width=10, command=equal)
b.place(x=260, y=250)

def clear():
    try:
        e.delete(0, END)
    except:
        e.insert(0, "Error")

b = Button(window, text="clear", width=10, command=clear)
b.place(x=10, y=300)

#step4: main loop
window.mainloop()