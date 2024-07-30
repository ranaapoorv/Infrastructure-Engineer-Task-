# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:30:56 2024

@author: ranaa
"""

import os
import pandas as pd

# Define the absolute path to the CSV file
csv_file_path = '/home/kali/Desktop/orders2.csv'

# Check the current working directory
print("Current Working Directory:", os.getcwd())

# Step 1: Read the CSV file
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' does not exist.")
    exit()

# Ensure that the necessary columns are present
required_columns = ['product_price', 'quantity', 'order_date', 'product_name', 'customer_id']
if not all(col in df.columns for col in required_columns):
    print(f"Error: The CSV file must contain the following columns: {', '.join(required_columns)}.")
    exit()

# Step 2: Calculate revenue for each row
df['revenue'] = df['product_price'] * df['quantity']

# Convert 'order_date' to datetime format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
if df['order_date'].isnull().any():
    print("Warning: Some 'order_date' values could not be parsed.")
    
# Extract the month from 'order_date'
df['month'] = df['order_date'].dt.to_period('M')

# Task 1: Total revenue per month
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
