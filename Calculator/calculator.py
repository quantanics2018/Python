from tkinter import *
from math import factorial, pi

root = Tk()
root.title('DataFlair - Calculator')
root.geometry('400x600')  # Set a fixed window size

# Font settings for a larger display and buttons
display_font = ('Arial', 20)
button_font = ('Arial', 15)

# Adding the input field with a larger font
display = Entry(root, font=display_font, borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=5, sticky=N+E+W, padx=10, pady=10)

# Define a button creation function to avoid repetition
def create_button(text, row, col, command, rowspan=1, colspan=1):
    button = Button(root, text=text, font=button_font, command=command, height=2, width=5)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky=N+S+E+W, padx=5, pady=5)

# Adding number buttons
create_button("1", 1, 0, lambda: get_variables(1))
create_button("2", 1, 1, lambda: get_variables(2))
create_button("3", 1, 2, lambda: get_variables(3))
create_button("4", 2, 0, lambda: get_variables(4))
create_button("5", 2, 1, lambda: get_variables(5))
create_button("6", 2, 2, lambda: get_variables(6))
create_button("7", 3, 0, lambda: get_variables(7))
create_button("8", 3, 1, lambda: get_variables(8))
create_button("9", 3, 2, lambda: get_variables(9))
create_button("0", 4, 1, lambda: get_variables(0))

# Adding operation buttons
create_button("+", 1, 3, lambda: get_operation("+"))
create_button("-", 2, 3, lambda: get_operation("-"))
create_button("*", 3, 3, lambda: get_operation("*"))
create_button("/", 4, 3, lambda: get_operation("/"))
create_button("pi", 1, 4, lambda: get_operation(str(pi)))
create_button("%", 2, 4, lambda: get_operation("%"))
create_button("(", 3, 4, lambda: get_operation("("))
create_button(")", 4, 4, lambda: get_operation(")"))
create_button("exp", 1, 5, lambda: get_operation("**"))
create_button("^2", 2, 5, lambda: get_operation("**2"))
create_button("x!", 3, 5, lambda: fact())
create_button(".", 4, 2, lambda: get_variables("."))
create_button("AC", 4, 0, lambda: clear_all())
create_button("<-", 4, 5, lambda: undo())

# Adding equal button which spans two columns
create_button("=", 5, 0, lambda: calculate(), rowspan=1, colspan=6)

# Keep track of current position in the input field
i = 0

# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    global i
    display.delete(0, END)
    i = 0

def undo():
    global i
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
        i = len(new_string)
    else:
        clear_all()
        display.insert(0, "Error")
        i = 0

def calculate():
    global i
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
        i = len(str(result))
    except Exception:
        clear_all()
        display.insert(0, "Error")
        i = 0

def fact():
    global i
    entire_string = display.get()
    try:
        num = int(entire_string)
        result = factorial(num)
        clear_all()
        display.insert(0, result)
        i = len(str(result))
    except Exception:
        clear_all()
        display.insert(0, "Error")
        i = 0

root.mainloop()
