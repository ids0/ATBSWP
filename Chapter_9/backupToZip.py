#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os 

def backupToZip(folder):
    #Backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder)    # make sure folder is absolute