stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2800,
    "HDFCBANK": 1600,
    "ICICIBANK": 950
}
portfolio = []
def add_stock():
    symbol = input("Enter stock symbol: ").upper()
    if symbol not in stock_prices:
        print("Stock not found in price list!\n")
        return
    quantity = float(input("Enter quantity: "))
    stock = {
        "symbol": symbol,
        "quantity": quantity,
        "price": stock_prices[symbol]
    }
    portfolio.append(stock)
    print(f"{symbol} added successfully at price {stock_prices[symbol]}!\n")
def calculate_total():
    total = 0
    print("\n--- Portfolio Summary ---")
    for stock in portfolio:
        value = stock["quantity"] * stock["price"]
        total += value
        print(f"{stock['symbol']}: {stock['quantity']} × {stock['price']} = {value}")
    print(f"\nTotal Investment Value: {total}\n")
def show_available_stocks():
    print("\nAvailable Stocks:")
    for symbol, price in stock_prices.items():
        print(f"{symbol}: {price}")
    print()
def main():
    while True:
        print("1. Show Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_available_stocks()
        elif choice == "2":
            add_stock()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")
if __name__ == "__main__":
    main()