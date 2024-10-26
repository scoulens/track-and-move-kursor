import pyautogui
from tkinter import *  
  
def clicked():  
    pyautogui.moveTo((int(txt.get()), int(f.get())), duration=0.01)  

def update_label():
    position = pyautogui.position()
    lbl.config(text=f"Position: {position}")
    lbl.after(100, update_label)

window = Tk()  
window.title("MoveKursor")  
window.geometry('400x250')  

lbl = Label(window, text=pyautogui.position())  
lbl.grid(column=0, row=0)  

Label(window, text="X:").grid(column=0, row=1)
txt = Entry(window, width=10)  
txt.grid(column=1, row=1)

Label(window, text="Y:").grid(column=2, row=1)
f = Entry(window, width=10)
f.grid(column=3, row=1)

btn = Button(window, text="Move", command=clicked)  
btn.grid(column=2, row=2)  

update_label()

window.mainloop()





