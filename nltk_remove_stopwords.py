#tokenize text
import nltk
import string

from collections import Counter

def get_tokens():
	with open('/Users/default/Desktop/july15pilot/Greece/UK_content/clean_uk.txt', 'r') as text_file:
		text = text_file.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

tokens = get_tokens()
count = Counter(tokens)
#print(count.most_common(10))

#removing stopwords
from nltk.corpus import stopwords

tokens = get_tokens()
filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)
print(count.most_common(10))


