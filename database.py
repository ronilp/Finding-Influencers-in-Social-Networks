from pymongo import MongoClient

client = MongoClient()
db = client.fbdb

def getFriendsCollection():
	collection = db.fbfriends
	return collection

def getLikesCollection():
	collection = db.fblikes
	return collection

def getPageCollection():
	collection = db.fbpages
	return collection

def getPageDataCollection():
	collection= db.fbpagesdata
	return collection

#cluster : [pageids]
def getClusterCollection():
	collection = db.cluster
	return collection


#pageId : cluster, peopleId, count
def getPagesClusterInfoCollection():
	collection = db.fbpagesclusterinfo
	return collection

def getClusterInfluencerScoreCollection():
	collection = db.clusterInfluencerScore
	return collection

def getUserClusterContributionCollection():
	collection = db.userClusterContribution
	return collection

def getFullInfluenceScoreCollection():
	collection = db.fullInfluenceScore
	return collection

def getclusterLevelResultCollection():
	collection = db.clusterLevelResult
	return collection