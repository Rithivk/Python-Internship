import requests

def get_exchange_rate(base_currency, target_currency):
    API_KEY = 'YOUR_API_KEY_HERE'  # Get your API key from exchangeratesapi.io
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {'symbols': target_currency, 'apikey': API_KEY}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(target_currency)
    else:
        return None

def currency_converter():
    print("Welcome to Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, etc.")

    base_currency = input("Enter the source currency code: ").upper()
    target_currency = input("Enter the target currency code: ").upper()

    amount = input("Enter the amount to convert: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is None:
        print("Failed to fetch exchange rates. Please try again later.")
        return

    converted_amount = amount * exchange_rate

    print(f"{amount} {base_currency} equals {converted_amount} {target_currency}")
    print(f"Exchange rate: 1 {base_currency} = {exchange_rate} {target_currency}")

if __name__ == "__main__":
    currency_converter()