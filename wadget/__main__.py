import argparse
from .interface import out
from .idgames import callAPI
from .idgames import pingAPI
from .idgames import downloadWAD
from .idgames import searchWAD

# Define the parser to be used from the command line.
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file',
                    help='File ID or name to download. Using a filename will download the first /idgames response result. Use -s to search for IDs, which is recommended.')
parser.add_argument('-s', action='store_true', required=False,
                    help='Search the /idgames database for a file ID by filename')


def main():
    # Parse the args and ping the API.
    args = parser.parse_args()
    pingAPI()
    # If the search parameter was passed
    if(args.s):
        searchWAD(args.file, False)
    # If no arguments are passed, try to download the file
    else:
        downloadWAD(args.file)


if(__name__ == '__main__'):
    main()
