For this project, I collected data from IRS tax records and restaurant location data from poi-factory.com. I used the uszipcode and pandas libraries to derive county info
from the zipcodes in the tax return data, and zipcode and county data for the coordinates in the restaurant csv files. Then, I consolidated the restaurant data using pandas into one single master restaurant csv file in poi-data/master. This data would be great for data sceince projects, as would the data in tax-data/old. tax-data/new contians the same data, just trimmed down for my purposes as my project will be focussing on total income by income bracket and geographical region.