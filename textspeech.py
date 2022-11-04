import pyttsx3
from tkinter import *

root = Tk()


myLabel = Label(root,text='Enter the Text you want to convert in speech ',pady=(15)).pack()

e = Entry(root)
e.pack()

def fun1(speak):
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()    
myBtn = Button(root,text='CONVERT', command=lambda : fun1(e.get())).pack(pady=15)




root.mainloop()









