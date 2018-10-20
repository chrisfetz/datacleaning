import pandas as pd
from uszipcode import SearchEngine

countCounty = 0
search = SearchEngine(simple_zipcode=False)

def getCounty(row):
    global countCounty
    global search

    #print progress so I know how far into the process it is
    countCounty+= 1
    string = 'getting county ' + str(countCounty)
    print string

    zipcode = row['zipcode']
    print zipcode

    #If no zipcode has been found, don't bother trying to find a county
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
            print result.county
            return result.county

#read tax data file
df = pd.read_csv('tax-data/old/16zpallagi.csv')

#remove unnecessary columns
df = df[['STATE', 'zipcode', 'agi_stub', 'N02650', 'A02650']]

#rename the columns to be understandable
df = df.rename({'STATE' : 'state', 'agi_stub' : 'incomeBracket', 
                'N02650' : 'numReturns', 'A02650' : 'totalIncome'}, axis='columns')

#generate counties from zipcodes
df["county"] = df['county'] = df.apply(lambda row: getCounty(row), axis=1)

#reorder columns
df = df[['state', 'zipcode', 'county', 'incomeBracket', 'numReturns', 'totalIncome']]

#print dataframe for debugging purposes
print df

#write to new tax data file
df.to_csv("tax-data/new/taxdata.csv", index=False)