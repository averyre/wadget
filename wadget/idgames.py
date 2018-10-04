import requests
import json
import urllib.request
from .interface import out

# The /idgames API path

IDGAMES_API = 'https://www.doomworld.com/idgames/api/api.php?action='

# idgames mirrors to be used when downloading

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


# Function to download a WAD using it's ID

def downloadWAD(wadID):
    # The mirror of idgames to use
    selectedMirror = TEXAS_MIRROR

    # Find the WAD by ID and construct the name and path
    wadResponse = callAPI('get' + '&id=' + wadID)
    wadData = wadResponse.json()
    fileName = str(wadData['content']['filename'])
    wadPath = str(wadData['content']['dir']) + fileName

    # Download the file
    urllib.request.urlretrieve(selectedMirror + wadPath, fileName)

# Function to search for a WAD by filename


def searchWAD(fileName):
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
        resultCount = searchString.find('filename', resultPoint)
        if resultCount == -1:
            resultsCounting = False
        else:
            resultsReturned += 1
            resultPoint = resultCount + 1

    # We only need to display one if multiple are not returned
    out('')
    if(resultsReturned != 1):
        resultCount = 0
        while(resultCount < resultsReturned):
            out('')
            out(searchData['content']['file'][resultCount]['title'])
            out("WAD ID: " + str(searchData['content']['file'][resultCount]['id']))
            out('\n ' + str(searchData['content']['file'][resultCount]['description']))
            resultCount += 1
    else:
        out(searchData['content']['file']['title'])
        out("WAD ID: " + str(searchData['content']['file']['id']))
        out('\n ' + str(searchData['content']['file']['description']))

    out('\nFound ' + str(resultsReturned) + ' matching WAD(s) or file(s) in the /idgames archive.')
    out('Use "wadget <WAD ID>" to download.\n')
