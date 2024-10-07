import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_curs = curs[t_code]
                b_curs = curs[b_code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {t_curs} за 1 {b_curs}.')
            else:
                mb.showerror('Ошибка', f'Валюта {t_code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


def restart_c_label(event):
    code = t_combobox.get()
    name = curs[code]
    c_label.config(text=name)


curs = {
        'RUB': 'Российский рубль',
        'EUR': 'Евро',
        'GBP': 'Британский фунт стерлингов',
        'JPY': 'Японская йена',
        'USD': 'Американский доллар',
        'CNY': 'Китайская йена',
        'KZT': 'Казахский тенге',
        'UZS': 'Узбекский сум',
        'AED': 'Арабский дирхам',
        'CHF': 'Швейцарский франк',
        'CAD': 'Канадский доллар'
}

w = Tk()
w.title('Курсы обмена валюты')
w.geometry('360x300')

Label(text = 'Базовая валюта').pack(pady = 10, padx = 10)

b_combobox = ttk.Combobox(values = list(curs.keys()))
b_combobox.pack(pady =10, padx = 10)


Label(text = 'Целевая валюта').pack(pady = 10, padx = 10)

t_combobox = ttk.Combobox(values = list(curs.keys()))
t_combobox.pack(pady =10, padx = 10)
t_combobox.bind('<<ComboboxSelected>>', restart_c_label)

c_label = ttk.Label()
c_label.pack(pady =10, padx = 10)

Button(text = 'Получить курс обмена', command = exchange).pack(pady = 10, padx = 10)

w.mainloop()
