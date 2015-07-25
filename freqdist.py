import nltk

rawtext = open('/Users/default/Desktop/july15pilot/Greece/IRL_content/clean_irl.txt').read().decode('utf-8').lower()

text = nltk.Text(nltk.word_tokenize(rawtext))
freq = nltk.FreqDist(text)

#print freq.freq('lord')
freq.plot(50, cumulative=False)