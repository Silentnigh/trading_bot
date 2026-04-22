import argparse
from client import get_client
from utils import place_order
from logger import setup_logger



def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()
    
    

    if args.type == "LIMIT" and not args.price:
        print(" Price required for LIMIT order")
        return

    client = get_client()

    print("Order Summary:")
    print(vars(args))

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if order:
        print("Order Successful")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
    else:
        print("Order Failed")

if __name__ == "__main__":# constructor
    main()