#!/bin/python3
​
#Store Tenable.io API Keys in Memory
akey = input('Access Key: ')
skey = input('Secret Key: ')
​
#Using pyTenable, set up the API connection
from tenable.io import TenableIO
tio = TenableIO(akey, skey)
​
#Accept a list of plugin ID's
pstring = input("enter plugin list (example: [19506, 16702]): ")
​
#Specify the string you're looking for in URLs
  #(Case sensitive and doesn't support regex...yet)
searchString = input("Enter a search string to look for in URLs: ")
​
#Remove the brackets and parse string to a list
plist = pstring.strip('][').split(', ')
​
#loop through plugins in list
for i in plist:
​
    #Query Tenable.io for plugin attributes
	attributes=tio.plugins.plugin_details(i)['attributes']
​
	#If a CVSSv2 Base score is present, print that out
	  #otherwise, print out that there was none.
	if "see_also" in str(attributes):
		seeAlso=(str([a['attribute_value'] for a in attributes if a['attribute_name']=='see_also']) [2:-2])
		if searchString in seeAlso:
			seeAlso = seeAlso.split('\\n')
			for link in seeAlso:
				#print(link)
				if searchString in link:
					print(i, "===== ", link)
		else:
			print('No', searchString, 'links for plugin ', i)
	else:
		print('no see also section for plugin', i)
