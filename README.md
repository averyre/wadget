# wadget
A multi-platform CLI /idgames client for downloading Doom addons quickly.

Written by Avery Ross using Python3 and the /idgames API.

### Purpose
Ever since using Linux on the daily I've fallen in love with the command line. Package managers from the CLI have been a godsend for installing software, so I decided to try and port the idea to Doom addons.

Doom was a game I fell in love with as a kid, and with this CLI tool you can easily download and search for new levels and files from the /idgames archive as you would apt-get or any other packaging solution. Of course it is a work in progress, but I hope it comes in handy!

### Install
Firstly, clone or download the git repository and navigate to it within a terminal. You MUST have Python3 and pip (3, if necessary to specify on your OS) installed for wadget to function.

Simply run this command from within the root wadget directory. wadget uses Python3, so you must specify pip3 if necessary on your system:
```
$ pip3 install .
```
You can now use wadget from the command line.

#### PyPi
PyPi carries the latest "stable" release of wadget:
```
$ pip3 install wadget
```

### Usage
To get started with basic usage, we can download Community Chest 3 to the working directory using:
```
$ wadget cchest3
```
If we wanted to search for all Community Chest files, or get a specific file ID for download, we can use the -s flag:
```
$ wadget cchest -s
```
This will return:
```
The Community Chest Project
---------------------------
FILE ID: 12021

This is a compilation of levels from the Doom Community

Community Chest 2
-----------------
FILE ID: 13024

Following the success of the original Community Chest, Community Chest 2 is a 32 map megawad including levels made by 26 different authors from the Doom Community. Originally announced almost one year ago in December 2003, it is now complete and ready for your enjoyment.

Community Chest 3
-----------------
FILE ID: 15156

The third installment of the series, Community Chest 3 boasts 32 maps made by 20 different authors from the Doom community. After one year of work, they have been made available for your enjoyment.

Community Chest 4
-----------------
FILE ID: 16911

The fourth installment of the series, Community Chest 4 boasts 32 maps made by 20 different authors from the Doom community. After four years of work, they have been made available for your enjoyment.<br><br> Included in this package is the base resource WAD compiled for the project, which can be found in cc4-tex.zip. It may be a good starting point if you need a large, varied, and meticulously organized texture WAD for your project!

Found 4 matching WAD(s) or file(s) in the /idgames archive.
Use "wadget <FILE ID>" to download.

```
Which provides us with our file ID that can be used as an alternative method to download. Multiple file results can also be displayed at the same time. This method is useful if wadget is downloading the wrong file using a filename.

More specific search features will be introduced later!
