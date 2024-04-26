import pymongo
instance=pymongo.MongoClient('mongodb://localhost:27017/')
db=instance['mydatabase']
list=instance.list_database_names
# if "mydatabase" in list:
#     print("knnx")
print(list)
