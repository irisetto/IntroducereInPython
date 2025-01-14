import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

def get_currencies():
    while True:
        response = requests.get("https://www.bnr.ro/nbrfxrates.xml")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml-xml')
            currencies = soup.find_all('Rate')
            currency_rates = {}
            for currency in currencies:
                currency_name = currency.get('currency')
                currency_value = currency.text
                currency_rates[currency_name] = currency_value

            currency_rates['RON'] = 1.0
            currency_rates = dict(sorted(currency_rates.items()))

            return currency_rates
        else:
            time.sleep(5)

def convert_currency(amount, from_currency, to_currency, currency_rates):
    amount_in_ron = amount * float(currency_rates[from_currency])
   
    amount_in_output_currency = amount_in_ron / float(currency_rates[to_currency])

    return round(amount_in_output_currency, 3)

def center_window(root):
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.update_idletasks()


def graphics(currencies):
    root = Tk()
    center_window(root)
    root.title("Convertor valutar")
    window = ttk.Frame(master=root, padding="3 3 12 12", width=600, height=400)
    window.pack(expand=True)
    style = ttk.Style()
    style.configure('My.TButton', font=('Candara', 15))

    window.grid_columnconfigure([1,2,3], weight=1, minsize=100)
    window.grid_rowconfigure([1,2,3], weight=1, minsize=70)

    amount_label = ttk.Label(window, text="From: ", font=("Candara", 15))
    amount_label.grid(column=1, row=1, sticky=E ,padx=5)
    amount = StringVar(window)
    amount_input = ttk.Entry(window, width=7, textvariable=amount, font=("Candara", 15))
    amount_input.grid(column=2, row=1, sticky=(W, E))

    from_currency = StringVar(window)
    from_currency.set(list(currencies.keys())[0])

    dropdown_from_currency = ttk.Combobox(window, textvariable=from_currency, values=list(currencies.keys()), height=5, font=('Candara', 15), justify='center', state='readonly', width=10)
    dropdown_from_currency.grid(column=3, row=1, sticky=(W,E), padx=5)

    to_currency = StringVar(window)
    to_currency.set(list(currencies.keys())[0])

    to_label = ttk.Label(window, text="To: ", font=("Candara", 15))
    to_label.grid(column=1, row=2, sticky=E ,padx=5)
    dropdown_to_currency = ttk.Combobox(window, textvariable=to_currency, values=list(currencies.keys()), height=5, font=('Candara', 15), justify='center',state='readonly', width=10)
    dropdown_to_currency.grid(column=3, row=2, sticky=(W, E), padx=5)

    result_label = ttk.Label(window, text="", font=("Candara", 15))
    result_label.grid(column=2, row=2, sticky=(W,E))

    def swap_currencies():
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        from_currency.set(to_curr)
        to_currency.set(from_curr)

    swap_button = ttk.Button(window, text="↔", command=swap_currencies)
    swap_button.grid(column=3, row=3)

    def calculate_and_display():
        try:
            amount = float(amount_input.get())
        except ValueError:
            result_label.config(text="Invalid amount")
            return
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result = convert_currency(amount, from_curr, to_curr, currencies)
        result_label.config(text=str(result))


    calculate_button = ttk.Button(window, text="Calculate", command=calculate_and_display, style='My.TButton')
    calculate_button.grid(column=2, row=3, sticky=(W,E))

    root.mainloop()

def main():
    try:
        currencies= get_currencies()
        graphics(currencies)
        
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()