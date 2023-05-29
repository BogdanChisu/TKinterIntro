from tkinter import *
from PIL import ImageTk, Image

root = Tk()

im = Image.open('icons/computer.png')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)
root.title("Learning about Frames")

frame = LabelFrame(root, text="This is my frame", padx=100, pady=100) # offset inside of the frame
frame.pack(padx=20, pady=20) # offset from the edge of the window

b = Button(frame, text="don't click here!", command=root.quit)
b2 = Button(frame, text="...or here!", command=root.quit)

b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()