import nltk
from nltk.collocations import *

open_file = open('mlmcd_test.txt', 'r')
raw = open_file.read()

tokens = nltk.word_tokenize(raw)

bgs = nltk.bigrams(tokens)

fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
	print(k,v)

