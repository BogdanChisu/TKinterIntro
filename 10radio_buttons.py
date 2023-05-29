from tkinter import *
from PIL import Image, ImageTk

root = Tk()

im = ImageTk.PhotoImage(Image.open('icons/computer.png'))
root.wm_iconphoto(True, im)

# kinter variables, not python variable


TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

#---------------------------------------------
for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)
#---------------------------------------------

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

top_label = Label(root, text = "Your selection is: ").pack()

my_button = Button(root, text="Click me!",  command=lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()