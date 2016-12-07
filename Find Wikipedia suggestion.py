from urllib.request import urlopen
import simplejson as json
import re
import os
import urllib.parse
import csv

Sentence ="""الفرقة القومية العربية للموسيقى بقيادة المايسترو سليم سحاب في ذكرى أم كلثوم على مسرح الجمهورية"""
Sentence = re.sub(r'[,|\(|\)|\[|\]\{\}|\#|\$|\%|\+|\&|\*|\^]', ' ', Sentence)
Terms= Sentence.split()
relatedTerms = []
suggestion = []
for i in Terms:
    Rec = []
    i  = urllib.parse.quote(i)
    language = 'ar'  #language of Wikipedia branch
    link = json.load(urlopen("https://"+ language + ".wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=" + i))

    if 'continue' in link:
        number = link['continue']['sroffset']
        titleInfo = link['query']['search']
        suggestion.append('None')
        for i in titleInfo:
            Rec.append(i['title'])
    elif 'suggestion' in link['query']['searchinfo']:
        Rec.append('None')
        suggestionInfo = link['query']['searchinfo']['suggestion']
        suggestion.append(suggestionInfo)
    else:
        Rec.append('None')
        suggestion.append('None')
    relatedTerms.append(Rec)

file_exists = os.path.isfile("PUT YOUR PATH IN HERE/suggestion.csv")
with open("PUT YOUR PATH IN HERE/suggestion.csv", 'a') as csvfile:
    temp = csv.writer(csvfile, delimiter=',')
    temp.writerows(zip(Terms, relatedTerms, suggestion))












