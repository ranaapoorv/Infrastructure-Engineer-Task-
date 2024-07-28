# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 01:04:32 2024

@author: ranaa
"""

import pytest
from Tanx import revenue_per_month, top_customers

def test_calculate_revenue():
    data = [
        # Example data
        {'product_price': 10.0, 'quantity': 2},
        {'product_price': 20.0, 'quantity': 1},
    ]
    expected_revenue = 40.0
    assert calculate_revenue(data) == expected_revenue

def test_get_top_customers():
    data = [
        # Example data with customer_id and total_spent
        {'customer_id': 1, 'total_spent': 100.0},
        {'customer_id': 2, 'total_spent': 150.0},
    ]
    top_customers = get_top_customers(data)
    assert top_customers[0]['customer_id'] == 2
    assert top_customers[1]['customer_id'] == 1