from uszipcode import SearchEngine
from uszipcode import Zipcode

search = SearchEngine(simple_zipcode=False)

result = search.by_coordinates(33.8238144, -118.3849869)

print result