# a number of different things in this code

import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()

#ngrams with 'greece' as a member
#greece_filter = lambda *w: 'greece' not in w

#bigrams
finder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words('/Users/default/Desktop/july15pilot/Greece/IRL_content/clean_irl.txt'))
#only bigrams that appear 3+ times
#finder.apply_freq_filter(3)
#all bigrams which contain Greece
#finder.apply_ngram_filter(greece_filter)
#return the 10 ngrams with the hightest PMI 
print(finder.nbest(bigram_measures.likelihood_ratio, 10))

#trigrams
#finder = TrigramCollocationFinder.from_words(nltk.corpus.genesis.words('/Users/default/Desktop/july15pilot/Greece/IRL_content/clean_irl.txt'))
#only trigrams that appear 3+ times
#finder.apply_freq_filter(3)
#all trigrams that contain 'greece'
#finder.apply_ngram_filter(greece_filter)
#return the 10 ngrams with the hightest PMI 
#print(finder.nbest(trigram_measures.likelihood_ratio, 10))