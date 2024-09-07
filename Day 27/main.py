import tkinter
from tkinter import Entry

from PIL.ImageOps import expand

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")    # shows label on the left of screen
my_label.pack()

my_label["text"] = "My text"
my_label.config(text="New text")

# Button

def button_clicked():
    # print("I'm clicked")
    new_text = input.get()
    # my_label.config(text="Button got clicked")
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=15)
input.pack()
print(input.get())


# import turtle
#
# tim = turtle.Turtle()
# tim.write()


window.mainloop()