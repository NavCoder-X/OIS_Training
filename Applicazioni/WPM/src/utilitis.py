import os
import random

def getRandomFileName():
    listOfFiles = os.listdir("archivio")
    return random.choice(listOfFiles)
