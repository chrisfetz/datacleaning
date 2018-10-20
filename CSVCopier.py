import pandas as pd

df = pd.read_csv('tax-data/16zpallagi.csv')
smallerdf = df[['STATE', 'zipcode', 'agi_stub', 'N02650', 'A02650']]
print smallerdf