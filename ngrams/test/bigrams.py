import nltk
from nltk.collocations import *

raw_text = open('/Users/default/Dropbox/PhD/PhD case studies/GreeceJuly15/july15pilot2/Greece/IRL_content/clean_irl.txt').read().decode('utf-8').lower()

tokens = nltk.word_tokenize(raw_text)

#creates bigrams
bgs = nltk.bigrams(tokens)

#calculates frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
	print(k,v)

