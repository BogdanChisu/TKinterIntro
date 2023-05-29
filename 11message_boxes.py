from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
im = ImageTk.PhotoImage(Image.open('icons/computer.png'))
#-----------------------------------------------------------------------------
# Types of message boxes:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#-----------------------------------------------------------------------------
root.wm_iconphoto(True, im)

def popup():
    response = messagebox.showinfo("This is my popup", "Hello, World!")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="You clicked Yes").pack()
    # else:
    #     Label(root, text="You clicked No").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()