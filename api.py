import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = '5c36bb01-2e42-40f5-b0ed-ef57cc2c9f9d'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Set the parameters for the API request
params = {'symbol': 'ETH', 'convert': 'NGN'}


# Set the headers with your API key
headers = {'X-CMC_PRO_API_KEY':  API_KEY}

# Make the API request and parse the response
response = requests.get(URL, params=params, headers=headers)
data = response.json()

# Extract the Ethereum price from the response
price_eth = data['data']['ETH']['quote']['NGN']['price']



# Print the Ethereum price
print(f"The current Ethereum price is N{price_eth:.5f}")
