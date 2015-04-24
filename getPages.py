from utilities import url, access_token
from database import getPageCollection,getLikesCollection


def getPages():

	likesCollection = getLikesCollection()
	pageCollection = getPageCollection()

	for likes in likesCollection.find():
		likes = likes['data']
		for like in likes:
			page = {'_id' : like['id']}
			print pageCollection.update(page, page, upsert=True)


if __name__ == '__main__':
	getPages()
