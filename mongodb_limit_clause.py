import pymongo as p
client=p.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=client['sai']
coll=db['col1']
res=coll.find().limit(5)
for x in res:
    print(x)
print(res)


# {'_id': ObjectId('66295ba4d11f75c1f146b799'), 'name': 'sai charan'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79c'), 'name': 'abcd', 'age': '23'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a4'), 'subject': 'ML', 'marks': '45'}
# {'_id': ObjectId('6629f1ff11ade2d23b46b7a0'), 'name': 'ukc', 'age': 45}
# {'_id': ObjectId('6629f1ff11ade2d23b46b79d'), 'name': 'asdfgh', 'age': '22'}
# <pymongo.cursor.Cursor object at 0x0000020711962270>