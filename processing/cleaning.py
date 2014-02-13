from __future__ import division

import nltk
import json
import re, pprint

from nltk.corpus import stopwords
from nltk.book import *
from nltk.corpus import PlaintextCorpusReader

def dump_json(tokens_in,size,chapter):
     tokens_freq = FreqDist(tokens_in)
     tokens_table = [dict(name=w, size=tokens_freq[w]) for w in tokens_freq]
     tokens_table_short = tokens_table[:size]
     with open("tokens_"+ str(chapter) + "_" + str(size) + ".json",'w') as outfile:
          json.dump(tokens_table_short,outfile, sort_keys = True, indent = 4,
ensure_ascii=False)

def tokenize_chapter(chapter, main_tokens):
	text_raw = open("ofk_ch" + str(chapter) + ".txt").read()
	leng = len(text_raw)
	tokens = nltk.word_tokenize(text_raw)
	tokens = [w.lower() for w in tokens] #change to lower case
	tokens = [re.sub('\.','',w) for w in tokens] #remove periods
	tokens = [w for w in tokens if w.isalpha()] #just keep words
	tokens = [w for w in tokens if not w in stopwords.words('english')]
	tokens_freq = FreqDist(tokens)
	main_freq = FreqDist(main_tokens)
	# Uncomment the following line for pure number of occurences of a word
	final_table = [dict(name=w, size=tokens_freq[w]) for w in main_freq]
	# Uncomment the following line for a normalized representation of the frequency of a word.
	# final_table = [dict(name=w, size=75000*tokens_freq[w]/leng) for w in main_freq]
	final_table_short = final_table[:20]
	with open("tokens_"+str(chapter)+"_20" + ".json",'w') as outfile:
          json.dump(final_table_short,outfile, sort_keys = True, indent = 4,
ensure_ascii=False)
	print "Chapter " + str(chapter) + " Dumped"

text_raw = open("ofk.txt").read()
leng = len(text_raw)
tokens = nltk.word_tokenize(text_raw)
tokens = [w.lower() for w in tokens] #change to lower case
tokens = [re.sub('\.','',w) for w in tokens] #remove periods
tokens = [w for w in tokens if w.isalpha()] #just keep words
tokens = [w for w in tokens if not w in stopwords.words('english')]
tokens_freq = FreqDist(tokens)
dump_json(tokens,20,0)
print "initial batch dumped"
for i in range(4):
	tokenize_chapter(i+1, tokens)

