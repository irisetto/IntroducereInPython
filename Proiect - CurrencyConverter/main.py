import requests
from bs4 import BeautifulSoup

def get_currencies():
    response = requests.get("https://www.bnr.ro/nbrfxrates.xml")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        currencies = soup.find_all('rate')
        currency_rates = {}
        for currency in currencies:
            currency_name = currency.get('currency')
            currency_value = currency.text
            currency_rates[currency_name] = currency_value
        return currency_rates
    
def main():
    currency_rates = get_currencies()
    print(currency_rates)

if __name__ == "__main__":
    main()