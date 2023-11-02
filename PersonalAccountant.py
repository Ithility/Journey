import pandas as pd
import numpy as np


spending = pd.DataFrame({
"Categories": ['Survivables', 'Bills', 'Treats', 'Clothing', 'Luxuries'],
"MonthlySpending $": ['250', '150', '100', '0', '80'],
"DailySpending $": ['50', '0', '20', '0', '5']
})

print(spending)