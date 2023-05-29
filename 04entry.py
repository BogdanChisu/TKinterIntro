from tkinter import *

root = Tk()

e = Entry(root, borderwidth=5, bg='cyan', fg='red')
e.pack()
e.get()

def clickMe():
    myLabel = Label(root, text = 'Hello, ' + e.get() + '!', bg='grey', fg='yellow')
    myLabel.pack()

myButton = Button(root, text='Enter your name', padx=10, pady=10, fg='black', bg='yellow', command=clickMe)
myButton.pack()

root.mainloop()