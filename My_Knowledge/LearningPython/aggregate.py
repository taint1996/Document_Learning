###### aggregate the key along with value so as the find the counts of all possible combinations of key with value
from pymongo import MongoClient
import csv

client = MongoClient()
db = client.csvtomongo

for coll in db.samplecoll.aggregate([{ '$group': { '_id': { 'gender': '$gender', 'opinion': '$opinion'}, 'count': {'$sum': 1}}}])
  print(coll)


######## Import from csv
### mongoimport -h 127.0.0.1 -d [namedb] -c [collection name] --type csv --file name.csv --headerline --ignoreBlanks
# mongoimport -d mydb -c things --type csv --file locations.csv --headerline --ignoreBlanks
