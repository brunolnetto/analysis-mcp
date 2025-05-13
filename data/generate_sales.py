import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Parameters
num_records = 1000
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Sample data
products = [
    {"ProductID": "P001", "ProductName": "Wireless Mouse", "Category": "Electronics", "UnitPrice": 25.99},
    {"ProductID": "P002", "ProductName": "Bluetooth Speaker", "Category": "Electronics", "UnitPrice": 45.50},
    {"ProductID": "P003", "ProductName": "Running Shoes", "Category": "Footwear", "UnitPrice": 60.00},
    {"ProductID": "P004", "ProductName": "Coffee Maker", "Category": "Home Appliances", "UnitPrice": 80.75},
    {"ProductID": "P005", "ProductName": "Desk Lamp", "Category": "Furniture", "UnitPrice": 30.20},
]

stores = [
    {"StoreID": "S001", "StoreName": "Downtown Store", "Region": "North"},
    {"StoreID": "S002", "StoreName": "Uptown Store", "Region": "South"},
    {"StoreID": "S003", "StoreName": "Suburban Store", "Region": "East"},
    {"StoreID": "S004", "StoreName": "Mall Outlet", "Region": "West"},
    {"StoreID": "S005", "StoreName": "Airport Kiosk", "Region": "Central"},
]

# Generate sales data
sales_data = []

for _ in range(num_records):
    product = random.choice(products)
    store = random.choice(stores)
    quantity = random.randint(1, 5)
    sale_date = fake.date_between(start_date=start_date, end_date=end_date)
    customer_id = fake.uuid4()
    customer_name = fake.name()
    revenue = round(product["UnitPrice"] * quantity, 2)

    sales_record = {
        "SaleID": fake.uuid4(),
        "SaleDate": sale_date,
        "StoreID": store["StoreID"],
        "StoreName": store["StoreName"],
        "Region": store["Region"],
        "ProductID": product["ProductID"],
        "ProductName": product["ProductName"],
        "Category": product["Category"],
        "UnitPrice": product["UnitPrice"],
        "Quantity": quantity,
        "Revenue": revenue,
        "CustomerID": customer_id,
        "CustomerName": customer_name,
    }

    sales_data.append(sales_record)

# Create DataFrame
df_sales = pd.DataFrame(sales_data)

# Save to CSV
filename = "data/sales.csv"
df_sales.to_csv(filename, index=False)

print(f"Synthetic sales data generated and saved to '{filename}'.")
