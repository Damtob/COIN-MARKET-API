'''
These lines import the requests module, which is used to make HTTP
requests to APIs, and the json module, which is used to parse JSON data.
'''
import requests
import json

'''
These lines make a GET request to the CoinMarketCap API to retrieve 
information on the latest cryptocurrency listings. The requests.get() method
returns a Response object, which is then passed to the json.loads() method to parse 
the response content as a JSON object. The resulting JSON object is stored in the api 
variable.
'''
api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")
api = json.loads(api_request.content)

#These lines simply print a separator to visually separate the output.
print("----------------")
print("----------------")

'''
This code defines a list of two dictionaries, each representing 
a cryptocurrency owned by the user. The dictionaries contain the symbol 
of the cryptocurrency (symbol), the amount owned (amount_owned), and the
price per coin (price_per_coin).
'''
coins = [
    {
        "symbol": "ETH",
        "amount_owned": 5,
        "price_per_coin": 4200
    },
    {
        "symbol": "EOS",
        "amount_owned": 200,
        "price_per_coin": 8.05
    }
]
#This code initializes a variable to store the total profit or loss of the user's portfolio.
total_pl = 0

'''
These lines iterate over the first 5 cryptocurrency listings in the
 api object and compare the symbols to the symbols in the coins list. 
For each matching symbol, it calculates the total amount paid for the
cryptocurrency (total_paid), the current value of the cryptocurrency 
(current_value), the profit or loss per coin (pl_percoin), and the total
profit or loss for the coin (total_pl_coin). It also adds the total profit
or loss for the coin to the overall portfolio profit or loss (total_pl). 
Finally, it prints out information about the cryptocurrency, including its name,
price, amount owned, total amount paid, current value, profit or loss per
'''
for i in range(0, 4):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_percoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin

            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print("Price - ${0:.3f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number Of Coin:", coin["amount_owned"])
            print("Total Amount Paid:", "${0:.3f}".format(total_paid))
            print("Current Value:", "${0:.3f}".format(current_value))
            print("P/L Per Coin:", "${0:.3f}".format(pl_percoin))
            print("Total P/L With Coin:", "${0:.3f}".format(total_pl_coin))
            print("----------------")

print("Total P/L For Portfolio:", "${0:.3f}".format(total_pl))