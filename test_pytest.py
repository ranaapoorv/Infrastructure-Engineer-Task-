import unittest
import pandas as pd
from io import StringIO

class TestRevenueCalculations(unittest.TestCase):
    
    def setUp(self):
        # Mock CSV data
        data = StringIO("""
        order_date,product_name,product_price,quantity,customer_id
        2024-01-10,Product A,10,2,1
        2024-01-15,Product B,20,1,2
        2024-02-10,Product A,10,3,1
        2024-02-15,Product B,20,2,3
        2024-02-20,Product C,30,1,2
        """)
        
        # Read the mock data into a DataFrame
        self.df = pd.read_csv(data)
        
        # Strip any leading or trailing spaces from the column names
        self.df.columns = self.df.columns.str.strip()
        
        # Perform the calculations as in the original program
        self.df['revenue'] = self.df['product_price'] * self.df['quantity']
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        
    def test_revenue_per_month(self):
        expected_revenue_per_month = pd.DataFrame({
            'month': [pd.Period('2024-01', 'M'), pd.Period('2024-02', 'M')],
            'revenue': [40, 100]
        })
        
        revenue_per_month = self.df.groupby('month')['revenue'].sum().reset_index()
        
        pd.testing.assert_frame_equal(revenue_per_month, expected_revenue_per_month)
        
    def test_revenue_per_product(self):
        expected_revenue_per_product = pd.DataFrame({
            'product_name': ['Product A', 'Product B', 'Product C'],
            'revenue': [50, 60, 30]
        })
        
        revenue_per_product = self.df.groupby('product_name')['revenue'].sum().reset_index()
        
        pd.testing.assert_frame_equal(revenue_per_product, expected_revenue_per_product)
        
    def test_revenue_per_customer(self):
        expected_revenue_per_customer = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'revenue': [50, 50, 40]
        })
        
        revenue_per_customer = self.df.groupby('customer_id')['revenue'].sum().reset_index()
        
        pd.testing.assert_frame_equal(revenue_per_customer, expected_revenue_per_customer)
        
    def test_top_customers(self):
        expected_top_customers = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'revenue': [50, 50, 40]
        }).sort_values(by='revenue', ascending=False).head(10).reset_index(drop=True)
        
        revenue_per_customer = self.df.groupby('customer_id')['revenue'].sum().reset_index()
        top_customers = revenue_per_customer.sort_values(by='revenue', ascending=False).head(10).reset_index(drop=True)
        
        pd.testing.assert_frame_equal(top_customers, expected_top_customers)
        
if __name__ == '__main__':
    unittest.main()
