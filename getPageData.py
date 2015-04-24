from utilities import url, access_token
from database import getPageCollection,getPageDataCollection
from Queue import Queue
import requests
import time
import sys
def getPageData():
	pageCollection = getPageCollection()
	pageDataCollection = getPageDataCollection()
	trurl = url + '/v2.3/'
	for page in pageCollection.find():
		rurl = trurl + page['_id']
		response = requests.get(rurl, params={'access_token': access_token, 'fields': 'about,category,bio,name,were_here_count,posts.limit(10){message}'})
		if response.status_code != 200:
			print page['_id']
			sys.stderr.write(page['_id'] + '\n')
		else:
			print response.json()


start = time.time()

if __name__ == '__main__':
	getPageData()
	end = time.time()
	print end - start




