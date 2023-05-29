from tkinter import *
from PIL import Image, ImageTk

root = Tk()

im1 = Image.open('icons/cycle-counting.png')
photo1 = ImageTk.PhotoImage(im1)
root.wm_iconphoto(True, photo1)

im2 = Image.open('icons/drum.ico')
photo2 = ImageTk.PhotoImage(im2)
myLabel = Label(image=photo2).pack()

button_quit = Button(root, text = 'Exit the program', command = root.quit).pack()

root.mainloop()