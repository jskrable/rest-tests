# restTest.py
# author: Jack Skrable
# date: 03/22/18
# desc: executes rest call and writes to file

import requests
import json
import os

def main():

	# url to hit on REST get
	url = ''
	# any headers to include with the request
	headers = {}
	
	# get output file
	filename = input("Enter the output file name: ") + ".json"
	
	# show user we're working
	print("Executing...")
	
	# execute get and store in response
	response = requests.get(url, headers = headers)
	
	# print response status code
	print("Status Code: " + str(response.status_code))
	
	# open file for writing
	with open(filename, "w") as outfile:
		#if response 200
		if(response.ok):
			# read response into JSON
			data = json.loads(response.content)
			# dump into file
			json.dump(data, 
				outfile,
				indent = 2, 
				sort_keys = True)
			# display file write success
			print(str(filename) + " write successful")
		# raise alert
		else:
			response.raise_for_status()
	
if __name__ == "__main__":
	main()