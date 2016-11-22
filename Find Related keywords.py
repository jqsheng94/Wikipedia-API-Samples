from urllib.request import urlopen
import simplejson as json
import urllib.parse


Terms= ['любви', 'Николай Воронов']
for i in Terms:
    i  = urllib.parse.quote(i)
    language = 'ru'  #language of the Wikipedia branch
    link = json.load(urlopen("https://"+ language + ".wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=" + i))
    relatedTerms = []
    if 'continue' in link:
        number = link['continue']['sroffset']
        titleInfo = link['query']['search']
        for i in titleInfo:
            relatedTerms.append(i['title'])
    print(relatedTerms)




