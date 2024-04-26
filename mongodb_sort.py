import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
coll=db['col']
res=coll.find().sort("name")
for c in res:
    print(c)

# {'_id': ObjectId('662a9cae161620e3aea23947'), 'name': 'Amy', 'address': 'Apple st 652'}
# {'_id': ObjectId('662a9cae161620e3aea2394f'), 'name': 'Ben', 'address': 'Park Lane 38'}
# {'_id': ObjectId('662a9cae161620e3aea2394b'), 'name': 'Betty', 'address': 'Green Grass 1'}
# {'_id': ObjectId('662a9cae161620e3aea23948'), 'name': 'Hannah', 'address': 'Mountain 21'}
# {'_id': ObjectId('662a9cae161620e3aea23949'), 'name': 'Michael', 'address': 'Valley 345'}
# {'_id': ObjectId('662a9cae161620e3aea2394c'), 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': ObjectId('662a9cae161620e3aea2394a'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# {'_id': ObjectId('662a9cae161620e3aea2394d'), 'name': 'Susan', 'address': 'One way 98'}
# {'_id': ObjectId('662a9cae161620e3aea2394e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}


#res=coll.find().sort("name",-1)
# {'_id': ObjectId('662a9cae161620e3aea2394e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# {'_id': ObjectId('662a9cae161620e3aea2394d'), 'name': 'Susan', 'address': 'One way 98'}
# {'_id': ObjectId('662a9cae161620e3aea2394a'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# {'_id': ObjectId('662a9cae161620e3aea2394c'), 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': ObjectId('662a9cae161620e3aea23949'), 'name': 'Michael', 'address': 'Valley 345'}
# {'_id': ObjectId('662a9cae161620e3aea23948'), 'name': 'Hannah', 'address': 'Mountain 21'}
# {'_id': ObjectId('662a9cae161620e3aea2394b'), 'name': 'Betty', 'address': 'Green Grass 1'}
# {'_id': ObjectId('662a9cae161620e3aea2394f'), 'name': 'Ben', 'address': 'Park Lane 38'}
# {'_id': ObjectId('662a9cae161620e3aea23947'), 'name': 'Amy', 'address': 'Apple st 652'}
