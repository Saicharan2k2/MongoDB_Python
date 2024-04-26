import pymongo as p
client=p.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=client['mydatabase']
collection=db['coll']
res=collection.drop()
print(res)           

# coll collection does not exist
# mydatabase> show collections;
# col
# collection1
# customers