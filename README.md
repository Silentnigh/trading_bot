# trading_bot
This for Binance internship assignment

## Overview
This project implements a basic crypto trading system that supports:
- MARKET orders
- LIMIT orders

## Setup Steps

1. Clone the repository:
   git clone https://github.com/your-username/crypto-trading-bot.git
   cd trading-bot

2. Create virtual environment

3. Install dependencies:
   pip install -r requirements.txt

##  How to Run

Run the main script:
python src/main.py

##  Example Usage
### MARKET Order
python src/main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
after the output are showing order summary then log are updated
## output
 Order Successful
Order ID: 13060517188
Status: FILLED
## log generate :
[2026-04-22 10:15:23] ORDER TYPE: MARKET
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001
Price: Market Price
Order ID: 13060517188
Status: FILLED

note:- depend on your order specifiaction

### LIMIT 
python src/main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
this command for limit
## output
Order Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'LIMIT', 'quantity': 0.001, 'price': 30000}

✅ Order Placed
Order ID: 13060517210
Status: NEW
## log generate :
[2026-04-22 10:20:45] ORDER TYPE: LIMIT
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001
Price: 30000
Order ID: 13060517210
Status: NEW
