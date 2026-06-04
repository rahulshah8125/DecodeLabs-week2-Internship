import pandas as pd

# Load the complete dataset
df = pd.read_excel("Product-Sales-Region.xlsx")

print("=" * 50)
print("TASK 1: DATASET UNDERSTANDING")
print("=" * 50)

# Dataset size
print("\n1. Dataset Size")
print("Rows and Columns:", df.shape)

# Column names
print("\n2. Column Names")
for col in df.columns:
    print(col)

# Data types
print("\n3. Data Types")
print(df.dtypes)

# Dataset information
print("\n4. Dataset Information")
df.info()

# Check missing values
print("\n5. Missing Values")
print(df.isnull().sum())

# Check duplicate rows
print("\n6. Duplicate Rows")
print("Duplicate Rows:", df.duplicated().sum())

# Statistical summary
print("\n7. Statistical Summary")
print(df.describe(include='all'))

print("\n8. Complete Dataset")
print(df)

print("\nDataset Understanding Completed Successfully!")