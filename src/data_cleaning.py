import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/sbi_transaction_data.csv"
)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove null values
df.dropna(inplace=True)

# Convert Amount column to numeric
df["Amount"] = pd.to_numeric(df["Amount"])

# Save cleaned dataset
df.to_csv(
    "data/processed/cleaned_transactions.csv",
    index=False
)

print("Data Cleaning Completed Successfully")