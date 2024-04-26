import pymongo
instance=pymongo.MongoClient('mongodb+srv://sai_charan:sai2024@clusterone.fw2f1nq.mongodb.net/')
db=instance['mydatabase']
list=instance.list_database_names
# if "mydatabase" in list:
#     print("knnx")
print(list)