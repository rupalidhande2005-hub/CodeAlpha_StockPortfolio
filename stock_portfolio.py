stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

print("Welcome to Stock Portfolio Tracker!")

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("\nStock:", stock_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total_investment)

else:
    print("Sorry, stock is not available.")