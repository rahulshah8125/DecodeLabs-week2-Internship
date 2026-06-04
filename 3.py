import pandas as pd

# Load dataset
ps = pd.read_excel("Product-Sales-Region.xlsx")

print("=" * 50)
print("TASK 3 : EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 50)

# Basic statistics
print("\n1. Statistical Summary")
print(ps.describe())

# Total Sales
print("\n2. Total Sales")
print(ps['TotalPrice'].sum())

# Average Sales
print("\n3. Average Order Value")
print(ps['TotalPrice'].mean())

# Maximum Sale
print("\n4. Maximum Order Value")
print(ps['TotalPrice'].max())

# Minimum Sale
print("\n5. Minimum Order Value")
print(ps['TotalPrice'].min())

# Region-wise Sales
print("\n6. Sales by Region")
print(ps.groupby('Region')['TotalPrice'].sum())

# Product-wise Sales
print("\n7. Sales by Product")
print(ps.groupby('Product')['TotalPrice'].sum())

# Customer Type Analysis
print("\n8. Customer Type Count")
print(ps['CustomerType'].value_counts())

# Payment Method Analysis
print("\n9. Payment Method Usage")
print(ps['PaymentMethod'].value_counts())

# Returns Analysis
print("\n10. Returned Products")
print(ps['Returned'].value_counts())

# Top 5 Highest Orders in the sheet
print("\n11. Top 5 Highest Sales Orders")
print(ps.nlargest(5, 'TotalPrice')[['OrderID', 'Product', 'Region', 'TotalPrice']])

print("\nEDA Completed Successfully!")