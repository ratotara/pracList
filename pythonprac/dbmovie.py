from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.m8xno0k.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.update_one({'title':'드림'},{'$set':{'rate':0}})