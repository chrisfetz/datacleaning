import pandas as pd

df = pd.read_csv('tax-data/16zpallagi.csv')
smallerDf = df[['STATE', 'zipcode', 'agi_stub', 'N02650', 'A02650']]
renamedSmallerDf = smallerDf.rename({'agi_stub' : 'incomeBracket', 'N02650' : 'numReturns', 'A02650' : 'totalIncome'}, axis='columns')
print renamedSmallerDf

renamedSmallerDf.to_csv("taxdata.csv")