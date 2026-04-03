"""
MODULE 1:: Upload the CSV file and read it into a DataFrame
"""

# Import required packages/libraries
import pandas as pd
import requests

# Read the CSV file into a DataFrame
orders = pd.read_csv("data/orders-2024-01-21.csv")
orders.head()
print(orders)


"""
MODULE 2:: Find the exchange rates for the date of the orders (2024-01-21) using an API
"""
url = "https://api.vatcomply.com/rates?base=USD&date=2024-01-21"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rates = data["rates"]
else:
    print(f"Error: {response.status_code}")
    exit()

print(rates)


"""
MODULE 3:: Calculate the amount in USD for each order
"""
orders["exchange_rate"] = orders["currency"].map(rates)
orders["amount_usd"] = round(orders["amount"] * orders["exchange_rate"], 2)
print(orders)


"""
MODULE 4:: Calculate the total sales in USD
"""
total_usd_sales = orders["amount_usd"].sum()

print(orders)
print(f"\nTotal USD Sales: ${total_usd_sales:,.2f}")
