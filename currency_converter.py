import requests
import json
from tkinter import *

'''
to = input('to: ')
from1 = input('from1: ')
amount = input('amount :')
url = "https://api.apilayer.com/fixer/convert?to="+to+"&from="+from1+"&amount="+amount
#payload = {}
headers= {
  "apikey": "NgulYh64NEZmpYwpKi7b22FLxVRa2zu7"
}

response = requests.request("GET", url, headers=headers)

status_code = response.status_code
result = response.text
result1 = json.loads(result)
#print(type(result))
#print(type(result1))
print(result1['result'])
'''


root = Tk()

root.title('Currency Converter')
root.geometry('350x300')

myLabel1 = Label(root,text='From: ') 
myLabel1.grid(row=0,column=0)

Entry1 = Entry(root)
Entry1.grid(row=0,column=1)


myLabel2 = Label(root,text='to: ') 
myLabel2.grid(row=1,column=0)

Entry2 = Entry(root)
Entry2.grid(row=1,column=1)

myLabel3 = Label(root,text='amount: ') 
myLabel3.grid(row=2,column=0)

Entry3 = Entry(root)
Entry3.grid(row=2,column=1)


def convert(from1,to,amount):
    
    url = "https://api.apilayer.com/fixer/convert?to="+to+"&from="+from1+"&amount="+amount
    #payload = {}
    headers= {
      "apikey": "NgulYh64NEZmpYwpKi7b22FLxVRa2zu7"
    }

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    result = response.text
    result1 = json.loads(result)
    #print(type(result))
    #print(type(result1))
    #print(result1['result']) 
    res = result1['result']
    myLabel4 = Label(root,text='result is: '+str(res))
    myLabel4.grid(row=5,column=1)



myBtn1 = Button(root,text='Convert', command=lambda : convert(Entry1.get(),Entry2.get(),Entry3.get()))
myBtn1.grid(row=3,column=1)


root.mainloop()




















