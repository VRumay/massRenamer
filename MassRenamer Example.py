"""
MassRenamer is a very simple script that manipulates strings in file names
to massively change names on any number of files in a matter of seconds.

I've been using it to simplify my life when I get hundreds of data sets with
similar names that I need to normalize

"""


import os

currentFiles = os.listdir(r'C:\\Users\\Rumay-Paz\\Desktop\\Recibos y Certificados Acn')

for fileName in currentFiles:
    """ In this example, I have about 100 pdf files with a name structure like 'MM-YY.pdf', I needed to switch the names to 'YY-MM.pdf'"""
    # Make sure the script only runs on files with a hyphen '-' in their name
    if fileName.find('-') != -1:
        currentPath = f'C:\\Users\\Rumay-Paz\\Desktop\\Recibos y Certificados Acn\\{fileName}'
        # Split to get month and name
        month = fileName.split('-')[0]
        year = fileName.split('-')[1].replace('.pdf','')
        # Build the desired structure  with the strings that result from the split
        newFileName = year + '-' + month + '.pdf'
        # Using the os library, change the path of each file to a new file constructed from the previous string syntax. 
        newPath = f'C:\\Users\\Rumay-Paz\\Desktop\\Recibos y Certificados Acn\\{newFileName}'
        os.rename(currentPath,newPath)

