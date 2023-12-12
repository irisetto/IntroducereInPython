import requests
from bs4 import BeautifulSoup

def get_currencies():
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
    
def convert_currency(amount, from_currency, to_currency, currency_rates):
    amount_in_ron = amount * float(currency_rates[from_currency])
   
    amount_in_output_currency = amount_in_ron / float(currency_rates[to_currency])

    return round(amount_in_output_currency, 3)

def main():
    currency_rates = get_currencies()
    amount = (float)(input("Enter amount: "))
    from_currency = input("Enter from currency: ")
    to_currency = input("Enter to currency: ")
    amount_transformed= convert_currency(amount, from_currency.upper(), to_currency.upper(), currency_rates)
    print(amount_transformed)


if __name__ == "__main__":
    main()