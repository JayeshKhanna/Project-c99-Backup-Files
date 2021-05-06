import os
import shutil

source=input("Enter Source folder name")
destination=input("Enter destination folder name")

source=source+'/'
destination=destination+'/'

listOfFiles=os.listdir(source)
print(listOfFiles)
os.rmdir("folderC")

for i in listOfFiles:
    shutil.move((source+i),destination) 

    