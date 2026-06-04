import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
rs = pd.read_excel("Product-Sales-Region.xlsx")

print("=" * 50)
print("TASK 4 : DATA VISUALIZATION")
print("=" * 50)

# 1. Sales by Region
region_sales = rs.groupby('Region')['TotalPrice'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 2 Top 10 Products by the Sales
products_sales = rs.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
products_sales.plot(kind='bar')
plt.title("Top 10 Products by the Sales")
plt.xlabel("Products")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 3. Payment  Distribution
payments_count = rs['PaymentMethod'].value_counts()

plt.figure(figsize=(7,7))
payments_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Distribution")
plt.ylabel("")
plt.show()

# 4. Total Price Distribution
plt.figure(figsize=(8,5))
plt.hist(rs['TotalPrice'], bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("Graphs Generated Successfully!")