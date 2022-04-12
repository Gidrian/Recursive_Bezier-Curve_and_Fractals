import tkinter as tk
from tkinter import *
from tkinter import CENTER, StringVar, ttk
from turtle import *
import turtle

root = tk.Tk()
root.geometry('1280x1000')
root.resizable(False, False)
root.title('Fractals')
canvas = tk.Canvas(root, bg = "pink",height=850, width=1280)  
canvas.place(relx=0.5, rely=0.45, anchor=CENTER)
screen = turtle.TurtleScreen(canvas)
skk =  turtle.RawTurtle(screen)


# We initialize the number of levels and the numbeer of sides
number = 3
level = 0

# Next 4 functions are for the buttons of the GUI
def on_click_number_aug():
    global level
    global number
    if (number < 6 ):
        number = number + 1
        number_label["text"] = number
        n_sus["state"] = "active"
        call_fractal(number , level)
    if (number == 6):
        n_aug["state"] = "disabled"
   
def on_click_number_dis():
    global level
    global number
    if (number > 3):
        number = number - 1
        number_label["text"] = number
        n_aug["state"] = "active"
        call_fractal(number , level)
    if (number == 3):
        n_sus["state"] = "disabled"
    
def on_click_level_aug():
    global level
    global number
    if (level < 6):
        level = level + 1
        level_label["text"] = level
        l_sus["state"] = "active"
        call_fractal(number , level)
    if (level == 6):
        l_aug["state"] = "disabled"
    
def on_click_level_dis():
    global level
    global number
    if (level > 0):
        level = level - 1
        level_label["text"] = level
        l_aug["state"] = "active"
        call_fractal(number , level)
    if (level == 0):
        l_sus["state"] = "disabled"
    
    
# This function is called when the user clicks on the buttons
# Its purpose is to setup the environment and varibales for the fractal
def call_fractal(number , level):
    n_aug["state"] = "disabled"
    l_aug["state"] = "disabled"
    n_sus["state"] = "disabled"
    l_sus["state"] = "disabled"
    x1,x2= 200,1100
    length = x2 - x1
    skk.penup()
    skk.goto(-400,-350)
    skk.pendown()
    skk.clear()
    skk.speed(0)
    screen.tracer(0)
    if (number == 3):
        fractal3(length, level)
    if (number == 4):
        fractal4(length, level)
    if (number == 5):
        fractal5(length, level)
    if (number == 6):
        fractal6(length, level)
    screen.update() 
    n_aug["state"] = "active"
    l_aug["state"] = "active"
    n_sus["state"] = "active"
    l_sus["state"] = "active"


# Next 4 functions draw the fractals depending on the number of sides
def fractal3(lengthSide, levels):
    if levels == 0:
        skk.forward(lengthSide)
        return
    lengthSide /= 3.0
    fractal3(lengthSide, levels-1)
    skk.left(60)
    fractal3(lengthSide, levels-1)
    skk.right(120)
    fractal3(lengthSide, levels-1)
    skk.left(60)
    fractal3(lengthSide, levels-1)
    
def fractal4(lengthSide, levels):
    if levels == 0:
        skk.forward(lengthSide)
        return
    lengthSide /= 3.0
    fractal4(lengthSide, levels-1)
    skk.left(90)
    fractal4(lengthSide, levels-1)
    skk.right(90)
    fractal4(lengthSide, levels-1)
    skk.right(90)
    fractal4(lengthSide, levels-1)
    skk.left(90)
    fractal4(lengthSide, levels-1)
    
def fractal5(lengthSide, levels):
    if levels == 0:
        skk.forward(lengthSide)
        return
    lengthSide /= 3.0
    fractal5(lengthSide, levels-1)
    skk.left(108)
    fractal5(lengthSide, levels-1)
    skk.right(72)
    fractal5(lengthSide, levels-1)
    skk.right(72)
    fractal5(lengthSide, levels-1)
    skk.right(72)
    fractal5(lengthSide, levels-1)
    skk.left(108)
    fractal5(lengthSide, levels-1)
    

def fractal6(lengthSide, levels):
    if levels == 0:
        skk.forward(lengthSide)
        return
    lengthSide /= 3.0
    fractal6(lengthSide, levels-1)
    skk.left(120)
    fractal6(lengthSide, levels-1)
    skk.right(60)
    fractal6(lengthSide, levels-1)
    skk.right(60)
    fractal6(lengthSide, levels-1)
    skk.right(60)
    fractal6(lengthSide, levels-1)
    skk.right(60)
    fractal6(lengthSide, levels-1)
    skk.left(120)
    fractal6(lengthSide, levels-1)
    



# number label
number_label = Label(root, text="3",
font=('Calibri 15 bold'))
number_label.place(relx=0.67, rely=0.945, relwidth=0.5, anchor='ne')

# level label
level_label = Label(root, text="0",
font=('Calibri 15 bold'))
level_label.place(relx=1.005, rely=0.945, relwidth=0.5, anchor='ne')


    
# label for the Number slider
slider_label_number = ttk.Label(
    root,
    text='Number:'
)
slider_label_number.place(relx=0.7, rely=0.9, relwidth=0.5, anchor='ne')

# label for the Level slider
slider_label_level = ttk.Label(
    root,
    text='Level:'
)
slider_label_level.place(relx=1.05, rely=0.9, relwidth=0.5, anchor='ne')

#  button number
n_aug = Button(root, text="+", command=on_click_number_aug)
n_aug.place(relx=0.51, rely=0.88, relwidth=0.25, anchor='ne')

n_sus = Button(root, text="-", command=on_click_number_dis)
n_sus.place(relx=0.51, rely=0.92, relwidth=0.25, anchor='ne')


#  button level
l_aug = Button(root, text="+", command=on_click_level_aug)
l_aug.place(relx=0.85, rely=0.88, relwidth=0.25, anchor='ne')

l_sus = Button(root, text="-", command=on_click_level_dis)
l_sus.place(relx=0.85, rely=0.92, relwidth=0.25, anchor='ne')


# current value label

current_value_number = ttk.Label(
    root,
    text='Current Value:'
)
current_value_number.place(relx=0.4, rely=0.95, relwidth=0.1, anchor='ne')

current_value_level = ttk.Label(
    root,
    text='Current Value:'
)
current_value_level.place(relx=0.75, rely=0.95, relwidth=0.1, anchor='ne')



call_fractal(number,level)
root.mainloop()