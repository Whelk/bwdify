#! /usr/bin/python3

from PIL import Image
import os, sys, pathlib



args = sys.argv

pathy = os.getcwd()

if len(args) < 2:
    print("Sepcify which file you wish to convert to a black-and-white dithered image.")
    quit()

imgfile = args[1]

extension = pathlib.Path(imgfile).suffix
accepted_types = ['.jpg','.jpeg','.png','.gif']
if extension not in accepted_types:
    print(f"Invalid file: {imgfile}\nPlease provide an image file of one of the following types: {' '.join(accepted_types)}")
    quit()

print(f"You will bwdify {imgfile}!")

#read the image from path
image = Image.open(f'{pathy}/{imgfile}')
 
#Convert it into the grayscale image
#grayscale = image.convert('L')
 
#Converting the same image to black and white mode
BW= image.convert('1')
 
#save both the images
#grayscale.save("grayscale_image.jpg")
newfile = f"{pathy}/BW_{imgfile}"
BW.save(newfile)
print(f"Saved BWD-ified image to: {newfile}")