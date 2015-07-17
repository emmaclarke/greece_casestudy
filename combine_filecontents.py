#to combine multiple files in a dir into 1 large .txt file

import fileinput        #Iterate over lines from multiple input streams
import glob 			#Return a possibly-empty list of path names that match pathname, 
						#which must be a string containing a path specification

file_list = glob.glob("*.txt")

with open('combined_uk.txt', 'w') as file:			#new txt file is combined_uk.txt
	input_lines = fileinput.input(file_list)
	file.writelines(input_lines)					#writes all lines to new .txt 