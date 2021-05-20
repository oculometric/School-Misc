from tkinter import *
import random

pre = Tk()

but = Button (pre, text="Hell", command=pre.destroy)
but.pack()
but.master.minsize(200, 200)
pre.title ("Hell")
pre.mainloop()


arr = ["apple", "banana", "crayon"]
arr2 = ["black", "blue", "white", "red", "green"]

while True:
    root = Tk()
    lbl1 = Label (root, text='Hello World!')
    lbl1.pack()
    root.geometry ("{0}x{1}+{2}+{3}".format(10*random.randint (1, 100), 10*random.randint (1, 100), 10*random.randint (1, 100), 10*random.randint (1, 100)))
    root.focus_force()
    root.title (arr[random.randint (0,2)])
    root.configure (background=arr2[random.randint(0,4)])
    root.update_idletasks()
    root.update()
