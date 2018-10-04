import argparse
from .interface import out
from .idgames import callAPI
from .idgames import pingAPI
from .idgames import downloadWAD
from .idgames import searchWAD

# Define the parser to be used from the command line.
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file',
                    help='File ID to download. Use -s to find one.')
parser.add_argument('-s', action='store_true', required=False,
                    help='Search for a file ID by filename')


def main():
    # Parse the args and ping the API.
    args = parser.parse_args()
    pingAPI()
    # If the search parameter was passed
    if(args.s):
        searchWAD(args.file)
    # If no arguments are passed, try to download the wad by ID
    else:
        downloadWAD(args.file)


if(__name__ == '__main__'):
    main()
