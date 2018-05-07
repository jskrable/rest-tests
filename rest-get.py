# rest_test.py
# author: Jack Skrable
# date: 03/22/18
# desc: executes rest GET and writes to file

import requests
import json
import os
import threading


def working(status):

	while not status:
		counter = 0
		if counter == 0 :
			print("Executing", end='/r')
			counter+=1
		elif counter == 1:
			print("/rExecuting.", end='/r')
			counter+=1
		elif counter == 2:
			print("/rExecuting..", end='/r')
			counter+=1
		elif counter == 3:
			print("/rExecuting...", end='/r')
			counter = 0		
	
	return


def main():

	# url to hit on REST get
	url = input("Enter the URL endpoint: ")
	
	# any headers to include with the request?
	head = input("Are there any headers to include? (Y/n)")
	if head.lower() in ('y','yes'):
		# is it an auth token?
		auth = input("Auth token? (Y/n)")
		if auth.lower() in ('y','yes'):
			field = 'Authorization'
			value = 'Bearer ' + input("Enter token value: ")
		# elif headers = {input("Enter raw headers: ")}
				
	# create header dict
	headers = {field: value}
	
	# get output file
	filename = input("Enter the output file name: ") + ".json"
	
	# show user we're working
	print("Sending request...")
	
	# init response
	status = False
	
	# start working animation in new thread
	w = threading.Thread(target=working, args=(status,))
	w.setDaemon(True)
	w.start()
	
	# execute get and store in response
	response = requests.get(url, headers = headers)
	status = True
	
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