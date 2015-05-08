from pyzotero import zotero
# read userid and apikey from config file
execfile('zottxt2note.conf')

zot = zotero.Zotero(userid, 'user', apikey)
articles = zot.items(itemType = 'journalArticle', sort = 'creator', q = 'Jucks')
print(len(articles))

for i in articles:
	print(i['data']['creators'][0]['lastName'])
