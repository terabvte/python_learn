from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=275, height=150)
window.config(padx=10, pady=20)

def mi_to_km(mi):
    return str(round((float(mi) * 1.609344), 4))

def on_button_click():
    converted_label.config(text=mi_to_km(miles_input.get()))

# Total of 6 widgets
# Widget 1: Input box for miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
# W2: "Miles" label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
# W3: "is equal to "label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
# W4: converted value label (this gets auto-updated)
converted_label = Label(text="0")
converted_label.grid(column=1, row=1)
# W5: "Km" label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
# W6: "Calculate" button
calculate_button = Button(text="Calculate", command=on_button_click)
calculate_button.grid(column=1, row=2)

# miles

window.mainloop()
