import re
url = "https://graph.facebook.com"
access_token = "CAACEdEose0cBAKBNJBJv2LfSD0JjWEinAwzDtyHpU9HA7YOxPAMKL6VJkfTZBFU0nAtLRfpTZAeRHtOhPFs4h9GZBGMc6GZAiBzdBuCKa33c7bB748Jn8Rtm1Ji4rBa5ZAXuAKydgKzRF1crZA44HSdeUKXKZAWeZBgXGmangCP9UtX4ZBtZBtQ7fLLnclESOJZCB1ZB9t8RpSnPThqJpkOizRoGAz0IhOvQEI8ZD"
KVAL = 7
PID = "1573397092904626"
MAXOUT = 3

def getAppendString(document):
		string = ''
		for key in document:
			if not document[key] or key == '_id' or key == 'were_here_count':
				continue
			elif key == 'posts':
				for post in document[key]:
					if not post:
						continue
					string += post.strip().lower() +' '
			else:
				string += document[key].strip().lower() + ' '
		string = re.sub(r"(?:\@|https?\://)\S+",' ',string,flags=re.MULTILINE)
		string = re.sub(r"[^\w]"," ", string,flags=re.MULTILINE)
		string = {'_id' :document['_id'], 'data' : stopWordRemoval(string)}
		return string

def stopWordRemoval(document):
	stopWords = map(str.strip,open('stopwords.txt').readlines())
	string = []
	for word in document.split():
		if word not in stopWords:
			string.append(word)

	return ' '.join(string)
