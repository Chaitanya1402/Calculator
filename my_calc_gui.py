from tkinter import *
import math as mh


def call_num(number):
    entry.insert(END, number)


def clear(how):
    string = entry.get()[:-1]
    entry.delete(0, END)
    if how == "last":
        entry.insert(0, string)


def do_math_2_nos(operator):
    global num1
    global math
    math = operator
    num1 = float(entry.get())
    entry.delete(0, END)


def equal_to():
    num2 = float(entry.get())
    entry.delete(0, END)

    if math == "divide":
        entry.insert(0, num1 / num2)
    elif math == "multiply":
        entry.insert(0, num1 * num2)
    elif math == "subtract":
        entry.insert(0, num1 - num2)
    elif math == "add":
        entry.insert(0, num1 + num2)
    elif math == "x raise y":
        entry.insert(0, mh.pow(num1, num2))
    else:
        entry.insert(0, num2)


def do_math_1_no(math):

    num1 = float(entry.get())
    entry.delete(0, END)

    if math == "sqrt":
        entry.insert(0, mh.sqrt(num1))
    elif math == "square":
        entry.insert(0, mh.pow(num1, 2))
    elif math == "cube":
        entry.insert(0, mh.pow(num1, 3))
    elif math == "reciprocal":
        entry.insert(0, 1/num1)
    elif math == "cuberoot":
        entry.insert(0, mh.pow(num1, 1/3))
    elif math == "fact":
        entry.insert(0, mh.factorial(num1))
    elif math == "sin":
        entry.insert(0, mh.sin(mh.radians(num1)))
    elif math == "cos":
        entry.insert(0, mh.cos(mh.radians(num1)))
    elif math == "tan":
        entry.insert(0, mh.tan(mh.radians(num1)))
    elif math == "log":
        entry.insert(0, mh.log10(num1))
    else:
        entry.insert(0, num1)


def second_body():

    Label(root, text="For trigonometry, measure angle in degrees", width=34)\
        .grid(row=1, column=0, columnspan=7)

    Button(root, text="√", width=4, pady=3, background="#9EFF64", font=100,
           command=lambda: do_math_1_no("sqrt")).grid(row=7, column=0)
    Button(root, text="x²", width=4, pady=3, background="#B0FF83", font=100,
           command=lambda: do_math_1_no("square")).grid(row=7, column=1)
    Button(root, text="x³", width=4, pady=3, background="#BDFF97", font=100,
           command=lambda: do_math_1_no("cube")).grid(row=7, column=2)
    Button(root, text="1/x", width=4, pady=3, background="#9EFF64", font=100,
           command=lambda: do_math_1_no("reciprocal")).grid(row=2, column=4)
    Button(root, text="xⁿ", width=4, pady=3, background="#D2FFB8", font=100,
           command=lambda: do_math_2_nos("x raise y")).grid(row=7, column=4)

    Button(root, text="³√", width=4, pady=3, background="#CAFFAC", font=100,
           command=lambda: do_math_1_no("cuberoot")).grid(row=7, column=3)
    Button(root, text="x!", width=4, pady=3, background="#A3FF6C", font=100,
           command=lambda: do_math_1_no("fact")).grid(row=3, column=4)
    Button(root, text="sin", width=4, pady=3, background="#B0FF83", font=100,
           command=lambda: do_math_1_no("sin")).grid(row=4, column=4)
    Button(root, text="cos", width=4, pady=3, background="#BDFF97", font=100,
           command=lambda: do_math_1_no("cos")).grid(row=5, column=4)
    Button(root, text="tan", width=4, pady=3, background="#CAFFAC", font=100,
           command=lambda: do_math_1_no("tan")).grid(row=6, column=4)
    Button(root, text="log₁₀", width=4, pady=3, background="#BDFF97", font=100,
           command=lambda: do_math_1_no("log")).grid(row=6, column=3)


def main_body():

    Button(root, text="1", width=4, pady=3, background="#FFF2F2", font=100,
           command=lambda: call_num(1)).grid(row=4, column=0)
    Button(root, text="2", width=4, pady=3, background="#FFF2F2", font=100,
           command=lambda: call_num(2)).grid(row=4, column=1)
    Button(root, text="3", width=4, pady=3, background="#FFF2F2", font=100,
           command=lambda: call_num(3)).grid(row=4, column=2)
    Button(root, text="4", width=4, pady=3, background="#FFE8E8", font=100,
           command=lambda: call_num(4)).grid(row=3, column=0)
    Button(root, text="5", width=4, pady=3, background="#FFE8E8", font=100,
           command=lambda: call_num(5)).grid(row=3, column=1)
    Button(root, text="6", width=4, pady=3, background="#FFE8E8", font=100,
           command=lambda: call_num(6)).grid(row=3, column=2)
    Button(root, text="7", width=4, pady=3, background="#FFDADA", font=100,
           command=lambda: call_num(7)).grid(row=2, column=0)
    Button(root, text="8", width=4, pady=3, background="#FFDADA", font=100,
           command=lambda: call_num(8)).grid(row=2, column=1)
    Button(root, text="9", width=4, pady=3, background="#FFDADA", font=100,
           command=lambda: call_num(9)).grid(row=2, column=2)
    Button(root, text="0", width=4, pady=3, background="#FFF6F6", font=100,
           command=lambda: call_num(0)).grid(row=5, column=0)

    Button(root, text="=", width=4, pady=21, background="#D4E2E6", font=100,
           command=equal_to).grid(row=2, column=3, rowspan=2)
    Button(root, text="+", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: do_math_2_nos("add")).grid(row=5, column=2)
    Button(root, text="AC", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: clear("full")).grid(row=5, column=3)
    Button(root, text="•", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: call_num(".")).grid(row=5, column=1)
    Button(root, text="←", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: clear("last")).grid(row=4, column=3)

    Button(root, text="/", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: do_math_2_nos("divide")).grid(row=6, column=0)
    Button(root, text="*", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: do_math_2_nos("multiply")).grid(row=6, column=1)
    Button(root, text="―", width=4, pady=3, background="#D4E2E6", font=100,
           command=lambda: do_math_2_nos("subtract")).grid(row=6, column=2)
    Button(root, text="more", width=4, pady=3, background="#D4E2E6", font=100,
           command=second_body).grid(row=6, column=3)


root = Tk()
root.title("My Calculator")

entry = Entry(root, width=32)
entry.grid(row=0, column=0, columnspan=5)

Label(root, text="").grid(row=1, column=0)

math = "none"

main_body()
root.mainloop()
