from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
# label.pack(side="right")
label.grid(column=0, row=0)
label.config(text="New Text")
# label.pack(side="top")

# Button
def button_clicked():
    label.config(text=input.get(), pady=20)


button = Button(text="Clicker")
button.grid(column=1, row=1)


new_button = Button(text="NEWY Clicker")
new_button.grid(column=2, row=0)
# Entry

input = Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()
