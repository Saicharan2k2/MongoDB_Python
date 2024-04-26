import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
collection=db['coll']
res=collection.drop()
print(res)           

# coll collection does not exist
# mydatabase> show collections;
# col
# collection1
# customers
