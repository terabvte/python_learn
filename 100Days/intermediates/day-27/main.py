import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=800, height=600)

# Label

label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
label.pack(side="right")






window.mainloop()
