# counts occurences of individual words in a txt file

file = open(r"/Users/default/Desktop/july15pilot/Greece/UK_content/2015-07-06a.txt", "r", encoding="utf-8-sig")

from collections import Counter
wordcount = Counter(file.read().split())

#to display number of times each indiv word occurs

for item in wordcount.items():
	print("{}\t{}".format(*item))