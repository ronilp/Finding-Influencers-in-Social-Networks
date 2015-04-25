from utilities import url, access_token, getAppendString
from database import getPageCollection,getPageDataCollection
from Queue import Queue
import traceback
import requests
from requests.exceptions import ConnectionError
import threading
import time
import sys
import re

class fetchingPageData(threading.Thread):
	#Pythonthonic way, avoid using global variable
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.collection = getPageDataCollection()


	def getdata(self,data,string):
		if string in data:
			return data[string]
		return None

	def run(self):
		while True:
			try:
				fbid = self.queue.get()
				trurl = url + '/v2.3/'
				rurl = trurl + fbid
				response = requests.get(rurl, params={'access_token': access_token, 'fields': 'about,category,bio,name,posts.limit(10){message}'})
				data = response.json()
				if 'posts' not in data:
					data['posts'] = {}
					data['posts']['data'] = []
				document = {
						'_id' : fbid,
						'name' : self.getdata(data,'name'),
						'about' : self.getdata(data,'about'),
						'category' : self.getdata(data,'category'),
						'bio' : self.getdata(data,'bio'),
						'posts' : [ self.getdata(msg,'message') for msg in data['posts']['data']]
						}

				string = getAppendString(document)
				a = self.collection.insert(string)
			except:
				self.queue.put(fbid)
				time.sleep(2)
			print fbid
			self.queue.task_done()


def getPageData():
	pageCollection = getPageCollection()
	pageDataCollection = getPageDataCollection()

	queue = Queue()
	index = 1
	for page_id in pageCollection.find():
		if not pageDataCollection.find_one(page_id):
			queue.put(page_id['_id'])
			index += 1

	print index

	for i in range(200):
		t = fetchingPageData(queue)
		t.setDaemon(True)
		t.start()

	queue.join()

	for doc in pageDataCollection.find():
		f = open('data/' + doc['_id'] + '.txt','w')
		f.write(doc['data'])
		f.close()


start = time.time()

if __name__ == '__main__':
	getPageData()
	end = time.time()
	print end - start




