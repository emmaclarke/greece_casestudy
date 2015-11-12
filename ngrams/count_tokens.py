#lowercase all and remove punctuation and tokenise text 
import nltk
import string
import codecs

from collections import Counter

def get_tokens():
	#with codecs.open('/Users/default/Dropbox/PhD/PhD_casestudies/ngram_november/combined_irl.txt', 'r') as text_file:  #which doesn't actually work
	with open('/Users/default/Dropbox/PhD/PhD_casestudies/ngram_november/combined_irl.txt', 'r') as text_file:
		text = text_file.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

tokens = get_tokens()
count = Counter(tokens)
print(count) #or print(count.most_common(10))

#remove stopwords

#from nltk.corpus import stopwords

#tokens = get_tokens()
#filtered = [w for w in tokens if not w in stopwords.words('english')]
#count - Counter(filtered)
#print(count.most_common(10))