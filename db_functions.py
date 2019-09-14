from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin:admin@cluster0-ah6nw.mongodb.net/test"

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection


def db_insert_user(collection, user):
    return collection.insert_one(user)


def db_find_all(collection, query={}):
    return collection.find(query)

def db_delete_one(collection, query={}):
	return collection.delete_many(query)
    
def db_find_one(collection, query={}):
    return collection.find_one(query)

if __name__ == '__main__':

	bubuc = db_connect(MONGO_URI, 'LinceHack', 'Usuarios')
	db_insert_user(bubuc, {'user':'bubu'})
	print("jalo")