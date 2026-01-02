from datetime import datetime

def format_price(value):
    return float(f"{float(value):.2f}")

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")