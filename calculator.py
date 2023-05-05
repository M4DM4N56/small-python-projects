# Simple Calculator
# started on Sept. 24, 2022
# finished on Sept. 26, 2022
from tkinter import *
root = Tk()
global num1
global num2
global op

# window name
root.title("Simple calculator")
root.configure(bg='#BCC9FF')


# top display
display = Entry(root, width=28, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)


def number_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))
    return


def clear_click():
    display.delete(0, END)


def operate(operator):
    global num1
    global op
    num1 = display.get()
    num1 = float(num1)

    display.delete(0, END)

    # checking operator types
    if operator == "+":
        op = add
    elif operator == "−":
        op = subtract
    elif operator == "×":
        op = multiply
    elif operator == "÷":
        op = divide


def answer():
    global op
    global num2
    num2 = display.get()
    num2 = float(num2)
    display.delete(0, END)

    if op == add:
        display.insert(0, num1 + num2)
    if op == subtract:
        display.insert(0, num1 - num2)
    if op == multiply:
        display.insert(0, num1 * num2)
    if op == divide:
        display.insert(0, num1 / num2)


def decimal():
    num = display.get()
    num = num + "."
    display.delete(0, END)
    display.insert(0, num)
    return


# number buttons
one = Button(root, padx=15, pady=15, text="1", command=lambda: number_click(1))
one.grid(row=1, column=0)


two = Button(root, padx=15, pady=15, text="2", command=lambda: number_click(2))
two.grid(row=1, column=1)

three = Button(root, padx=15, pady=15, text="3", command=lambda: number_click(3))
three.grid(row=1, column=2)

four = Button(root, padx=15, pady=15, text="4", command=lambda: number_click(4))
four.grid(row=2, column=0)

five = Button(root, padx=15, pady=15, text="5", command=lambda: number_click(5))
five.grid(row=2, column=1)

six = Button(root, padx=15, pady=15, text="6", command=lambda: number_click(6))
six.grid(row=2, column=2)

seven = Button(root, padx=15, pady=15, text="7", command=lambda: number_click(7))
seven.grid(row=3, column=0)

eight = Button(root, padx=15, pady=15, text="8", command=lambda: number_click(8))
eight.grid(row=3, column=1)

nine = Button(root, padx=15, pady=15, text="9", command=lambda: number_click(9))
nine.grid(row=3, column=2)

zero = Button(root, padx=15, pady=15, text="0", command=lambda: number_click(0))
zero.grid(row=4, column=1)

# other buttons
sign = Button(root, padx=17, pady=15, text=".", command=decimal)
sign.grid(row=4, column=0)

clear = Button(root, padx=5, pady=15, bg="#FFBCBC", text="Clear", command=clear_click)
clear.grid(row=4, column=2)

# operators
add = Button(root, padx=15, pady=15, bg="#CCCCCC", text="+", command=lambda: operate("+"))
add.grid(row=1, column=3)

subtract = Button(root, padx=15, pady=15, bg="#CCCCCC", text="−", command=lambda: operate("−"))
subtract.grid(row=2, column=3)

multiply = Button(root, padx=15, pady=15, bg="#CCCCCC", text="×", command=lambda: operate("×"))
multiply.grid(row=3, column=3)

divide = Button(root, padx=15, pady=15, bg="#CCCCCC", text="÷", command=lambda: operate("÷"))
divide.grid(row=4, column=3)

# equals
equal = Button(root, padx=83.5, pady=15, bg="#CCCCCC", text="=", command=answer)
equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
