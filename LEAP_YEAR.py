from tkinter import *



#creating the root Window
root = Tk()
root.title('LEAP YEAR SYSTEM')
root.geometry('400x200')

#creating the Input Field
label3 = Label(root,text='Enter the Year',pady=10).pack()
myEntry = Entry(root,borderwidth=3)
myEntry.pack(pady=(0,10))


#creating the LEAP YEAR function
def leap(num):
    if(int(num) %4==0):
        label1 = Label(root,text= num+' is leap year')
        label1.pack()
    else:
        label2 = Label(root,text= num+' is not leap year')
        label2.pack()
        
#creating the Button
myButton = Button(root,text='CHECK',command=lambda : leap(myEntry.get()))
myButton.pack()












root.mainloop()




























