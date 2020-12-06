from tkinter import *
import sys
import os

def c():
    return

def ce():
    return

def erase():
    return

def addtract():
    return

def subtract():
    return

def multiply():
    return

def divide():
    return

def percent():
    return

def add_dot():
    return

def calculate():
    return

def add_value():
    return

root = Tk()
root.title("J0ker Calculator")
root.resizable(0,0)
root.geometry("300x300")

entry = Frame(root, bg='red')
entry.pack(fill=BOTH)

e = Entry(entry)
e.pack(fill=BOTH)

calc = Frame(root, bg='black')
calc.pack(fill=BOTH, expand=True)

button_clear_all = Button(calc, text="CE", command=add_value, width=5, height=3)
button_clear = Button(calc, text="C", command=add_value, width=5, height=3)
button_percent = Button(calc, text="%", command=add_value, width=5, height=3)
button_divide = Button(calc, text="/", command=add_value, width=5, height=3)

button_7 = Button(calc, text="7", command=add_value, width=5, height=2)
button_8 = Button(calc, text="8", command=add_value, width=5, height=2)
button_9 = Button(calc, text="9", command=add_value, width=5, height=2)
button_multiply = Button(calc, text="x", command=add_value, width=5, height=2)

button_4 = Button(calc, text="4", command=add_value, width=5, height=2)
button_5 = Button(calc, text="5", command=add_value, width=5, height=2)
button_6 = Button(calc, text="6", command=add_value, width=5, height=2)
button_subtract = Button(calc, text="-", command=add_value, width=5, height=2)

button_1 = Button(calc, text="1", command=add_value, width=5, height=2)
button_2 = Button(calc, text="2", command=add_value, width=5, height=2)
button_3 = Button(calc, text="3", command=add_value, width=5, height=2)
button_addtract = Button(calc, text="+", command=add_value, width=5, height=2)

button_dot = Button(calc, text=".", command=add_value, width=5, height=2)
button_0 = Button(calc, text="0", command=add_value, width=5, height=2)
button_erase = Button(calc, text="<-", command=erase, width=5, height=2)
button_equal = Button(calc, text="=", command=add_value, width=5, height=2)


button_clear_all.grid(row=0, column=0, sticky='nesw')
button_clear.grid(row=0, column=1, sticky='nesw')
button_percent.grid(row=0, column=2, sticky='nesw')
button_divide.grid(row=0, column=3, sticky='nesw')

button_7.grid(row=1, column=0, sticky='nesw')
button_8.grid(row=1, column=1, sticky='nesw')
button_9.grid(row=1, column=2, sticky='nesw')
button_multiply.grid(row=1, column=3, sticky='nesw')

button_4.grid(row=2, column=0, sticky='nesw')
button_5.grid(row=2, column=1, sticky='nesw')
button_6.grid(row=2, column=2, sticky='nesw')
button_subtract.grid(row=2, column=3, sticky='nesw')

button_1.grid(row=3, column=0, sticky='nesw')
button_2.grid(row=3, column=1, sticky='nesw')
button_3.grid(row=3, column=2, sticky='nesw')
button_addtract.grid(row=3, column=3, sticky='nesw')

button_dot.grid(row=4, column=0, sticky='nesw')
button_0.grid(row=4, column=1, sticky='nesw')
button_erase.grid(row=4, column=2, sticky='nesw')
button_equal.grid(row=4, column=3, sticky='nesw')

root.mainloop()
