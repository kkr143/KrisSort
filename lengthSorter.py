#!/usr/bin/python
import os
import sys

#Initialization
#Basic Check to make sure user is passing 2 files as required. one for reading input one for writing output
if not len(sys.argv) == 3:
   print "please specify input and output test file names to the script to execute"
   sys.exit()
infileName = sys.argv[1]
outfileName = sys.argv[2]

def sortFile(infileName,outfileName):
    """
    Function to Sort given file by line length
    @param
    infileName : It is the file containing text to be sorted, mandated to exist
    outfileName : We would write sorted data here, if not exist created.
    @return :
    True on success
    False otherwise
    """

    #Check If infileName exist, else return false and exit
    if infileName is None or not os.path.exists(infileName) or not os.path.isfile(infileName) :
        print "File does not exist, exiting the execution"
        return None
    fileIn = open(infileName, 'r')
    lines = fileIn.read().splitlines()
    linesSorted = sorted(lines, key=len, reverse=True)
    fileOut = open(outfileName,'w')
    for line in linesSorted:
        fileOut.write("%s\n" %line)
    print "Sorted Output written to file", outfileName
    return True

# Actual Script executionstarts here

sortFile(infileName,outfileName)

# cleanUp

