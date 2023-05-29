from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
im = ImageTk.PhotoImage(Image.open('icons/computer.png'))
root.wm_iconphoto(True, im)

def open():
    global my_image
    # --------------------------------------------------------------------------------------------------------------
    root.filename = filedialog.askopenfilename(initialdir='images', title="Select a file",
                                               filetypes=(("jpeg", "*.jpeg"), ("png", "*.png"), ("all files", "*.*")))
    # --------------------------------------------------------------------------------------------------------------
    my_label = Label(root, text=root.filename).grid(row=2, column=0, columnspan=2)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).grid(row=1, column=0, columnspan=2)

my_btn = Button(root, text="Open a file", command=open).grid(row=0, column=0)
quit_btn = Button(root, text="Exit", command=root.quit).grid(row=0, column=1)

root.mainloop()