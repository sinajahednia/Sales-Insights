
import pandas as pd


# ==========================================
# 1. LOAD DATA
# ==========================================

print("\n========== SALES ANALYSIS ==========\n")

df = pd.read_csv("data/online_retail.csv")


# ==========================================
# 2. CALCULATE SALES
# ==========================================

df["Sales"] = df["Quantity"] * df["UnitPrice"]


# ==========================================
# 3. IDENTIFY SALES AND CANCELLATIONS
# ==========================================

cancelled = df["InvoiceNo"].str.startswith("C", na=False)

positive_sales = (df["Quantity"] > 0) & (~cancelled)


# ==========================================
# 4. MAIN BUSINESS METRICS
# ==========================================

total_recorded_sales = df["Sales"].sum()

gross_sales = df.loc[positive_sales, "Sales"].sum()

cancelled_sales = df.loc[cancelled, "Sales"].sum()

total_orders = df.loc[positive_sales, "InvoiceNo"].nunique()

total_invoices = df["InvoiceNo"].nunique()

average_order_value = gross_sales / total_orders


print("----- BUSINESS SUMMARY -----")
print(f"Total Recorded Sales: £{total_recorded_sales:,.2f}")
print(f"Gross Sales: £{gross_sales:,.2f}")
print(f"Cancelled Sales: £{cancelled_sales:,.2f}")
print(f"Total Invoices: {total_invoices:,}")
print(f"Valid Orders: {total_orders:,}")
print(f"Average Order Value: £{average_order_value:,.2f}")


# ==========================================
# 5. SALES BY COUNTRY
# ==========================================

country_sales = (
    df.loc[positive_sales]
    .groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\n----- TOP 3 COUNTRIES -----")
print(country_sales)


# ==========================================
# 6. PRODUCT ANALYSIS
# ==========================================

product_revenue = (
    df.loc[positive_sales]
    .groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

product_quantity = (
    df.loc[positive_sales]
    .groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\n----- TOP 3 PRODUCTS BY REVENUE -----")
print(product_revenue)

print("\n----- TOP 3 PRODUCTS BY QUANTITY -----")
print(product_quantity)


# ==========================================
# 7. MONTHLY SALES ANALYSIS
# ==========================================

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month

monthly_sales = (
    df.loc[positive_sales]
    .groupby(["Year", "Month"])["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n----- TOP 3 SALES MONTHS -----")
print(monthly_sales.head(3))


print("\n========== ANALYSIS COMPLETED ==========")
