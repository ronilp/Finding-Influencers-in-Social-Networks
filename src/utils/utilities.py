import re

url = "https://graph.facebook.com"
access_token = "CAACEdEose0cBAJw4PuZBNWC4BnoT3yEsv0TOVszOxipHLk6x8GVLzKfW9ZBmoT1ZBturw7jGS6jt2cmanDsexxwIPZBoh2A7z9ny4hAPvepzB6RWTmjZA96LCuZBEvuKFRdA0wJkjSepkPFAF1mDToWBZBJk6BTkRFrOM3f6NN1xwGZCe595NWrw2z5tzZCeh6BWJrvb5t8xytXZAnOW53oVbf9jqoVO4eSB0ZD"
KVAL = 7
PID = 449082841792177
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
                string += post.strip().lower() + ' '
        else:
            string += document[key].strip().lower() + ' '
    string = re.sub(r"(?:\@|https?\://)\S+", ' ', string, flags=re.MULTILINE)
    string = re.sub(r"[^\w]", " ", string, flags=re.MULTILINE)
    string = {'_id': document['_id'], 'data': stopWordRemoval(string)}
    return string


def stopWordRemoval(document):
    stopWords = map(str.strip, open('stopwords.txt').readlines())
    string = []
    for word in document.split():
        if word not in stopWords:
            string.append(word)

    return ' '.join(string)
