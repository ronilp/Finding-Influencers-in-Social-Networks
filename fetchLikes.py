import requests
from utilities import url, access_token
import json

def getLikes(person,count,done):
	fbid = person['id']
	rurl = url + '/v2.3/' + fbid
	response = requests.get(rurl,params ={'access_token': access_token, 'fields' : 'likes'})
	print '#' + str(count), "Fetching Likes for friend", ":", person['name']
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
		done = done + 1
		print '#' + str(done) , 'Fetched', str(len(all_likes)) + ' liked pages of ' + person['name']
	return all_likes