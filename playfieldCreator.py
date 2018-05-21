# !/usr/bin/python3
from tkinter import filedialog
from tkinter import *

import tkinter

root = Tk()

def cb(array, text):
    text.delete('1.0',END)
    text.insert(INSERT, "LEFTPF0\n\t.byte ")
    for i in range(len(array)):
        PF0 = 0
        for j in range(len(array[i])):
            if j < 4:
                PF0 = PF0 | (array[i][j].get() << (4 + j))
        text.insert(INSERT, "$%X" % PF0)
        if i < len(array) - 1:
            text.insert(INSERT, ",")
        else:
            text.insert(INSERT, "\n")

    text.insert(INSERT, "LEFTPF1\n\t.byte ")
    for i in range(len(array)):
        PF1 = 0
        for j in range(len(array[i])):
            if j >= 4 and j < 12:
                PF1 = PF1 | (array[i][j].get() << (7 - (j - 4)))
        text.insert(INSERT, "$%X" % PF1)
        if i < len(array) - 1:
            text.insert(INSERT, ",")
        else:
            text.insert(INSERT, "\n")

    text.insert(INSERT, "LEFTPF2\n\t.byte ")
    for i in range(len(array)):
        PF2 = 0
        for j in range(len(array[i])):
            if j >= 12 and j < 20:
                PF2 = PF2 | (array[i][j].get() << (j - 12))
        text.insert(INSERT, "$%X" % PF2)
        if i < len(array) - 1:
            text.insert(INSERT, ",")
        else:
            text.insert(INSERT, "\n")

img = PhotoImage(width=1, height=1)
scaling = 5 
ht = 1*scaling
wt = 7*scaling
height = 50
width = 20

text = Text(root)

checks=[[0 for j in range(width)] for i in range(height)]

# Create the matrix of checkboxes
for i in range(len(checks)):
    for j in range(len(checks[i])):
        checks[i][j] = IntVar()
        chk = Checkbutton(root, highlightcolor="#D3D3D3", selectcolor="black", indicatoron=False, variable = checks[i][j], \
                         onvalue = 1, offvalue = 0, height=ht, \
                         width = wt, image = img, command=lambda : cb(checks,text))
        chk.grid(row=i, column=j)

text.grid(row=height, columnspan=width)

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# display the menu
root.config(menu=menubar)

root.mainloop()
