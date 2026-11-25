import pandas as pd
from pathlib import Path

# Set folder path to the directory 
folder = Path(__file__).parent

#  Load and clean orders data
orders = pd.read_csv(folder / "orders.csv")
orders = orders.drop_duplicates()
orders["amount"] = orders["amount"].fillna(orders["amount"].median()).astype(int)
orders["order_id"] = orders["order_id"].astype(str)

#  Load customers data
customers = pd.read_csv(folder / "customers.csv")

#  Inner Join: Keep only matching records in both tables
inner = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)
print("inner join row:", len(inner), "(customer 104 dropped)")

#  Left Join: Find customers who have no orders
left = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)
no_orders = left[left["order_id"].isna()]["name"]
print("No orders:", ",".join(no_orders))

# Outer Join: Find orders without a matching customer
outer = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="outer"
)
no_customer = outer[outer["name"].isna()]["customer_id"]
print(
    "order without customer:customer_id",
    ",".join(str(i) for i in no_customer)
)