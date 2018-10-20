import pandas as pd
from uszipcode import SearchEngine

countZip = 0
countCounty = 0
search = SearchEngine(simple_zipcode=False)

#get the zipcode from the 'latitude' and 'longitude' columns in a row
def getZipcode(row):
    global countZip
    global search

    #print progress so I know how far into the process it is
    countZip+= 1
    string = 'getting zipcode ' + str(countZip)
    print string

    latitude = row['latitude']
    longitude = row['longitude']

    result = search.by_coordinates(latitude, longitude)

    #if the address isn't an american address, there won't be a zipcode
    if not result:
        print 'None'
        return 'None'
    else:
        print result[0].zipcode
        return result[0].zipcode

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

oldpath = 'poi-data/old/'
newpath = 'poi-data/new/'
csvs = ['arbys.csv', 'burgerking.csv', 'carlsjr.csv', 'chickfila.csv', 
        'chipotle.csv', 'dominos.csv', 'dq.csv', 'fiveguys.csv', 
        'hardees.csv', 'jackinthebox.csv', 'jimmyjohns.csv', 'kfc.csv', 
        'mcdonalds.csv', 'pandaexpress.csv', 'pizzahut.csv', 'sonic.csv', 
        'subway.csv', 'tacobell.csv', 'wendys.csv', 'whataburger.csv']

names = ['Arby\'s', 'Burger King', 'Carl\'s Jr.', 'Chick-Fil-A',
         'Chipotle', 'Domino\'s', 'Dairy Queen', 'Five Guys',
         'Hardee\'s', 'Jack in the Box', 'Jimmy John\'s', 'KFC',
         'McDonald\'s', 'Panda Express', 'Pizza Hut', 'Sonic Drive-In',
         'Subway', 'Taco Bell', 'Wendy\'s', 'Whataburger']

#loop that creates the csvs
for i in range (0, 20):
    countZip = 0
    countCounty = 0
    oldcsv = oldpath + csvs[i]

    #read from the csv file. columns are longitude, latitude, restaurant name, address
    df = pd.read_csv(oldcsv, names=['longitude', 'latitude', 'title', 'address'])

    #we only care about the 'latitude' and 'longitude' columns
    df = df.reindex(columns=['latitude', 'longitude'])
    
    #we want to add name, zipcode and county columns to compare with our taxdata dataset
    df['name'] = names[i]
    df['zipcode'] = df.apply(lambda row: getZipcode(row), axis=1)
    df['county'] = df.apply(lambda row: getCounty(row), axis=1)
    
    #we only care about US addresses, so remove any canadian addresses
    df = df[df.county != 'None']
    
    #print the dataframe for debugging purposes
    print df

    #write result to a csv file in poi-data/new, don't include index column
    newcsv = newpath + csvs[i]
    df.to_csv(newcsv, index=False, float_format='%.6f')
