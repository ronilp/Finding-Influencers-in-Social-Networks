from database import getClusterInfluencerScoreCollection, getUserClusterContributionCollection


def getClusterContribution():
	clusterInfluencerScoreCollection = getClusterInfluencerScoreCollection()
	userClusterContributionCollection = getUserClusterContributionCollection()
	userClusterContributionCollection.drop()
	for scores in clusterInfluencerScoreCollection.find():
		document = {}
		document['_id'] = scores['_id']
		document['contribution'] = []
		for cscore in sorted(scores['cluster'].keys()):
			document['contribution'].append(len(scores['cluster'][cscore]))

		document['contribution'] = [i*1.0/sum(document['contribution']) for i in document['contribution'] if sum(document['contribution']) > 0]
		userClusterContributionCollection.insert(document)

if __name__ == '__main__':
	getClusterContribution()