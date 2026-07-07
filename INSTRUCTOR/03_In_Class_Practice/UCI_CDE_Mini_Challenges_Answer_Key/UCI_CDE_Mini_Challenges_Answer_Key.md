# UCI CDE Mini Challenges Answer Key

Instructor answer key for the module-based 15-minute mini challenges.

## Module 1: Python Environment & Jupyter

### Challenge 1: Create a notebook and execute Hello World.

Students should create a new notebook, add a code cell, and run a basic print statement.

```python
print("Hello, UCI CDE!")
```

Expected output: Hello, UCI CDE!. Teaching note: confirm students can create, run, and save notebooks.

### Challenge 2: Import pandas and display version.

Students should import pandas and check the installed version.

```python
import pandas as pd
print(pd.__version__)
```

Expected output: a pandas version number such as 2.x.x. Teaching note: if this fails, verify the correct environment/kernel.

### Challenge 3: Navigate Jupyter shortcuts.

Students should demonstrate basic shortcuts such as adding cells, switching modes, and running cells.

```python
# Useful shortcuts:
# Shift + Enter: run current cell
# A: insert cell above
# B: insert cell below
# M: change cell to Markdown
# Y: change cell to Code
# DD: delete selected cell
```

Expected outcome: students can explain at least three shortcuts and use them during class.

## Module 2: Python Fundamentals

### Challenge 1: Write a function to compute average sales.

Students should define a reusable function that accepts a list of numeric sales values.

```python
def average_sales(sales):
    if len(sales) == 0:
        return 0
    return sum(sales) / len(sales)

sales_values = [1200, 950, 1430, 1100]
average_sales(sales_values)
```

Expected output: 1170.0. Teaching note: ask students why empty-list handling matters.

### Challenge 2: Find the largest value in a list.

Students should use either Python's built-in max() function or a loop.

```python
sales_values = [1200, 950, 1430, 1100]
largest_sale = max(sales_values)
print(largest_sale)
```

Expected output: 1430. Teaching note: extension question: also find the index/location of the largest sale.

### Challenge 3: Debug a provided Python script.

Students should identify syntax, name, or logic errors and correct them.

```python
# Broken example:
# sales = [100, 200, 300]
# print(sum(sale) / len(sales))

# Corrected version:
sales = [100, 200, 300]
average = sum(sales) / len(sales)
print(average)
```

Expected output: 200.0. Teaching note: discuss variable naming and reading traceback messages.

## Module 3: Pandas DataFrames

### Challenge 1: Find top 10 customers by sales.

Students should group by customer segment if customer-level data is unavailable, or use CustomerID/CustomerName if available.

```python
# If CustomerSegment is available:
top_customers = (
    df.groupby("CustomerSegment")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
top_customers

# If CustomerID exists, use:
# df.groupby("CustomerID")["Sales"].sum().sort_values(ascending=False).head(10)
```

Expected output: a ranked sales summary. Teaching note: explain groupby + aggregation + sorting.

### Challenge 2: Identify missing values.

Students should count missing values by column.

```python
missing_summary = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percent": (df.isna().mean() * 100).round(2)
})
missing_summary
```

Expected output: table showing missing count and percent. Teaching note: ask which missing values matter most for analysis.

### Challenge 3: Filter orders with profit < 0.

Students should select rows where profit is negative.

```python
loss_orders = df[df["Profit"] < 0]
loss_orders.head()

print("Number of negative-profit orders:", len(loss_orders))
```

Expected output: filtered rows plus count. Teaching note: connect negative profit to discounting or cost issues.

### Challenge 4: Create a new Profit Margin column.

Students should calculate profit divided by sales while avoiding divide-by-zero errors.

```python
df["ProfitMargin"] = df["Profit"] / df["Sales"]
df[["Sales", "Profit", "ProfitMargin"]].head()
```

Expected output: new ProfitMargin column. Teaching note: students should format margin as a percentage in final reporting.

## Module 4: Data Wrangling & GroupBy

### Challenge 1: Calculate monthly revenue.

Students should convert order dates to datetime, create month, and aggregate sales.

```python
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["OrderMonth"] = df["OrderDate"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.groupby("OrderMonth")["Sales"]
      .sum()
      .reset_index()
      .sort_values("OrderMonth")
)
monthly_revenue.head()
```

Expected output: monthly sales table. Teaching note: emphasize datetime conversion before grouping.

### Challenge 2: Group by region and summarize sales.

Students should summarize sales by region.

```python
region_sales = (
    df.groupby("Region")["Sales"]
      .agg(["count", "sum", "mean"])
      .sort_values("sum", ascending=False)
)
region_sales
```

Expected output: count, total sales, and average sales by region.

### Challenge 3: Export grouped results to CSV.

Students should export the grouped summary.

```python
region_sales.to_csv("region_sales_summary.csv")
print("Export complete.")
```

Expected output: CSV file created in working directory. Teaching note: show students where Jupyter saves files.

## Module 5: Visualization

### Challenge 1: Create a bar chart by category.

Students should aggregate sales by category and create a readable bar chart.

```python
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

category_sales.plot(kind="barh", figsize=(8, 5))
plt.title("Total Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.show()
```

Expected output: horizontal bar chart. Teaching note: horizontal bars often improve readability for category names.

### Challenge 2: Compare sales vs profit.

Students should create a scatter plot or grouped bar chart.

```python
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.5)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()
```

Expected output: scatter plot showing relationship between sales and profit. Teaching note: ask students to identify outliers.

### Challenge 3: Improve a misleading chart.

Students should improve chart labels, scale, title, and readability.

```python
# Weak chart:
# df.groupby("Region")["Sales"].sum().plot(kind="bar")

# Improved chart:
region_sales = df.groupby("Region")["Sales"].sum().sort_values()
region_sales.plot(kind="barh", figsize=(8, 5))
plt.title("Total Sales by Region")
plt.xlabel("Total Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
```

Expected output: better-labeled chart. Teaching note: discuss why title, axis labels, and sorting matter.

## Module 6: Machine Learning Basics

### Challenge 1: Train a linear regression model.

Students should use simple numeric features to predict profit.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

features = ["Sales", "Discount", "Quantity"]
model_df = df[features + ["Profit"]].dropna()

X = model_df[features]
y = model_df["Profit"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
```

Expected output: trained model coefficients. Teaching note: clarify that this is an introductory predictive model, not a production model.

### Challenge 2: Interpret feature importance.

Students should examine coefficients from linear regression.

```python
coef_table = pd.DataFrame({
    "feature": features,
    "coefficient": model.coef_
}).sort_values("coefficient", ascending=False)

coef_table
```

Expected output: coefficient table. Teaching note: larger absolute values indicate stronger model relationship, but interpretation depends on units.

### Challenge 3: Evaluate model accuracy.

Students should calculate R-squared and error metrics.

```python
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

predictions = model.predict(X_test)

print("R-squared:", round(r2_score(y_test, predictions), 3))
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 2))
```

Expected output: R-squared, MAE, and RMSE. Teaching note: explain that lower MAE/RMSE is better, higher R-squared is generally better.

## Module 7: Applied Data Science

### Challenge 1: Clean messy business data.

Students should demonstrate multiple cleaning steps.

```python
clean_df = df.copy()

clean_df = clean_df.drop_duplicates()
clean_df["Region"] = clean_df["Region"].astype("string").str.strip().str.title()
clean_df["Category"] = clean_df["Category"].astype("string").str.strip().str.title()
clean_df["OrderDate"] = pd.to_datetime(clean_df["OrderDate"], errors="coerce")

clean_df.isna().sum()
```

Expected output: cleaned dataframe and missing-value check. Teaching note: ask students to document why each cleaning step is needed.

### Challenge 2: Answer an executive business question.

Students should answer a business question with evidence.

```python
# Example question: Which region is most profitable?
region_profit = (
    clean_df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)
region_profit

best_region = region_profit.index[0]
print(f"The most profitable region is {best_region}.")
```

Expected output: ranked region profit and a written conclusion.

### Challenge 3: Write three recommendations.

Students should convert analysis into business actions.

```python
recommendations = [
    "Review high-discount transactions because they may reduce profit margin.",
    "Track profit margin in addition to sales revenue.",
    "Standardize data entry rules for region, category, and order date fields."
]

for i, rec in enumerate(recommendations, start=1):
    print(f"{i}. {rec}")
```

Expected output: three evidence-based recommendations. Teaching note: recommendations should be specific and actionable.

## Module 8: LLM / Generative AI

### Challenge 1: Use an LLM to explain pandas code.

Students should ask an AI tool to explain a code block, then verify the explanation.

```python
# Example prompt:
# "Explain this pandas code in plain English:
# df.groupby('Region')['Sales'].sum().sort_values(ascending=False)"
```

Expected answer: The code groups records by region, sums sales within each region, and sorts regions from highest to lowest total sales.

### Challenge 2: Improve prompts.

Students should rewrite a vague prompt into a specific prompt.

```python
# Weak prompt:
# "Fix my pandas code."

# Improved prompt:
# "I am using pandas to group retail sales by Region and calculate total Sales and Profit.
# Here is my code and error message. Please explain the error, suggest a corrected version,
# and describe how I can verify the output."
```

Expected outcome: a clearer prompt including context, goal, code, error, and desired output.

### Challenge 3: Verify AI-generated results.

Students should test AI-generated code and validate the output independently.

```python
# Verification checklist:
# 1. Run the code without errors.
# 2. Check row and column counts.
# 3. Compare sample calculations manually.
# 4. Confirm chart labels and units.
# 5. Explain the result in your own words.
```

Expected outcome: students do not copy AI output blindly; they test and explain it.

