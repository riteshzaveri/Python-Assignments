#step1: import tkinter
from tkinter import *
import tkinter.messagebox

#step2: gui interaction
window = Tk()

#step3: adding inputs

# Print hello world
# inp = Label(window, text="Hello World!")
# inp.pack()

# Basic modification using tkinter
# window.title("Simple")
# window.geometry("500x700")
# window.config(bg="yellow")
# frame1 = Frame(window, width=300, height=300, cursor="dot")
# frame2 = Frame(window, width=300, height=300, cursor="dotbox")
#
# button1 = Button(frame1, text="Button1", bg="blue")
# button2= Button(frame2, text="Button2", bg="green")
# button3 = Button(frame1, text="Button3", fg="blue")
#
# frame1.pack(side=TOP)
# frame2.pack(side=BOTTOM)
# button1.pack()
# button2.pack()
# button3.pack()

# Entry Box and grid layout
# window.title("Simple")
# window.geometry("250x50")
#
# label1 = Label(window, text="mail")
# label2 = Label(window, text="password")
#
# e1 = Entry(window, width=40, borderwidth=5)
# e2 = Entry(window)
#
# label1.grid(row=0, column=1)
# label2.grid(row=1, column=1)
# e1.grid(row=0, column=2)
# e2.grid(row=1, column=2)

# Pack
# window.title("Simple")
# window.geometry("500x500")

# label1 = Label(window, text="Label-1", bg="red", fg="white")
# label2 = Label(window, text="Label-2", bg="blue", fg="white")
# label3 = Label(window, text="Label-3", bg="green", fg="white")
#
# label1.pack(side=TOP, fill=X, expand=False)
# label2.pack(side=LEFT, fill=Y, expand=False)
# label3.pack(side=RIGHT, fill=Y, expand=False)

# Handling Buttons
# window.title("Simple")
# window.geometry("500x500")
# def log_entry():
#     print("Logged In")
#
# button = Button(window, text="LOGIN", command=log_entry, width=12, bg="red", fg="white", font=("bold", 12), activebackground="black", activeforeground="white")
# button.pack()

# Menubar
# menu = Menu(window)
# file = Menu(menu, tearoff=0) # tearoff = 1 is a floating menu
# menu.add_command(label="New")
# menu.add_command(label="Open")
# menu.add_command(label="Save")
# menu.add_command(label="Save as")
# file.add_separator()  #This is a line
# file.add_command(label="Exit", command=window.quit)
#
# menu.add_cascade(label="File", menu=file)
# window.config(menu=menu)

# Message Box
# tkinter.messagebox.showinfo("Info", "Running out of time")
# tkinter.messagebox.showwarning("Info", "Running out of time")
# tkinter.messagebox.showerror("Info", "Running out of time")
# question = tkinter.messagebox.askyesno("Weather", "Will it rain?")
#
# if question == True:
#     print("Take an umbrella")
# else:
#     print("Okay")

# Drawing
# c = Canvas(window, width=500, height=500)
# c.pack()
#
# c.create_line(0,0,500,500, width=5, fill="green", dash=(3,3))
# c.create_line(0,500,500,0, width=5, fill="blue", dash=(3,3))
# c.create_rectangle(150,125,450,375, fill="red", outline="yellow", width=5)

# Message box 2
# window.geometry("500x500")
# '''
# message = Message(window, text="Python")
# message.pack()
# '''
# '''
# var = StringVar()
# message = Message(window, textvariable=var, relief=RAISED, padx=20, pady=20) # relief raised gives 2D effect. Looks like a button
# message.pack()
# window.mainloop()
# var.set("Welcome")
# message.pack()
# '''
# var = StringVar()
# ent_var = StringVar()
#
# def insert():
#     result = ent_var.get()
#     var.set(result)
#
# message = Message(window, textvariable=var, relief=RAISED, padx=50, pady=50)
# entry = Entry(window, textvariable=ent_var)
# button = Button(window, text="Okay", command=insert)
# message.pack()
# entry.pack()
# button.pack()

# Checkbox
# window.geometry("500x500")
#
# check_box_1 = IntVar()
# check_box_2 = IntVar()
# check_box_3 = IntVar()
#
# chk_btn_1 = Checkbutton(window, text="apple", onvalue=1, offvalue=0, height=2, width=10, variable=check_box_1)
# chk_btn_2 = Checkbutton(window, text="mango", onvalue=1, offvalue=0, height=2, width=10, variable=check_box_1)
# chk_btn_3 = Checkbutton(window, text="plum", onvalue=1, offvalue=0, height=2, width=10, variable=check_box_1)
#
# chk_btn_1.pack()
# chk_btn_2.pack()
# chk_btn_3.pack()

# Place
# window.geometry("500x500")
#
# # Place takes place in X and Y axis
# button = Button(window, text="Button", width=12)
# button.place(x=25, y=25)

#step4: main loop
window.mainloop()