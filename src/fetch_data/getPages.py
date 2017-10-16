from utilities import url, access_token
from database import getPageCollection, getLikesCollection


# Finding only unique pages
def getPages():
    likesCollection = getLikesCollection()
    pageCollection = getPageCollection()
    counter = 0
    for likes in likesCollection.find():
        likes = likes['data']
        for like in likes:
            page = {'_id': like['id']}
            pageCollection.update(page, page, upsert=True)
            counter += 1
            print counter
    print 'Total', counter, 'pages fetched'


if __name__ == '__main__':
    getPages()
