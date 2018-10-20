
from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=False)

result = search.by_coordinates(-114.063442, 50.930246, radius=249, returns=1)

print result