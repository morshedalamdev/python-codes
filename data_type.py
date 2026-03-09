import pandas as pd

sales = {"user_id": ["KM37", "PR19", "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

# Read in sales.csv
sales_df = pd.read_csv("data/sales.csv")

# Display the DataFrame info
print("--- DataFrame Info ---")
print(sales_df.info())

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first few rows
print(sales_df.head())