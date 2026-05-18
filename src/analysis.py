import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/processed/cleaned_transactions.csv"
)

# Rename columns
df.columns = [
    "Transaction_ID",
    "Date",
    "Time",
    "Customer_ID",
    "Service_Type",
    "Amount",
    "Status"
]

print("\nFirst 5 Rows:\n")
print(df.head())

# Total Amount
total_amount = df["Amount"].sum()

print("\nTotal Transaction Amount:")
print(total_amount)

# Transaction Types
print("\nTransaction Types:\n")

print(
    df["Service_Type"]
    .value_counts()
)

# Status Count
print("\nTransaction Status:\n")

print(
    df["Status"]
    .value_counts()
)

# Highest Amount
highest = df["Amount"].max()

print("\nHighest Transaction Amount:")
print(highest)