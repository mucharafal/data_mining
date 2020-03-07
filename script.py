# Running: python script.py dblp_papers_v11.txt dblb_filtered.txt

import sys
import json
import time

removable_keys = ["page_start", "page_end", "issn", "isbn", "doi", "pdf", "url", "abstract", "indexed_abstract"]

def remove_keys(object):
	filtered_object = object
	
	for key in removable_keys:
		filtered_object.pop(key, None)
	return filtered_object

def readfile(inputFile, outputFile):	
	source = open(inputFile, "r")
	destination = open(outputFile, "w+")
	
	line = source.readline()
	while line:
		object = json.loads(line)
		object = remove_keys(object)
		destination.write(json.dumps(object)+"\n")
		line = source.readline()
	source.close()

if __name__ == "__main__":
	numberOfArguments = len(sys.argv)-1
	
	if numberOfArguments == 0:
		print("no arguments given")
		sys.exit(1)

	inputFile = sys.argv[1]
	outputFile = inputFile + ".out"
	if numberOfArguments >= 2:
		outputFile = sys.argv[2]

	startTime = time.time()
	readfile(inputFile, outputFile)
	print("--- Done - %s seconds ---" % (time.time() - startTime))
