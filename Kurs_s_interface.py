import requests
import json
from tkinter import *
from tkinter import messagebox as mb



w = Tk()
w.title('Курсы обмена валюты')
w.geometry('360x180')

Label(text = 'Введите код валюты').pack(pady = 10, padx = 10)

entry = Entry()
entry.pack(pady = 10, padx = 10)

Button(text = 'Получить курс обмена валюты', command = exchange).pack(pady = 10, padx = 10)

w.mainloop()
