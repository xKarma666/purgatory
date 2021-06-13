from tkinter import*
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('life clock')

def time():
    string= strftime ('%H:%M:%S:%p')
    label.config (text=string)
    label.after(1000,time)


label=Label (root, font=("", 100) , background= 'yellow', foreground='black')
label.pack(anchor='center')

time()

mainloop()

