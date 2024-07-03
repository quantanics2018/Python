from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15)
length.pack()

pass_str = StringVar()

def Generator():
    length = pass_len.get()
    if length < 4:
        length = 4
        pass_len.set(4)

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]


    if length > 4:
        password += random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=length - 4)
    
    random.shuffle(password)
    pass_str.set(''.join(password))

generate_button = Button(root, text="GENERATE PASSWORD", command=Generator)
generate_button.pack(pady=5)

password_entry = Entry(root, textvariable=pass_str)
password_entry.pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

copy_button = Button(root, text='COPY TO CLIPBOARD', command=Copy_password)
copy_button.pack(pady=5)

root.mainloop()
