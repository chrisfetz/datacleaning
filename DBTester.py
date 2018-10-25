import pandas as pd

df = pd.read_csv('tax-data/new/taxdata.csv')
print df.isnull().values.any