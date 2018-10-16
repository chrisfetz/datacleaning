from uszipcode import SearchEngine
import csv

search = SearchEngine(simple_zipcode=False)

#with open ('<filename>') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    for row in csv_reader:
#        zipcode = search.by_coordinates(row[0], row[1], 0.01) #find zipcode at cooirdinates




# for each line in csv file
#   split string on commas
#   search for zipcode that matches split[0] & split[1]
#   write ", <zipcode>" at end of line

