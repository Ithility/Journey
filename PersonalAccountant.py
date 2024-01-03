import pandas as pd

# Your existing DataFrame
spending = pd.DataFrame({
    "Categories": ['Survivables', 'Bills', 'Treats', 'Clothing', 'Luxuries'],
    "MonthlySpending $": ['250', '150', '100', '0', '80'],
    "DailySpending $": ['50', '0', '20', '0', '5']
})

# Convert spending columns to numeric values
spending["MonthlySpending $"] = pd.to_numeric(spending["MonthlySpending $"])
spending["DailySpending $"] = pd.to_numeric(spending["DailySpending $"])

print(spending)
