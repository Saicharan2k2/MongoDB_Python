import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
mycol=db['coll']
list1=[
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id":76, "name": "William", "address": "Central st 954"},
  { "_id":44, "name": "Chuck", "address": "Main Road 989"},
  { "_id":21, "name": "Viola", "address": "Sideway 1633"}
]
ids=mycol.insert_many(list1)
print(ids)
print(ids.inserted_ids)
# InsertManyResult([11, 76, 44, 21], acknowledged=True)
# [11, 76, 44, 21]
