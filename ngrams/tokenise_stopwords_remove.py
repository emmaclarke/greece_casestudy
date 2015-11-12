
import codecs
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

stop_list = set(stopwords.words('english'))

infile = codecs.open("/Users/default/Dropbox/PhD/PhD_casestudies/ngram_november/combined_irl.txt", "r", "utf-8")
text = infile.read()
#print(text)

tokens = word_tokenize(text.encode('utf-8'))
tokens = [word for word in tokens if not word in stop_list]
#print(tokens)

