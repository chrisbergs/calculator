from tkinter import *
import sys
import os


button_width = 5
button_height = 2

button_bg = '#CCCCCC'
number_bg = '#DEDEDE'
root_bg = '#BBBBBB'

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

def add_value(val):
    print(val)
    print(e.get())
    return


def validate(action, index, new_value, prior_value, key, validation_type, trigger_type, widget_name):
    if key == 'q' or key == 'Q':
        print('***Closing J0ker Calculator***')
        sys.exit()
    elif key in key_list:
        return True
    else:
        if new_value == '':
            return True
        else:
            try:
                float(new_value)
                return True
            except:
                return False



root = Tk()
val = (root.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
key_list = ['+', '-', '/', '*', '%']
root.title("J0ker Calculator")
root.resizable(0,0)

entry = Frame(root, bg=root_bg)
entry.pack(fill=BOTH, expand=True)

e = Entry(entry, relief=FLAT, validate='key', validatecommand=val, font=('Verdana', 20), bg=root_bg, highlightthickness=0)
e.pack(fill=BOTH, expand=True)

calc = Frame(root, bg=root_bg)
calc.pack() 

button_clear_all = Button(calc, text="CE", command=ce, width=8, height=2, bg=button_bg)
button_clear = Button(calc, text="C", command=c, width=8, height=2, bg=button_bg)
button_percent = Button(calc, text="%", command=percent, width=8, height=2, bg=button_bg)
button_divide = Button(calc, text="/", command=divide, width=8, height=2, bg=button_bg)

button_7 = Button(calc, text="7", command=lambda: add_value(7), width=5, height=2, bg=number_bg)
button_8 = Button(calc, text="8", command=add_value, width=5, height=2, bg=number_bg)
button_9 = Button(calc, text="9", command=add_value, width=5, height=2, bg=number_bg)
button_multiply = Button(calc, text="*", command=add_value, width=5, height=2, bg=button_bg)

button_4 = Button(calc, text="4", command=add_value, width=5, height=2, bg=number_bg)
button_5 = Button(calc, text="5", command=add_value, width=5, height=2, bg=number_bg)
button_6 = Button(calc, text="6", command=add_value, width=5, height=2, bg=number_bg)
button_subtract = Button(calc, text="-", command=add_value, width=5, height=2, bg=button_bg)

button_1 = Button(calc, text="1", command=add_value, width=5, height=2, bg=number_bg)
button_2 = Button(calc, text="2", command=add_value, width=5, height=2, bg=number_bg)
button_3 = Button(calc, text="3", command=add_value, width=5, height=2, bg=number_bg)
button_addtract = Button(calc, text="+", command=add_value, width=5, height=2, bg=button_bg)

button_dot = Button(calc, text=".", command=add_value, width=5, height=2, bg=button_bg)
button_0 = Button(calc, text="0", command=add_value, width=5, height=2, bg=number_bg)
button_erase = Button(calc, text="<-", command=erase, width=5, height=2, bg=button_bg)
button_equal = Button(calc, text="=", command=add_value, width=5, height=2, bg=button_bg)


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

e.focus()
root.mainloop()
