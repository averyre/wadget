import requests
import zipfile
import os
from os import path
import urllib.request
from .interface import out
from .interface import horizontalLine
from .interface import ynPrompt

# The /idgames API path

IDGAMES_API = 'https://www.doomworld.com/idgames/api/api.php?action='

# /idgames mirrors to be used when downloading

TEXAS_MIRROR = 'http://ftp.mancubus.net/pub/idgames/'
NEWYORK_MIRROR = 'http://youfailit.net/pub/idgames/'
GREECE_MIRROR = 'http://ftp.ntua.gr/pub/vendors/idgames/'

# Returns a requests response object after passing an action to the /idgames API


def callAPI(action):
    response = requests.get(IDGAMES_API + action + '&out=json')
    return response

# A function to ping the /idgames API


def pingAPI():
    out('Contacting /idgames API...')
    pingResponse = callAPI('ping')
    pingData = pingResponse.json()
    if(str(pingData['content']['status']) == 'true'):
        out('/idgames API pinged successfully!')
    else:
        out('Failed to contact the /idgames API! Exiting...')
        exit()


# Function to download a WAD using it's ID or filename

def downloadWAD(fileInput, extractArchive):
    # The mirror of /idgames to use
    selectedMirror = TEXAS_MIRROR

    # Check if we have a file ID or archive name
    if(fileInput.isdigit()):
        fileID = fileInput
        isfileID = True
    else:
        isfileID = False
        # Append '.zip' if filename is less than 3 characters
        if(len(fileInput) < 3):
            fileInput += '.zip'

    # Handle it appropriately
    out('Contacting /idgames for file data...')
    if(isfileID):
        wadResponse = callAPI('get' + '&id=' + fileID)
    else:
        wadResponse = callAPI('get' + '&id=' + searchWAD(fileInput, True))

    # Check the response for if the file ID is bad
    if('Bad Id' in str(wadResponse.json())):
        out('Bad file ID! Nothing to download.')
        exit()

    wadData = wadResponse.json()
    fileName = str(wadData['content']['filename'])
    wadPath = str(wadData['content']['dir']) + fileName
    wadName = str(wadData['content']['title'])

    out(wadName + ' was selected.')

    # Check if the file exists and prompt to overwrite
    if(path.exists(fileName)):
        if(ynPrompt('A file with the name ' + fileName + ' already exists in this directory. Would you like to overwrite it?')):
            out(fileName + ' will be overwritten.')
        else:
            out('Exiting...')
            exit()

    # Download the file
    out('Downloading ' + fileName + '...')
    urllib.request.urlretrieve(selectedMirror + wadPath, fileName)

    # Extract it if specified
    if(extractArchive):
        # Unpack it
        out('Extracting ' + fileName + '...')
        packedFile = zipfile.ZipFile(fileName)
        packedFile.extractall('.')
        packedFile.close()

        # Clean up
        out('Removing leftover archive...')
        os.remove(fileName)

    out('Done.')


# Function to search /idgames by filename


def searchWAD(fileName, returnfirstFile):
    # Append '.zip' if filename is less than 3 characters
    if(len(fileName) < 3):
        fileName += '.zip'

    out('Contacting /idgames for search query...')
    searchResponse = callAPI('search' + '&query=' + fileName)
    searchData = searchResponse.json()

    # We have to search the json for 'filename' strings to get how many files there are in the response
    resultPoint = 0
    resultsReturned = 0
    resultsCounting = True

    out('Parsing /idgames search response...')
    # resultsReturned will count every 'filename' in the JSON response
    while(resultsCounting):
        searchString = str(searchResponse.json())
        resultCount = searchString.find('\'filename\': ', resultPoint)
        if resultCount == -1:
            resultsCounting = False
        else:
            resultsReturned += 1
            resultPoint = resultCount + 1

    # If we're only returning the first file, don't output anything
    if(returnfirstFile == True):
        # If no file is found, exit
        if(resultsReturned == 0):
            out('No file found for query: ' + fileName)
            exit()
        else:
            # Return the first file ID
            if(resultsReturned != 1):
                fileID = str(searchData['content']['file'][0]['id'])
            else:
                fileID = str(searchData['content']['file']['id'])
            return fileID
    else:
        # We only need to display one if multiple are not returned
        out('')
        if(resultsReturned != 1):
            resultCount = 0
            while(resultCount < resultsReturned):
                out('')
                out(searchData['content']['file'][resultCount]['title'])
                out(horizontalLine(
                    len(str(searchData['content']['file'][resultCount]['title']))))
                out("FILE ID: " +
                    str(searchData['content']['file'][resultCount]['id']))
                out('\n' + str(searchData['content']
                               ['file'][resultCount]['description']))
                resultCount += 1
        else:
            out(searchData['content']['file']['title'])
            out(horizontalLine(
                len(str(searchData['content']['file']['title']))))
            out("FILE ID: " + str(searchData['content']['file']['id']))
            out('\n' + str(searchData['content']['file']['description']))

        out('\nFound ' + str(resultsReturned) +
            ' matching WAD(s) or file(s) in the /idgames archive.')
        out('Use "wadget <FILE ID>" to download.\n')
