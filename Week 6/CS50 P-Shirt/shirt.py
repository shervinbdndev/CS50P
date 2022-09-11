import os
import sys
from PIL import (Image , ImageOps)


def main():
    checkCommandLineArgument()
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    shirtFile = Image.open('shirt.png')
    size = shirtFile.size
    muppet = ImageOps.fit(imageFile , size)
    muppet.paste(shirtFile , shirtFile)
    muppet.save(sys.argv[2])




def checkCommandLineArgument():
    if (len(sys.argv) < 3):
        sys.exit('Too few command-line arguments')
    if (len(sys.argv) > 3):
        sys.exit('Too many command-line arguments')
    file1 = os.path.splitext(sys.argv[1])
    file2 = os.path.splitext(sys.argv[2])
    if (checkExtensions(file1[1]) == False):sys.exit('Invalid input')
    if (checkExtensions(file2[1]) == False):sys.exit('Invalid input')
    if (file1[1].lower() != file2[1].lower()):sys.exit('Input and output have different extensions')



def checkExtensions(file):
    if (file in ['.jpg' , '.jpeg' , '.png']):
        return True
    return False



if __name__ == '__main__':
    main()