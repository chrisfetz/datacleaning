import glob
import pandas as pd

path = r'poi-data/new/'
allFiles = glob.glob(path + "*.csv")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_)
    list_.append(df)

frame = pd.concat(list_)
print frame

frame.to_csv('poi-data/master/restaurants.csv', index=False)