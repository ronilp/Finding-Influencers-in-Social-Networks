from database import getClusterInfluencerScoreCollection, getFullInfluenceScoreCollection, \
    getUserClusterContributionCollection, getFriendsCollection


def getFullInfluenceScore():
    partialScoreCollection = getClusterInfluencerScoreCollection()
    userClusterContributionCollection = getUserClusterContributionCollection()

    fbfriends = getFriendsCollection()
    fullScoreCollection = getFullInfluenceScoreCollection()

    for friend in fbfriends.find():
        fid = friend['id']
        partial = partialScoreCollection.find_one({'_id': fid})
        contribution = userClusterContributionCollection.find_one({'_id': fid})

        score = []

        for i in range(len(contribution['contribution'])):
            avg = 1.0
            try:
                avg *= sum(partial['cluster'][str(i)]) / len(partial['cluster'][str(i)])
            except ZeroDivisionError:
                avg = 0.0
            score.append(avg * contribution['contribution'][i])

        if len(score) > 0:
            document = {}
            document['_id'] = fid
            document['name'] = friend['name']
            document['score'] = score
            fullScoreCollection.insert(document)
            print friend['name'], score


if __name__ == '__main__':
    getFullInfluenceScore()
