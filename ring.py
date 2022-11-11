import os
from tkinter import *
from tkinter import ttk

corOn = "#57f542"
corOff = "#f52a14"
janela = Tk()
janela.title("Ring Controller")
janela.geometry("235x318")
number = 0

def Ring(On) :
    global number
    if On == 1 :
        os.system("BlinkStickPower, 100, 100")
        number = 1
        
  
        
    else:
        os.system("BlinkStickPower, 0, 0")
        number = 0 
    
def ControllerRing(e):
    value = slider.get()
    if number == 1:
        
       # os.system("BlinkStickPower, {}, {}" .format(value))
        os.system(f"BlinkStickPower, {value}, {value}")
        print("Ativo")
    else:
       # os.system("BlinkStickPower, 0, 0")
       print("Desativo")



frame_corpo = Frame(janela,width=235, height=318)
frame_corpo.grid(row =0, column=0)

slider = Scale(frame_corpo, command=ControllerRing , from_=0, to=100, orient=HORIZONTAL)
slider.set(50)
slider.place(x=60, y= 0)

b_on = Button(frame_corpo, command=lambda:Ring(1), text = "Ligar", width = 10, height = 2, bg=corOn, fg="#fff", font=('Ivy 13 bold'), relief=RAISED)
b_on.place(x=5, y=100)

b_off = Button(frame_corpo, command=lambda:Ring(0), text = "Desligar", width = 10, height = 2, bg=corOff,fg="#fff", font=('Ivy 13 bold'), relief=RAISED)
b_off.place(x=120, y=100)





        

janela.mainloop()
