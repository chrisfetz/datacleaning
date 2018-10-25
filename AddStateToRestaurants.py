import pandas as pd
from uszipcode import SearchEngine

countState = 0
search = SearchEngine()

def getState(row):
    global countState
    global search

    #print progress so I know how far into the process it is
    countState+= 1
    string = 'getting state ' + str(countState)
    print string

    zipcode = row['zipcode']
    print zipcode

    #If no zipcode has been found, don't bother trying to find a state
    if zipcode == 'None':
        print 'None'
        return 'None'
    #Just in case a zipcode doesn't have a corresponding county in the uszipcode database
    else:
        result = search.by_zipcode(zipcode)
        if not result:
            print 'None'
            return 'None'
        else:
            print result.state
            return result.state

df = pd.read_csv('poi-data/master/restaurants.csv')

#generate states from zipcodes
df['state'] = df['state'] = df.apply(lambda row: getState(row), axis=1)

#write to new tax data file
df.to_csv("restaurants-with-states.csv", index=False)