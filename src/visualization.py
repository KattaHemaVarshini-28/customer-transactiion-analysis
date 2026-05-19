import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Transaction Type Chart
plt.figure(figsize=(8,5))

sns.countplot(
    x="Service_Type",
    data=df
)

plt.title("Transaction Types")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "images/category_sales.png"
)

plt.show()


# Status Pie Chart
df["Status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Transaction Status")

plt.ylabel("")

plt.savefig(
    "images/payment_mode.png"
)

plt.show()


# Amount Distribution
plt.figure(figsize=(8,5))

sns.histplot(
    df["Amount"],
    bins=10,
    kde=True
)

plt.title("Amount Distribution")

plt.tight_layout()

plt.savefig(
    "images/sales_trend.png"
)

plt.show()

print("Graphs Saved Successfully")