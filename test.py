from app import df, calculate_monthly_revenue, calculate_product_revenue, calculate_customer_revenue, identify_top_customers

# calculate_monthly_revenue function
monthly_revenue = calculate_monthly_revenue(df)
print("Monthly Revenue:")
print(monthly_revenue)

# calculate_product_revenue function
product_revenue = calculate_product_revenue(df)
print("Product Revenue:")
print(product_revenue)

# calculate_customer_revenue function
customer_revenue = calculate_customer_revenue(df)
print("Customer Revenue:")
print(customer_revenue)

#  identify_top_customers function
top_customers = identify_top_customers(df)
print("Top Customers:")
print(top_customers)

