from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="OMG, you clicked me!")
    myLabel.pack()

myButton = Button(root, text="Click me!", padx=10, pady=10, fg="yellow", bg="black", command=myClick)
myButton.pack()

root.mainloop()
