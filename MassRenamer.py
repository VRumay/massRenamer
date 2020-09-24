"""
MassRenamer is a very simple script that manipulates strings in file names
to massively change names on any number of files in a matter of seconds.

I've been using it to simplify my life when I get hundreds of data sets with
similar names that I need to normalize

"""


import os

currentFiles = os.listdir(r'YOURPATH')

for fileName in currentFiles:
    currentPath = f'YOURPATH\\{fileName}'
    newFileName = fileName.replace('02','0-2').replace('37','3-7').replace('','') # Use this variable to modify the existing name or to define a new one.
    newPath = f'YOURPATH\\{newFileName}'
    os.rename(currentPath,newPath)

