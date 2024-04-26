import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
# coll=db['customers']

# res=coll.delete_one({})
# print(res)

# DeleteResult({'n': 1, 'electionId': ObjectId('7fffffff0000000000000010'), 'opTime': {'ts': Timestamp(1714109452, 3), 't': 16}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1714109452, 3), 'signature': {'hash': b'9_\x82h\n?)\xb6\xb1\x18\xbf\xe8\x9a\x9b:\xa6H\xd9\xcb\xd3', 'keyId': 7361115298671362053}}, 'operationTime': Timestamp(1714109452, 3)}, acknowledged=True)
# PS C:\Users\saich\MongoDB_Py> 

coll=db['collection1']
res=coll.delete_one({"taste":"sweet"})
print(res)

# DeleteResult({'n': 1, 'electionId': ObjectId('7fffffff0000000000000010'), 'opTime': {'ts': Timestamp(1714109575, 2), 't': 16}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1714109575, 2), 'signature': {'hash': b'hKjq\xc9`\xdc\xf7\x04\xd7\xdd\xc1\xc5\xa9.XlA[\xbc', 'keyId': 7361115298671362053}}, 'operationTime': Timestamp(1714109575, 2)}, acknowledged=True)
