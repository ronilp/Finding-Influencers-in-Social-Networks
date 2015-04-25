import re
url = "https://graph.facebook.com"
access_token = "CAACEdEose0cBAKPdtwsyUXZBaIknGoBZBUQvdLgZC75Pert3K1ZCpJkTa7Az7bB8QdcRKszZBdkcruytEqdRI7uCHZAJv5GhsLn79Fr6sZB99LzILvQBHlvJThJRV9NofJJvQilkh1bA0UeccQEVLYmZBz00XK6bUXx2wNlB6VYOdwKZBUL3ZAj3uFTWhZCLXfv9F1Pw8ZAqBc1c5dbAbsyraLMm"
kval =
tid = 
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
