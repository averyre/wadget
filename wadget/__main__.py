import argparse
from .interface import out
from .idgames import callAPI
from .idgames import pingAPI
from .idgames import downloadWAD
from .idgames import searchWAD

# Define the parser to be used from the command line.
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file',
                    help='file ID or name to download. Using a filename will download the first /idgames response result. Use -s to search for IDs, which is recommended.')
parser.add_argument('-s', action='store_true', required=False,
                    help='search the /idgames database for a file ID by filename')
parser.add_argument('-e', action='store_true', required=False,
                    help='extract the selected archive after downloading')


def main():
    # Parse the args and ping the API.
    args = parser.parse_args()
    pingAPI()
    # If the search parameter was passed
    if(args.s):
        searchWAD(args.file, False)
    # If no arguments are passed, try to download the file
    else:
        # Check if we're extracting the archive or not
        if(args.e):
            downloadWAD(args.file, True)
        else:
            downloadWAD(args.file, False)


if(__name__ == '__main__'):
    main()
