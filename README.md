# wadget
A multi-platform CLI /idgames client for downloading Doom addons quickly.

### Purpose
Ever since using Linux on the daily I've fallen in love with the command line. Package managers from the CLI have been a godsend for installing software, so I decided to try and port the idea to Doom addons.

Doom was a game I fell in love with as a kid, and with this CLI tool you can easily download and search for new levels and files from the /idgames archive as you would apt-get or any other packaging solution. Of course it is a work in progress, but I hope it comes in handy!

### Install
Firstly, clone or download the git repository and navigate to it within a terminal. You MUST have Python3 and pip (3, if necessary to specify on your OS) installed for wadget to function.

Simply run this command from within the root wadget directory:
```
pip3 install .
```
You can now use wadget from the command line.

If you'd rather use PyPi, I cannot gurantee how up to date that version will be. At your own discretion you can also use:
```
pip3 install wadget
```

### Usage
To get started with basic usage, we can download the original Doom shareware to the working directory using:
```
wadget 7043
```
This is all well and good if we know the WAD ID associated with the WAD we'd like. Luckily, wadget has a search function to scrape WAD IDs from /idgames. Let's try:
```
wadget doom19s -s
```
This will return:
```
DOOM v1.9 - Shareware
WAD ID: 7043

 This is the latest and FINAL version of DOOM, version 1.9.  This version
has various bug fixes, includes the new DM.EXE (DeathManager) shell,
the new DWANGO.EXE app, rewritten SETUP.EXE and slightly modified
SERSETUP and IPXSETUP programs. Read the DM.DOC and DWANGO.DOC on
information about the new programs.  Also included is the quite awesome
DOOM FAQ v6.666!  Read it and weep!

Found 1 matching WAD(s) or file(s) in the /idgames archive.
Use "wadget <WAD ID>" to download.
```
Which provides us with our WAD ID needed to download. The "-s" flag lets wadget know we are searching /idgames, not downloading from it. Multiple file results can also be displayed at the same time.

More specific search features will be introduced later!
