import argparse
from .interface import out
from .idgames import callAPI
from .idgames import pingAPI
from .idgames import downloadWAD
from .idgames import searchWAD

# Define the parser to be used from the command line.
parser = argparse.ArgumentParser()
parser.add_argument('wad', metavar='WAD',
                    help='WAD ID to download. Use -s to find one.')
parser.add_argument('-s', action='store_true', required=False,
                    help='Search for a WAD ID by filename')


def main():
    # Parse the args and ping the API.
    args = parser.parse_args()
    pingAPI()
    # If the search parameter was passed
    if(args.s):
        searchWAD(args.wad)
    # If no arguments are passed, try to download the wad by ID
    else:
        downloadWAD(args.wad)
    # 15156 test wad.


if(__name__ == '__main__'):
    main()