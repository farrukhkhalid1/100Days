from tkinter import *

def button_clicked():
    new_text = entry.get()
    miles_into_km = round(float(new_text)*1.609)
    my_label4.config(text=miles_into_km)

window = Tk()
window.title("Mile to km Converter")
#window.minsize(width=300,height=200)
window.config(padx=10,pady=10)

my_label1 = Label(text= "is equal to ")
my_label1.grid(column = 0,row = 1 )

my_label2 = Label(text= "Miles ")
my_label2.grid(column = 2,row = 0 )

my_label3 = Label(text= "Km ")
my_label3.grid(column = 2,row = 1 )

my_label4 = Label()
my_label4.grid(column = 1,row = 1 )

entry = Entry(width = 8)
entry.grid(column = 1,row = 0)

button = Button(text= "Calculate",command = button_clicked)
button.grid(column=1, row=2)


window.mainloop()


