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
                c_curs = curs[code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_curs} за 1 доллар.')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


def restart_c_label(event):
    code = combobox.get()
    name = curs[code]
    c_label.config(text=name)


curs = {
        'RUB': 'Российский рубль',
        'EUR': 'Евро',
        'GBP': 'Британский фунт стерлингов',
        'JPY': 'Японская йена',
        'CNY': 'Китайская йена',
        'KZT': 'Казахский тенге',
        'UZS': 'Узбекский сум',
        'AED': 'Арабский дирхам',
        'CHF': 'Швейцарский франк',
        'CAD': 'Канадский доллар'
}

w = Tk()
w.title('Курсы обмена валюты')
w.geometry('360x180')

Label(text = 'Выберите код валюты').pack(pady = 10, padx = 10)

combobox = ttk.Combobox(values = list(curs.keys()))
combobox.pack(pady =10, padx = 10)
combobox.bind('<<ComboboxSelected>>', restart_c_label)

c_label = ttk.Label()
c_label.pack(pady =10, padx = 10)

Button(text = 'Получить курс обмена валюты', command = exchange).pack(pady = 10, padx = 10)

w.mainloop()
