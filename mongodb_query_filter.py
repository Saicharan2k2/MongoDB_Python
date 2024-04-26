import pymongo as p 
client=p.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=client['sai']
coll=db['col1']
#query={"age":{"$gt":"20"}}
# query={"name":"sai charan"}         #{'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}
# res=coll.find(query)
# for x in res:
#     print(x)

# {'_id': ObjectId('6629f1ff11ade2d23b46b79c'), 'name': 'abcd', 'age': '23'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79d'), 'name': 'qwer', 'age': '22'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b799'), 'name': 'sai', 'age': '22', 'address': 'hyd'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79f'), 'name': 'knkv', 'age': '44'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a2'), 'name': 'nncc', 'age': '34'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a1'), 'name': 'nvnk', 'age': '78'}    

#           ---regex---
query={"name":{"$regex":"^s"}}
res=coll.find(query)
for x in res:
    print(x)
                            # starts with s  
# {'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b799'), 'name': 'sai', 'age': '22', 'address': 'hyd'}