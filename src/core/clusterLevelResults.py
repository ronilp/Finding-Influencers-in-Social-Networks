from database import getFullInfluenceScoreCollection, getclusterLevelResultCollection


def clusterLevelResults():
    scoreCollection = getFullInfluenceScoreCollection()
    clusterResCollection = getclusterLevelResultCollection()

    numCluster = len(scoreCollection.find_one()['score'])
    clusterResCollection.drop()
    for i in range(numCluster):
        doc = {}
        i = str(i)
        doc['_id'] = i
        doc['users'] = []
        clusterResCollection.insert(doc)

    for scores in scoreCollection.find():
        fid = scores['_id']
        name = scores['name']
        userScore = scores['score']
        for i in range(len(userScore)):
            doc = {}
            doc['id'] = fid
            doc['name'] = name
            doc['score'] = userScore[i]
            cluster = str(i)
            print i, doc
            clusterResCollection.update({'_id': cluster},
                                        {
                                            '$push': {
                                                'users': {
                                                    '$each': [doc],
                                                    '$sort': {'score': -1},
                                                    '$slice': -1000
                                                }
                                            }

                                        }
                                        , upsert=False)


if __name__ == '__main__':
    clusterLevelResults()
