# Updated Homework Codebook and Dataset Guide

## Course level
Introductory Python analytics course focused on Jupyter, Python basics, pandas, data loading, filtering, grouping, dates, exporting, and basic visualization.

## Homework submission standard
Students should submit a `.ipynb` notebook that runs from top to bottom after restarting the kernel. Each homework should include:

1. Student name and date.
2. Short markdown explanation of the business question.
3. Clean import section.
4. Relative dataset path from `Data/`.
5. Code cells with readable variable names.
6. At least one written interpretation of the result.
7. No hard-coded instructor machine paths.

## Dataset path standard
Use relative paths such as:

```python
import pandas as pd
name_data = pd.read_csv('../Data/Most_Popular_Baby_Boy_Names__Illinois_1980-2013.csv')
fuel_prices = pd.read_csv('../Data/AAA_Fuel_Prices.csv', parse_dates=['Month_of_Price'])
auto_mpg = pd.read_csv('../Data/auto-mpg-tabs.csv', sep='\t', index_col=0)
labor = pd.read_csv('../Data/LaborSheetData.csv', parse_dates=['Business_Date', 'Timestamp'])
```

## Dataset codebook

### Most_Popular_Baby_Boy_Names__Illinois_1980-2013.csv
- `Rank`: popularity rank within year.
- `Year`: calendar year.
- `Name`: baby boy name.
- `Frequency`: count of babies with that name.
- Teaching uses: filtering, sorting, groupby, simple trends.

### AAA_Fuel_Prices.csv / M3_AAA_Fuel_Prices.csv / M5_AAA_Fuel_Prices.csv
- `Month_of_Price`: monthly price date/time.
- `County`: geography, mostly US aggregate in this teaching file.
- `Fuel`: fuel type.
- `Price`: price value.
- `PhysicalUnit`: unit label.
- Teaching uses: parsing dates, plotting trends, groupby by fuel type.

### auto-mpg-tabs.csv / M3_auto-mpg-tabs.csv
- Tab-separated file.
- Columns include `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `accelartion`, `model year`, `carname`.
- Note: original column spelling `accelartion` is preserved to avoid breaking existing lessons.
- Teaching uses: `read_csv(sep='\t')`, numeric summaries, filtering.

### LaborSheetData.csv
Synthetic classroom dataset added for reproducibility.
- `Store`, `Business_Date`, `Hour`, `Day_Part`, `Transactions`, `Net_Sales`, `Labor_Hours`, `Drive_Thru_Avg_Seconds`, `Crew_Count`, `Manager`, `Weather`, `Promotion_Flag`, `Customer_Satisfaction`, `Timestamp`.
- Teaching uses: date parsing, operational KPIs, groupby, business interpretation.

### 724080-13739-2001
Small whitespace-delimited weather training file added for reproducibility.
- Columns are defined inside notebooks as year/month/day/hour plus weather measures.
- Teaching uses: whitespace-delimited import, custom column names, temperature transformation.

## Suggested grading rubric
- Correctness: 40%
- Reproducibility: 20%
- Code readability: 15%
- Interpretation/business explanation: 15%
- Submission hygiene: 10%

## Suggested course improvements
- Add a weekly checklist with exact expected deliverables.
- Add a one-page pandas cheat sheet for `read_csv`, `head`, `info`, `describe`, filtering, groupby, and plotting.
- Add starter and answer notebooks consistently for each homework.
- Keep datasets small and local so beginners can focus on analytics concepts.
- Add a final mini-project using one business dataset and a short executive summary.
