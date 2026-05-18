import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="SBI Transaction Dashboard",
    layout="wide"
)

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv(
    "data/processed/cleaned_transactions.csv"
)

# Rename Columns
df.columns = [
    "Transaction_ID",
    "Date",
    "Time",
    "Customer_ID",
    "Service_Type",
    "Amount",
    "Status"
]

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.title("Filters")

service_filter = st.sidebar.multiselect(
    "Select Service Type",
    options=df["Service_Type"].unique(),
    default=df["Service_Type"].unique()
)

status_filter = st.sidebar.multiselect(
    "Select Status",
    options=df["Status"].unique(),
    default=df["Status"].unique()
)

# Filter Data
filtered_df = df[
    (df["Service_Type"].isin(service_filter)) &
    (df["Status"].isin(status_filter))
]

# ---------------------------------
# Title
# ---------------------------------

st.title("🏦 SBI Customer Transaction Analysis Dashboard")

st.markdown("---")

# ---------------------------------
# Metrics
# ---------------------------------

total_transactions = filtered_df.shape[0]

total_amount = filtered_df["Amount"].sum()

average_amount = filtered_df["Amount"].mean()

highest_amount = filtered_df["Amount"].max()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    total_transactions
)

col2.metric(
    "Total Amount",
    f"₹ {total_amount}"
)

col3.metric(
    "Average Amount",
    f"₹ {average_amount:.2f}"
)

col4.metric(
    "Highest Amount",
    f"₹ {highest_amount}"
)

st.markdown("---")

# ---------------------------------
# Charts Row 1
# ---------------------------------

col1, col2 = st.columns(2)

# Transaction Type Chart
type_data = (
    filtered_df["Service_Type"]
    .value_counts()
    .reset_index()
)

type_data.columns = [
    "Service_Type",
    "Count"
]

fig1 = px.bar(
    type_data,
    x="Service_Type",
    y="Count",
    title="Transaction Types",
    text_auto=True
)

col1.plotly_chart(
    fig1,
    use_container_width=True
)

# Status Chart
status_data = (
    filtered_df["Status"]
    .value_counts()
    .reset_index()
)

status_data.columns = [
    "Status",
    "Count"
]

fig2 = px.pie(
    status_data,
    names="Status",
    values="Count",
    title="Transaction Status"
)

col2.plotly_chart(
    fig2,
    use_container_width=True
)

# ---------------------------------
# Charts Row 2
# ---------------------------------

col3, col4 = st.columns(2)

# Amount Distribution
fig3 = px.histogram(
    filtered_df,
    x="Amount",
    nbins=10,
    title="Amount Distribution"
)

col3.plotly_chart(
    fig3,
    use_container_width=True
)

# Amount by Service Type
service_amount = (
    filtered_df
    .groupby("Service_Type")["Amount"]
    .sum()
    .reset_index()
)

fig4 = px.line(
    service_amount,
    x="Service_Type",
    y="Amount",
    markers=True,
    title="Amount by Service Type"
)

col4.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Dataset Preview
# ---------------------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df)

# ---------------------------------
# Download Button
# ---------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_transactions.csv",
    mime="text/csv"
)