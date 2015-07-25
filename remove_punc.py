infile = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk.txt")
text = infile.read()
infile.close()

def remove_punc(text):
	punctuation = '!@#$%^&*()_-+={}[]:;"|<>,.?/~`-\''
	clean_text = "  "
	for character in text:
		if character not in punctuation:
			clean_text += character
	return clean_text

new_text = remove_punc(text)   #removes punctuation

print(new_text)

newfile = open("/Users/default/Desktop/july15pilot/Greece/UK_content/combined_uk_nopunc.txt", mode = "w")
	
for item in new_text:
	newfile.write(item)