#tokenize text
import nltk
import string
from collections import Counter
from nltk.corpus import stopwords

#infile = open('/Users/default/Desktop/ukuk.txt', 'r')
#text = infile.read()
#infile.close()

def get_tokens():
	with open('/Users/default/Desktop/irelandireland.txt', 'r') as text_file:
		text = text_file.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

tokens = get_tokens()
#count = Counter(tokens)
print(tokens)


stopwords = nltk.corpus.stopwords.words('english')
content = [w for w in tokens if w.lower() not in stopwords]
print(len(content)) 
print(len(tokens))






