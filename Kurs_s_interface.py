import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {code} за 1 единицу.')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')



w = Tk()
w.title('Курсы обмена валюты')
w.geometry('360x180')

Label(text = 'Выберите код валюты').pack(pady = 10, padx = 10)

curs = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'AED', 'CHF', 'CAD']
combobox = ttk.Combobox(values = curs)
combobox.pack(pady =10, padx = 10)

# entry = Entry()
# entry.pack(pady = 10, padx = 10)

Button(text = 'Получить курс обмена валюты', command = exchange).pack(pady = 10, padx = 10)

w.mainloop()
