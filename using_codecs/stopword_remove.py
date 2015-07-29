import codecs
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_list = set(stopwords.words('english'))

infile = codecs.open("/Users/default/Desktop/july15pilot_round2/clean_irl.txt", "r", "utf-8")
text = infile.read()
#print(text)

tokens = word_tokenize(text.encode('utf-8'))
tokens = [word for word in tokens if not word in stop_list]
print(tokens.encode('utf-8'))

#freq = nltk.FreqDist(tokens)

#freq.plot(20, cumulative=False)
