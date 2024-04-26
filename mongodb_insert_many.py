import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
mycol=db['col']
list=[
    { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"}
]
res=mycol.insert_many(list)
print(res)
print(res.inserted_ids)
# [ObjectId('662a9cae161620e3aea23947'), ObjectId('662a9cae161620e3aea23948'), ObjectId('662a9cae161620e3aea23949'), 
#  ObjectId('662a9cae161620e3aea2394a'), ObjectId('662a9cae161620e3aea2394b'), ObjectId('662a9cae161620e3aea2394c'), 
#  ObjectId('662a9cae161620e3aea2394d'), ObjectId('662a9cae161620e3aea2394e'), ObjectId('662a9cae161620e3aea2394f')]
