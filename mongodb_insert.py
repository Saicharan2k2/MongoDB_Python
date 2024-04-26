# import pymongo
# instance=pymongo.MongoClient('mongodb://localhost:27017/')
# mydb=instance['mydatabase']
# collection=mydb['mycollection']
# mydict={"name":"charan","address":"hyd"}
# res=collection.insert_one(mydict)
# print(res)

# import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# mydb = myclient['mydatabase']
# mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# print(x)

import pymongo as p
myclient=p.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase']
coll=mydb['collection1']
data={"color":"yellow","taste":"sweet","name":"mango"}
ins=coll.insert_one(data)
print(ins)                          #InsertOneResult(ObjectId('662a9b0e57247c33d9d09510'), acknowledged=True)
print(ins.inserted_id)              #662a9bc7c6605645a9a83b33
