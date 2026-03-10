import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("online_retail.csv")

# Display first 5 rows
print(df.head())

# Remove missing values
df = df.dropna()

# Create Sales column
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# Top selling products
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

print("Top Selling Products:")
print(top_products)

# Plot top selling products
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.show()

# Sales by country
country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)

country_sales.plot(kind="bar")
plt.title("Top Countries by Sales")
plt.show()

# Monthly sales trend
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.show()