import nltk

rawtext = open('/Users/default/Desktop/july15pilot/Greece/UK_content/clean_uk.txt').read().decode('utf-8').lower()

text = nltk.Text(nltk.word_tokenize(rawtext))
freq = nltk.FreqDist(text)

#print freq.freq('lord')
freq.plot(20, cumulative=False)