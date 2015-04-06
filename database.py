from pymongo import MongoClient

client = MongoClient()
db = client.irassignment

def getFriendsCollection():
	collection = db.fbfriends
	return collection

def getLikesCollection():
	collection = db.fblikes
	return collection