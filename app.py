import pandas as pd

def calculate_monthly_revenue(df):
    revenue_by_month = df.groupby('month')['product_price'].sum()
    return revenue_by_month

def calculate_product_revenue(df):
    revenue_by_product = df.groupby('product_name')['product_price'].sum()
    return revenue_by_product

def calculate_customer_revenue(df):
    revenue_by_customer = df.groupby('customer_id')['product_price'].sum()
    return revenue_by_customer

def identify_top_customers(df):
    revenue_by_customer = calculate_customer_revenue(df)
    top_10_customers = revenue_by_customer.nlargest(10)
    return top_10_customers

df = pd.read_csv('orders.csv', delimiter='\t')

df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')

df['month'] = df['order_date'].dt.to_period('M')
