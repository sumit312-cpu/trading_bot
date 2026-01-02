#  Binance Testnet Trading Bot :-

This project is a simple **Automated Trading Bot** built using Python for the **Binance Spot Test Network**.  
It connects to the Binance Testnet, fetches wallet balances, places test BUY/SELL orders, and stores executed trades in a log file.

This project is created as part of an **assignment / backend-style trading test project**.

---

##  Features

-  Connects to Binance Testnet API  
-  Loads API keys securely using `.env` file  
-  Fetches account balance  
-  Places **test BUY & SELL market orders**  
-  Saves trade history inside `orders.log`  
-  Clean & modular Python code structure  

---

##  Project Structure :-
trading_bot/
├── bot.py
├── main.py
├── orders.py
├── utils.py
├── logger.py
├── orders.log
├── .env.example
├── .gitignore
└── venv/

##  Environment Variables (`.env`) :-

Create a `.env` file in the project root:
API_KEY=YOUR_BINANCE_TESTNET_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET
BASE_URL=https://testnet.binance.vision


 NOTE:  
`.env` is **not uploaded to GitHub** for security reasons.  
Instead `.env.example` is provided.

---

## ▶️ How to Run

### 1️⃣ Install dependencies
pip install python-binance python-dotenv
### 2️⃣ Run account balance script
python main.py

### 3️⃣ Run trading bot (places test BUY + SELL order)
python bot.py

## Order Logs :-

Executed trade records are saved in:
orders.log
Example Entry:
2026-01-02 18:35:55 | { "symbol": "BTCUSDT", "status": "FILLED", "side": "BUY" }


---

##  Screenshots :-
- Project structure  
- Balance output  
- Order execution  
- orders.log file
-  bot.py
- main.py
 
##  Env :-

---

##  Tech Stack :-

- Python  
- Binance API (Testnet)  
- Dotenv  
- Logging System  

---

##  Purpose of Project :-

This project demonstrates:

- API integration  
- Trading automation basics  
- Logging & backend logic  
- Clean Python project structure  

---

## Credits :-

Developed by **Sumit Tiwari**  





