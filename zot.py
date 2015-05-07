from pyzotero import zotero
# change 'userid' to the libraryid and the API key to the API key from Zotero
zot = zotero.Zotero('userid', 'user', 'apikey')
articles = zot.items(itemType = 'journalArticle', sort = 'creator', q = 'Jucks')
print(len(articles))

for i in articles:
	print(i['data']['creators'][0]['lastName'])
