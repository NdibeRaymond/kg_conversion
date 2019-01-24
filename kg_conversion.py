from tkinter import *
window = Tk()
def convert():
    value_to_convert = float(entry.get())
    gram_value = str(value_to_convert*1000)
    pound_value = str(value_to_convert*2.20462)
    ounce_value = str(value_to_convert*35.274)

    txt.delete(1.0,END)
    txt1.delete(1.0,END)
    txt2.delete(1.0,END)
    #result = "gram: "+str(gram_value)+"; pound: "+str(pound_value)+"; ounce: "+str(ounce_value)
    txt.insert(END,gram_value)

    txt1.insert(END,pound_value)

    txt2.insert(END,ounce_value)

e1=Label(window,text="Kg:",width = 3)
e1.grid(row = 0, column = 1)

e2=Label(window,text="Gram:",width = 10)
e2.grid(row = 1, column = 0)

e3=Label(window,text="Pound:",width = 10)
e3.grid(row = 2, column = 0)

e4=Label(window,text="Ounce:",width = 10)
e4.grid(row = 3, column = 0)

but = Button(window,text = "convert",command = convert)
but.grid(row = 0,column = 0)

entry = StringVar()
ent = Entry(window,textvariable = entry,width = 20)
ent.grid(row = 0, column = 2)

txt = Text(window,height = 1,width = 20)
txt.grid(row = 1,column = 1,columnspan = 2)

txt1 = Text(window,height = 1, width = 20)
txt1.grid(row = 2,column = 1,columnspan = 2)

txt2 = Text(window,height = 1, width = 20 )
txt2.grid(row = 3,column = 1, columnspan = 2)


window.mainloop()
