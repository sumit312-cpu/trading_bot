def place_test_order(client):

  import time
  server_time = client.get_server_time()['serverTime']
  local_time = int(time.time() * 1000)
  client.timestamp_offset = server_time - local_time


  order = client.create_order(
            symbol="BTCUSDT",
            side="BUY",
            type="MARKET",
            quantity=0.001
  )
  save_order_log(order)
  return order

import time

def run_trading_bot():
    while True:
        ticker = client.get_symbol_ticker(symbol="BTCUSDT")
        price = float(ticker["price"])
        print("Current Price:", price)

        # Simple Strategy Example
        if price < 60000:
            print("Price low — Buying...")
            order = place_test_order(client)
            save_order_log(order)

        elif price > 62000:
            print("Price high — Selling...")
            order = place_sell_order(client)
            save_order_log(order)

        time.sleep(10)  # wait 10 sec before next cycle
        run_trading_bot()

import json
from datetime import datetime

def save_order_log(order):
    with open("orders.log", "a") as f:
        f.write(
            f"{datetime.now()} | {json.dumps(order)}\n"
        )


def place_sell_order(client):
    order = client.create_order(
        symbol="BTCUSDT",
        side="SELL",
        type="MARKET",
        quantity=0.001
    )

    save_order_log(order)
    return order