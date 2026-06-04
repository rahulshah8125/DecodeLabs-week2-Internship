import pandas as pd

df = pd.read_excel("Product-Sales-Region.xlsx")

print("=" * 50)
print("TASK 2 : DATA CLEANING & PREPROCESSING")
print("=" * 50)

print("\nDataset Shape Before Cleaning:")
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna("Unknown")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

# Save cleaned file
df.to_excel("Cleaned_Product_Sales_Region.xlsx", index=False)

print("\nCleaning completed successfully!")