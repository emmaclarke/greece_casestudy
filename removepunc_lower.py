infile = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk.txt")
text = infile.read()
infile.close()

#function split operates on a string and splits a string on spaces and returns a list of smaller strings (or words):
#print(text.split())

def remove_punc(text):
	punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`-'
	clean_text = ""
	for character in text:
		if character not in punctuation:
			clean_text += character
	return clean_text

new_text = remove_punc(text.lower())   #removes punctuation and makes everything lowercase

print(new_text)







