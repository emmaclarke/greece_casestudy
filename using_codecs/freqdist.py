import codecs
import nltk

rawtext = codecs.open('/Users/default/Desktop/july15pilot_round2/clean_irl.txt').read().decode('utf-8').lower()

text = nltk.Text(nltk.word_tokenize(rawtext))
freq = nltk.FreqDist(text)

#print freq.freq('lord')
freq.plot(20, cumulative=False)