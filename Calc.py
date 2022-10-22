from tkinter import *
from math import *

window = Tk()
window.title("Calculator")

number = 0
previous_number = 0
action = ""

# Numbers buttons ---------------

def add_digit(digit):
    global number
    number = number * 10 + digit
    entry_text.set(number)

def button_press_1():
    add_digit(1)

def button_press_2():
    add_digit(2)

def button_press_3():
    add_digit(3)

def button_press_4():
    add_digit(4)

def button_press_5():
    add_digit(5)

def button_press_6():
    add_digit(6)

def button_press_7():
    add_digit(7)

def button_press_8():
    add_digit(8)

def button_press_9():
    add_digit(9)

def button_press_0():
    add_digit(0)

# Actions buttons -----------------

def make_action(chosen_action):
    global number
    global previous_number
    global action

    action = chosen_action
    previous_number = number
    number = 0

    entry_text.set(number)

def button_press_plus():
    make_action("+")

def button_press_minus():
    make_action("-")

def button_press_delit():
    make_action("/")

def button_press_umnojit():
    make_action("*")

# Better actions -------------

def button_press_cos():
    make_action("cos")

def button_press_sin():
    make_action("sin")

def button_press_radix():
    make_action("radix")

def button_press_degree():
    make_action("**")

# Result button --------------

def button_press_result():
    global number
    global previous_number
    global action

    if action == '+':
        number = previous_number + number
    elif action == '-':
        number = previous_number - number
    elif action == '*':
        number = previous_number * number
    elif action == '/':
        number = previous_number / number
    elif action == 'cos':
        number = cos(previous_number)
    elif action == 'sin':
        number = sin(previous_number)
    elif action == 'radix':
        number = sqrt(previous_number)
    elif action == '**':
        number = previous_number ** number

    entry_text.set(number)

# Clear button ------------------------------
def button_press_clear():
    global number
    global previous_number

    number = 0
    previous_number = 0

    entry_text.set(number)


# GUI

entry_text = StringVar()
Entry(window, width=40, textvariable=entry_text).grid(row=0, column=0, columnspan=4)

Button(window, text='1', height=5, width=10, command=button_press_1).grid(row=1, column=0)
Button(window, text='2', height=5, width=10, command=button_press_2).grid(row=1, column=1)
Button(window, text='3', height=5, width=10, command=button_press_3).grid(row=1, column=2)
Button(window, text='4', height=5, width=10, command=button_press_4).grid(row=2, column=0)
Button(window, text='5', height=5, width=10, command=button_press_5).grid(row=2, column=1)
Button(window, text='6', height=5, width=10, command=button_press_6).grid(row=2, column=2)
Button(window, text='7', height=5, width=10, command=button_press_7).grid(row=3, column=0)
Button(window, text='8', height=5, width=10, command=button_press_8).grid(row=3, column=1)
Button(window, text='9', height=5, width=10, command=button_press_9).grid(row=3, column=2)
Button(window, text='0', height=5, width=10, command=button_press_0).grid(row=4, column=1)
Button(window, text='=', height=5, width=10, command=button_press_result).grid(row=4, column=0)
Button(window, text='AC', height=5, width=10, command=button_press_clear).grid(row=4, column=2)

Button(window, text='+', height=5, width=10, command=button_press_plus).grid(row=1, column=3)
Button(window, text='-', height=5, width=10, command=button_press_minus).grid(row=2, column=3)
Button(window, text='*', height=5, width=10, command=button_press_umnojit).grid(row=3, column=3)
Button(window, text='/', height=5, width=10, command=button_press_delit).grid(row=4, column=3)

Button(window, text='cos', height=5, width=10, command=button_press_cos).grid(row=1, column=4)
Button(window, text='sin', height=5, width=10, command=button_press_sin).grid(row=2, column=4)
Button(window, text='√', height=5, width=10, command=button_press_radix).grid(row=3, column=4)
Button(window, text='radix', height=5, width=10, command=button_press_degree).grid(row=4, column=4)


mainloop()
