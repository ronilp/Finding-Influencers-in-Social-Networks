import requests
from database import getLikesCollection, getFriendsCollection
from utilities import url, access_token
from Queue import Queue
import threading
import json

idQueue = Queue()

likesCollection = getLikesCollection()
friendsCollection = getFriendsCollection()

for friend in friendsCollection.find():
	idQueue.put(friend['id'])


class getLikes(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.queue = idQueue

	def run(self):
		while True:
			fbid = self.queue.get()
			rurl = url + '/v2.3/' + fbid
			response = requests.get(rurl,params ={'access_token': access_token, 'fields' : 'likes'})
			print "This is for : ", fbid
			all_likes = []
			while True:
				data = response.json()
				if 'likes' not in data:
					data['likes'] = data
				if 'data' not in data['likes']:
					break
				likes = data['likes']['data']
				if (not 'paging' in data['likes']) or (not 'next' in data['likes']['paging']):
					break
				rurl = data['likes']['paging']['next']
				all_likes.extend(likes)
				response = requests.get(rurl)
			if len(all_likes) > 0:
				likesCollection.insert({'id' : fbid, 'data' : all_likes})
			self.queue.task_done()


for i in range(20):
	t = getLikes()
	t.setDaemon(True)
	t.start()

idQueue.join()



