from main import client
from orders import place_test_order, place_sell_order
from utils import timestamp
from logger import log

def run_bot():
    log("Bot Started at " + timestamp())

    order = place_test_order(client)
    log(f"BUY Order Executed: {order}")

    sell = place_sell_order(client)
    log(f"SELL Order Executed: {sell}")

if __name__ == "__main__":
    run_bot()