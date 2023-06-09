# This script calls an API using the requests library and formats json response using the json library

import requests
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press ⌘F8 to toggle the breakpoint.


def conv(fromCCY, toCCY, amount):
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = json.loads(response.text)

    rates = data["rates"]

    FrCCY2EUR = rates[fromCCY]
    ToCCY2EUR = rates[toCCY]

    ToCCY2FrCCY = ToCCY2EUR / FrCCY2EUR

    Amt = int(amount) * ToCCY2FrCCY

    return Amt

""" Commented out the old function that used the 250 per month API, use the above version of conv function with free API
def conv(fromCCY, toCCY, amount):

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={toCCY}&from={fromCCY}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "KM9HI1yPfEVjXlMmdhyIVUoJfmRbw3cs"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    #print_hi(status_code)
    #print_hi(result)

    jresult = json.loads(result)
    return jresult["result"]
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    FrAmt = input('Amount: ')
    FrCCY = input('from CCY: ')
    ToCCY = input('To CCY: ')

    ToAmt = conv(FrCCY, ToCCY, str(FrAmt))

    print(f'{FrAmt} {FrCCY} is {ToAmt} {ToCCY}')

