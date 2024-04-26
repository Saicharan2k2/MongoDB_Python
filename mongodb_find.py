import pymongo as p
client=p.MongoClient('mongodb://localhost:27017/')
db=client['sai']
# coll=db['new']
# data=coll.find_one()
# print(data)                 #None


# coll=db['col1']
# data=coll.find_one()
# print(data)         #{'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}

coll=db['col1']
# res=coll.find()
# for x in res:
#     print(x)                    #{'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79c'), 'name': 'abcd', 'age': '23'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b7a4'), 'subject': 'ML', 'marks': '45'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b7a0'), 'name': 'ukc', 'age': 45}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79d'), 'name': 'qwer', 'age': '22'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b799'), 'name': 'sai', 'age': '22', 'address': 'hyd'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79e'), 'name': 'tyui', 'marks': 121}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79f'), 'name': 'knkv', 'age': '44'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79b'), 'name': 'charan', 'game': 'cricket', 'place': 'hyd'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b79a'), 'color': 'yellow', 'name': 'mango', 'taste': 'sweet'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b7a2'), 'name': 'nncc', 'age': '34'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b7a1'), 'name': 'nvnk', 'age': '78'}
                                # {'_id': ObjectId('6629f1ff11ade2d23b46b7a3'), 'name': 'kvnf', 'age': '12'}

# for x in coll.find():
#     print(x)
# res=coll.find({},{"name":"sai charan"})
# print(res)
print(coll.find({"name":"sai charan"}))     #<pymongo.cursor.Cursor object at 0x00000285015CA270>
