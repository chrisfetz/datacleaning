from uszipcode import SearchEngine
import pandas as pd

search = SearchEngine(simple_zipcode=False)
result = search.by_coordinates(33.949688, -83.399628, radius=30, returns=1)
print (result[0].county)
print (result[0].zipcode)


#with open ('<filename>') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    for row in csv_reader:
#        zipcode = search.by_coordinates(row[0], row[1], 0.01) #find zipcode at cooirdinates




# for each line in csv file
#   split string on commas
#   search for zipcode that matches split[0] & split[1]
#   write ", <zipcode>" at end of line

