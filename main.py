import time
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "BOT RUNNING 24/7"

def trading_bot():
    print("SMART BOT STARTED")
    while True:
        print("Bot checking...")
        time.sleep(60)

if __name__ == "__main__":
    t = threading.Thread(target=trading_bot, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=10000)
