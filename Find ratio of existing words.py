#Check the ratio of existing words in Wikipedia under certain language branch

from urllib.request import urlopen
import simplejson as json
import urllib.parse
import re

language = 'ar'
Sentence ="""ليج اوف ليجيندز شرح القيم بلاي (الأساسيات)"""
length = len(Sentence)
Sentence = re.sub(r'[,|\(|\)|\[|\]\{\}|\#|\$|\%|\+|\&|\*|\^]', ' ', Sentence)
WordsList = Sentence.split()
WordsInWikipedia = 0
for i in WordsList:
    i = urllib.parse.quote(i)
    link = json.load(urlopen("https://" + language + ".wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=" + i))
    if 'continue' in link:
        WordsInWikipedia += 1

ratio = WordsInWikipedia/len(WordsList)
print(ratio)

