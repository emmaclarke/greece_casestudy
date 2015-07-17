infile = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk.txt")
text = infile.read()
infile.close()

#function split operates on a string and splits a string on spaces and returns a list of smaller strings (or words):
#print(text.split())

def remove_punc(text):
	punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`-1234567890'
	clean_text = " "
	for character in text:
		if character not in punctuation:
			clean_text += character
	return clean_text

new_text = remove_punc(text.lower())   #removes punctuation and makes everything lowercase

print(new_text)

words = new_text.split()

def counter(list_to_search):
	counts = {}
	for word in list_to_search:
		if word in counts:
			counts[word] = counts[word] + 1
		else:
			counts[word] = 1
	return counts

#write the wordlist to a new text file - word and count separated by comma
write_wordcount = counter(words)
outfile = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk_LIST.csv", mode = 'w')

for word, frequency in write_wordcount.items():
	outfile.write(word + " , " + str(frequency) + '\n')

outfile.close()








