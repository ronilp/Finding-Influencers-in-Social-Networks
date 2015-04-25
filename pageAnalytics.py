from database import getPageCollection, getLikesCollection, getPagesClusterInfoCollection, getClusterCollection
from pprint import pprint
import dateutil.parser as dateparser

allpages = getPageCollection()
alllikes = getLikesCollection()
fbpagesinfo = getPagesClusterInfoCollection()
clusterinfo = getClusterCollection()

fbpagesinfo.drop()
for pageId in allpages.find():
	cursor = alllikes.find({'data' : { '$elemMatch' : {'id' : pageId['_id']} } })
	cluster = clusterinfo.find_one({'pages' : pageId['_id']})
	cluster = cluster["cluster"]

	document = {'_id' : pageId['_id'], 'people' : [], 'count' : cursor.count(), 'cluster' : cluster}
	for c in cursor:
		dd = {'id' : c['id']}
		for pages in c['data']:
			if pages['id'] == pageId['_id']:
					if 'created_time' in pages:
						dd['created_time'] = dateparser.parse(pages['created_time'])
						break
		document['people'].append(dd)
	print document
	fbpagesinfo.insert(document)
	