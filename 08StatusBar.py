from tkinter import *
from PIL import Image, ImageTk

root = Tk()
icon_pic = ImageTk.PhotoImage(Image.open('icons/computer.png'))
root.wm_iconphoto(True, icon_pic)

my_image1 = ImageTk.PhotoImage(Image.open('images/pic01.jpeg'))
my_image2 = ImageTk.PhotoImage(Image.open('images/pic02.jpeg'))
my_image3 = ImageTk.PhotoImage(Image.open('images/pic03.jpeg'))
my_image4 = ImageTk.PhotoImage(Image.open('images/pic04.jpeg'))
my_image5 = ImageTk.PhotoImage(Image.open('images/pic05.jpeg'))
my_image6 = ImageTk.PhotoImage(Image.open('images/pic06.jpeg'))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6]

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

# -------------------------------------------------------------------
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
# -------------------------------------------------------------------

def forward(my_number):
    global button_forward
    global button_back
    global my_label

    my_label.grid_forget()
    my_label = Label(image=image_list[my_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(my_number+1))
    button_back = Button(root, text='<<', command=lambda: back(my_number-1))

    if my_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
#---------------------------------------
    status = Label(root, text="Image " + str(my_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
#---------------------------------------

def back(my_number):
    global button_forward
    global button_back
    global my_label

    my_label.grid_forget()
    my_label = Label(image=image_list[my_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(my_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(my_number - 1))

    if my_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    # ---------------------------------------
    status = Label(root, text="Image " + str(my_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    # ---------------------------------------

button_back = Button(root, text="<<", command=lambda: back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()