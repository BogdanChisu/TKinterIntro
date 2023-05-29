from tkinter import *
from PIL import Image, ImageTk

root = Tk()
im = ImageTk.PhotoImage(Image.open('icons/computer.png'))
root.wm_iconphoto(True, im)

def open():
    global my_img
    top = Toplevel()
    top.title('My second window')
    im2 = ImageTk.PhotoImage(Image.open('icons/drum.ico'))
    top.wm_iconphoto(True, im2)

    lbl = Label(top, text="Hello, World!").pack()
    my_img = ImageTk.PhotoImage(Image.open('images/pic04.jpeg'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text = "Open second window", command=open).pack()
btn3 = Button(root, text = "Exit program", command=root.quit).pack()

root.mainloop()