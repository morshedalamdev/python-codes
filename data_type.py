import pandas as pd

sales = {"user_id": ["KM37", "PR19", "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

sales_df = pd.DataFrame(sales)
print(sales_df)