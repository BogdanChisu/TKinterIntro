from tkinter import *

root = Tk()

myLabel1 = Label(root, text = 'Hello world!').grid(row = 0, column = 0)
myLabel2 = Label(root, text = 'My name is Bogdan Chisu!').grid(row = 1, column = 1)
myLabel3 = Label(root, text = 'Studying Tk I am!').grid(row = 2, column = 2)

root.mainloop()