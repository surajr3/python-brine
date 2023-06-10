import pandas as pd

df = pd.read_csv('orders.csv', delimiter='\t')

df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')

df['month'] = df['order_date'].dt.to_period('M')
revenue_by_month = df.groupby('month')['product_price'].sum()

revenue_by_product = df.groupby('product_name')['product_price'].sum()

revenue_by_customer = df.groupby('customer_id')['product_price'].sum()

top_10_customers = revenue_by_customer.nlargest(10)

# Print the results
print("Total Revenue by Month:")
print(revenue_by_month)
print("\nTotal Revenue by Product:")
print(revenue_by_product)
print("\nTotal Revenue by Customer:")
print(revenue_by_customer)
print("\nTop 10 Customers 
