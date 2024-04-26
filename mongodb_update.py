import pymongo as p
client=p.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=client['sai']
coll=db['col1']
res=coll.update_one({"name":"qwer"},{"$set":{"name":"asdfgh"}})
for x in coll.find():
    print(x)


# {'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79c'), 'name': 'abcd', 'age': '23'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a4'), 'subject': 'ML', 'marks': '45'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a0'), 'name': 'ukc', 'age': 45}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79d'), 'name': 'asdfgh', 'age': '22'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b799'), 'name': 'sai', 'age': '22', 'address': 'hyd'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79e'), 'name': 'tyui', 'marks': 121}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79f'), 'name': 'knkv', 'age': '44'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79b'), 'name': 'charan', 'game': 'cricket', 'place': 'hyd'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79a'), 'color': 'yellow', 'name': 'mango', 'taste': 'sweet'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a2'), 'name': 'nncc', 'age': '34'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a1'), 'name': 'nvnk', 'age': '78'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a3'), 'name': 'kvnf', 'age': '12'}