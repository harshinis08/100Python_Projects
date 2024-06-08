import tkinter

window = tkinter.Tk()
window.minsize(width=600, height=300)

window.config(padx=20, pady=100)
window.title("Mile to Km Converter")


def mile_to_Km_Converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


miles_input = tkinter.Entry(width=15)
miles_input.grid(row=0, column=1)

text = tkinter.Label(text="Miles")
text.grid(row=0, column=2)

text2 = tkinter.Label(text="is equal to")
text2.grid(row=1, column=0)

text3 = tkinter.Label(text="Km")
text3.grid(row=1, column=2)

km_result = tkinter.Label(text="0")
km_result.grid(row=1, column=1)

button = tkinter.Button(text="Calculate", command=mile_to_Km_Converter)
button.grid(row=2, column=1)

window.mainloop()
