import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_list = set(stopwords.words('english'))

with open('/Users/default/Desktop/july15pilot/Greece/UK_content/clean_uk.txt', 'r') as text_file:
    text = text_file.read()
    tokens = word_tokenize(str(text))
    tokens = [word for word in tokens if not word in stop_list]
    #print tokens

freq = nltk.FreqDist(tokens)

freq.plot(20, cumulative=False)
