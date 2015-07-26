from bs4 import BeautifulSoup

#works for UK, but not for IRL - 

import requests

url = "http://www.oireachtas.ie/parliament/education/glossary/"
req = requests.get(url)

soup = BeautifulSoup(req.content)

#print(soup.prettify)   #shows the html in an easy to read format

#links = soup.find_all("a")  #finds all links or anchor tags

#for link in links:
#	if "http" in link.get("href"):
#	print "<a href='%s'>%s</a>" %(link.get("href"), link.text) #gets all the hyperlinks & the text associated with them

general_data = soup.find_all("h2")  #gives all of the <h2> in the context of IRL

with open("/Users/default/Desktop/july15pilot/Greece/IRL_content/glossary.txt", mode = "w") as f:
	for item in general_data:
		f.write(item.text.encode("utf-8"))


