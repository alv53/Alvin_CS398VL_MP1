import nltk
import json
# nltk.download()
# from nltk.book import *
from nltk.corpus import PlaintextCorpusReader
wordlists = PlaintextCorpusReader('', 'ofk_ch[1234]\.txt')
wordlists.fileids()
# print "hi"

ch1_words = wordlists.words('ofk_ch1.txt')
print len(ch1_words)

ch2_words = wordlists.words('ofk_ch2.txt')
print len(ch2_words)

ch3_words = wordlists.words('ofk_ch3.txt')
print len(ch3_words)

ch4_words = wordlists.words('ofk_ch4.txt')
print len(ch4_words)
