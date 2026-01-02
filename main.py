from dotenv import load_dotenv
load_dotenv()
print("Bot statted...")
import os 
print("API Key Loaded:",
      os.getenv("API_kEY"))

from binance.client import Client

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
base_url = os.getenv("BASE_URL")

client = Client(api_key, api_secret)
client.API_URL = base_url   # force testnet URL

account = client.get_account()
print("Connected to Binance Testnet")
print("Balances:")
for asset in account['balances']:
    if float(asset['free']) > 0:
        print(asset['asset'], asset['free'])


from orders import place_test_order
print("\nPlacing Test Order...")
order = place_test_order(client)
print("Order Executed:")
print(order)