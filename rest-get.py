# rest_test.py
# author: Jack Skrable
# date: 03/22/18
# desc: executes rest GET and writes to file

import requests
import json
import os

def main():

	# url to hit on REST get
	url = input("Enter the URL endpoint: ")
	
	# any headers to include with the request?
	head = input("Are there any headers to include? (Y/n)")
	if head.lower() in ('y','yes'):
		# is it an auth token?
		raw = input("Enter raw header? (Y/n)")
		if raw.lower() in ('y','yes'):
			headers = input("Enter headers: ")
		auth = input("Auth token? (Y/n)")
		if auth.lower() in ('y','yes'):     
			field = 'Authorization'
			value = 'Bearer ' + input("Enter token value: ")
			headers = {field: value}
	
	# get output file
	filename = input("Enter the output file name: ") + ".json"
	
	# show user we're working
	print("Sending request...")
	
	# execute get and store in response
	response = requests.get(url, headers = headers)
	
	while not str(response.status_code):
		counter = 0
		if counter == 1:
			print("/rExecuting.")
		elif counter == 2:
			print("/rExecuting..")
		elif counter == 3:
			print("/rExecuting...")
			counter = 0
		counter+=1
	
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