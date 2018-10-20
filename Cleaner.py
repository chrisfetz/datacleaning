from uszipcode import SearchEngine
import pandas as pd

countZip = 0
countCounty = 0
search = SearchEngine(simple_zipcode=False)
simpleSearch = SearchEngine(simple_zipcode=True)

def getZipcode(row):
    global countZip
    global search
    countZip+= 1
    string = 'getting zipcode ' + str(countZip)
    print string

    latitude = row['latitude']
    longitude = row['longitude']

    result = search.by_coordinates(latitude, longitude)
    if not result:
        print 'None'
        return 'None'
    else:
        print result[0].zipcode
        return result[0].zipcode

def getCounty(row):
    global countCounty
    global search
    countCounty+= 1
    string = 'getting county ' + str(countCounty)
    print string

    zipcode = row['zipcode']
    print zipcode

    if zipcode == 'None':
        print 'None'
        return 'None'
    else:
        result = search.by_zipcode(zipcode)
        if not result:
            print 'None'
            return 'None'
        else:
            print result.county
            return result.county

#loop that creates the csvs
oldpath = 'poi-data/old'
newpath = 'poi-data/new'
csvs = {'arbys.csv', 'burgerking.csv', 'carlsjr.csv', 'chickfila.csv', 
        'chipotle.csv', 'dominos.csv', 'dq.csv', 'fiveguys.csv', 
        'hardees.csv', 'jimmyjohns.csv', 'kfc.csv', 'mcdonalds.csv', 
        'pandaexpress.csv', 'pizzahut.csv', 'sonic.csv', 'subway.csv',
        'tacobell.csv', 'wendys.csv', 'whataburger.csv', 'jackinthebox.csv'}

#read from the csv file. columns are longitude, latitude, restaurant name, address
df = pd.read_csv('poi-data/old/Arbys_USA_CAN.csv', names=['longitude', 'latitude', 'title', 'address'])
df = df.reindex(columns=['latitude', 'longitude'])
df['name'] = 'Arby\'s'
df['zipcode'] = df.apply(lambda row: getZipcode(row), axis=1)
df['county'] = df.apply(lambda row: getCounty(row), axis=1)
df = df[df.county != 'None']
print df

df.to_csv('poi-data/new/arbys.csv', index=False)

#search = SearchEngine(simple_zipcode=False)
#result = search.by_coordinates(33.949688, -83.399628, radius=30, returns=1)
#print (result[0].county)
#print (result[0].zipcode)
