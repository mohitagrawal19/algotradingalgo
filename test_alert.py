import time

def generate_alert():
    # Example alert message
    alert_message = "ALERT: Stocks to Buy: RELIANCE, HDFCBANK | Stocks to Sell: TCS | Options to Buy: NIFTY 24000 CE | Options to Sell: NIFTY 24000 PE"
    print(alert_message)

if __name__ == "__main__":
    while True:
        generate_alert()
        time.sleep(30)
