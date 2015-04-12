import requests
from database import getFriendsCollection
from utilities import url, access_token
from fetchLikes import getLikes

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
	global friendscollection,count
	for person in data:
		count = count + 1
		likes = getLikes(person,count,done)
		personDetails = { person['name'] : likes }
		friendscollection.insert(personDetails)
		#print person['name'],  person['id']

done = 0
count = 0
allFriends = getFriends()