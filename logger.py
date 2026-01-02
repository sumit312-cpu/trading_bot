import logging

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

def log(message):
    print(message)
    logging.info(message)

def log_error(message):
    print("ERROR:", message)
    logging.error(message)