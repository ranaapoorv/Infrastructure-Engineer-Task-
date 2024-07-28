# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:30:56 2024

@author: ranaa
"""

import pandas as pd

# Step 2: Read the CSV file
df = pd.read_csv("D:\Project\orders.csv")

# Step 3: Calculate revenue for each row
df['revenue'] = df['product_price'] * df['quantity']

# Task 1: Total revenue per month
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')
revenue_per_month = df.groupby('month')['revenue'].sum().reset_index()
print("Total revenue per month:")
print(revenue_per_month)

# Task 2: Total revenue per product
revenue_per_product = df.groupby('product_name')['revenue'].sum().reset_index()
print("\nTotal revenue per product:")
print(revenue_per_product)

# Task 3: Total revenue per customer
revenue_per_customer = df.groupby('customer_id')['revenue'].sum().reset_index()
print("\nTotal revenue per customer:")
print(revenue_per_customer)

# Task 4: Top 10 customers by revenue
top_customers = revenue_per_customer.sort_values(by='revenue', ascending=False).head(10)
print("\nTop 10 customers by revenue:")
print(top_customers)