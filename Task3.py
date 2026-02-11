prices = {"milk": 2.5, "bread": 1.8, "eggs": 3.2}

try:
    product = input("Enter product name: ")
    print("Price:", prices[product])
except KeyError:
    print("Product not found.")
    print("Available products:", list(prices.keys()))
