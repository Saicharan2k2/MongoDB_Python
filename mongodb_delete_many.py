import pymongo as p
client=p.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=client['mydatabase']
coll=db['coll']
# parameter={"name":{"$regex":"^S"}}
res=coll.delete_many({})        #4  documents deleted..
print(res.deleted_count," documents deleted..")

# 0  documents deleted..
# PS C:\Users\saich\MongoDB_Py> & C:/Users/saich/AppData/Local/Programs/Python/Python312/python.exe c:/Users/saich/MongoDB_Py/mongodb_delete_many.py
# 1  documents deleted..
# PS C:\Users\saich\MongoDB_Py> & C:/Users/saich/AppData/Local/Programs/Python/Python312/python.exe c:/Users/saich/MongoDB_Py/mongodb_delete_many.py
# 2  documents deleted..