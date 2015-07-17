#using NLTK's stopword list, remove stopwords from a file
#remoember stopwords.words('english') returns a list of lowercase SWs

from nltk.corpus import stopwords

text = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk.txt", 'r')
stopwords = set(stopwords.words('english'))

for line in text:
	for word in line.split():
		if word.lower() not in stopwords:
			print word

