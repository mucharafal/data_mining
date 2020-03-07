# Running: python slicer.py dblp_papers_v11.txt dblp_part

import sys
import json
import time

def rewriteNLines(source, destination, n):	
	line = source.readline()
	lineCounter = 0
	while line and lineCounter < n:
		destination.write(line+"\n")
		lineCounter += 1
		line = source.readline()
	return lineCounter == n

def partitionFile(sourceFilename, partFilenamePrefix, partSize):
    filesCounter = 0
    partFilename = partFilenamePrefix + str(filesCounter) + ".out"

    inputFileHandler = open(sourceFilename, "r")
    outputFileHandler = open(partFilename, "w+")

    while rewriteNLines(inputFileHandler, outputFileHandler, partSize):
        outputFileHandler.close()
        filesCounter += 1
        outputFilename = partFilenamePrefix + str(filesCounter) + ".out"
        outputFileHandler = open(outputFilename, "w+")


if __name__ == "__main__":
	numberOfArguments = len(sys.argv)-1
	
	if numberOfArguments != 2:
		print("Bad number of arguments: " + str(numberOfArguments))
		sys.exit(1)

	inputFilename = sys.argv[1]
	partPrefix = sys.argv[2]

	startTime = time.time()

	partitionFile(inputFilename, partPrefix, 100000)

	print("--- Done - %s seconds ---" % (time.time() - startTime))
