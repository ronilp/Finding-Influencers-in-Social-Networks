from pymongo import MongoClient

client = MongoClient()
db = client.fbDatabase

def getFriendsCollection():
	collection = db.fbfriends
	return collection
