import operator
text = open('mlmcd_test.txt', 'r')


wordlist = list()

lines = text.readlines()

for i in range(len(lines)):
	lines[i] = lines[i].strip()
	lines[i] = lines[i].strip('.')

	if lines[i] != '':
		if lines[i][0] == '[':
			j = lines[i].find(']')
			lines[i] = lines[i][j+2:]
		lines[i] = lines[i].split(" ")

		if not lines[i][0].isupper() and lines[i][0] != 'Enter':
			for word in lines[i]:
				wordlist.append(word)

n = 2
ngrams = dict()

for i in range(len(wordlist) - n + 1):
	gram = tuple(wordlist[i:i+n])
	if gram in ngrams:
		ngrams[gram] += 1
	else:
		ngrams[gram] = 1

sorted_ngrams = sorted(ngrams.iteritems(), key = operator.itemgetter(1), reverse = True)
print(sorted_ngrams)