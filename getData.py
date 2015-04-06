import requests
from database import getFriendsCollection
from utilities import url, access_token


friendscollection =  getFriendsCollection()

def getFriends():
	global url, access_token
	rurl = url + '/v2.3/me'
	response = requests.get(rurl, params = {'access_token' : access_token, 'fields' : 'friends'})
	while True:
		data = response.json()
		if not 'friends'in data:
			data['friends'] = data

		insertFriends(data['friends']['data'])
		if 'next' in data['friends']['paging']:
			rurl = data['friends']['paging']['next']
		else:
			break
		response = requests.get(rurl)


def insertFriends(data):
	#collection.insert_many(data)
	global friendscollection
	for person in data:
		friendscollection.insert(person)
		print person['name'],  person['id']


allFriends = getFriends()