import requests
from database import getFriendsCollection
from utilities import url, access_token
from fetchLikes import getLikes

friendsCollection =  getFriendsCollection()

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
	global friendsCollection,count,done
	for person in data:
		count = count + 1
		
		if person['name'] not in friends:
			likes,done = getLikes(person,count,done)
			personDetails = { 'name' : person['name'], 'likes' : likes }
			friendsCollection.insert(personDetails)
			#print person['name'],  person['id']
		

done = 0
count = 0
friends = []
for friend in friendsCollection.find():
	friends.append(friend['name'])
allFriends = getFriends()
print 'Fetched likes of ' + str(count) + ' friends'