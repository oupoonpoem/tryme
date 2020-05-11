import pandas as pd
csv_file = 'sales-cut.csv'
df = pd.read_csv(csv_file)
saved_column = df
print(saved_column)
print(saved_column.date)