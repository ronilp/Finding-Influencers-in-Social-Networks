from database import getPagesClusterInfoCollection, getFriendsCollection, getClusterInfluencerScoreCollection
import datetime
import bisect


def getPartialInfluenceScore():
	clusterInfoCollection = getPagesClusterInfoCollection()
	clusterInfluencerCollection = getClusterInfluencerScoreCollection()
	friendsCollection = getFriendsCollection()
	clusterInfluencerCollection.drop()
	clusterNumber = len(clusterInfoCollection.distinct('cluster'))
	for friend in friendsCollection.find():
		_id = friend['id']
		document = {}
		document['_id'] = _id
		document['cluster'] = {}
		for i in range(clusterNumber):
			document['cluster'][str(i)] = []
		clusterInfluencerCollection.insert(document)

	pagesCursor = clusterInfoCollection.find({"count" : {"$gt" :3}})
	epoch = datetime.datetime.utcfromtimestamp(0)

	dt = 7*24*60*60
	scores = []
	for page in pagesCursor:
		users = page['people']
		users.sort(key = lambda x : x['created_time'])
		cluster = page['cluster']
		liketime = []
		for user in users:
			liketime.append((user['created_time'] - epoch).total_seconds())

		back = 0
		print users
		for user in users:
			userId = user['id']
			timeahead = (user['created_time'] - epoch).total_seconds() + dt
			timeback = (user['created_time'] - epoch).total_seconds() - dt
			ahead = bisect.bisect_right(liketime, timeahead)
			score = ahead - back
			back += 1
			print userId, cluster, score
			clusterInfluencerCollection.update({ '_id' : userId}, { '$push' : {'cluster.' +str(cluster) : score} }, upsert = False)




if __name__ == '__main__':
	getPartialInfluenceScore()