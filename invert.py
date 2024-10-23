


"""#invert
from PIL import Image,ImageOps
import os

# specify the directory containing the images
folder = "C:\\Users\\dell\\Desktop\\input"

# specify the DPI for the output images
dpi = (300, 300)

# loop through the images in the directory
for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        # open the image
        image = Image.open(os.path.join(folder, filename))
        # invert the colors
        inverted_image = ImageOps.invert(image)
        # set the DPI of the inverted image
        inverted_image.info['dpi'] = dpi
        # save the inverted image with high quality
        inverted_image.save(os.path.join('C:\\Users\\dell\\Desktop\\output', "inverted_" + filename), "JPEG", quality=95, dpi=dpi)
"""

from PIL import Image, ImageOps
import os
from tqdm import tqdm

# specify the directory containing the images
folder = "C:\\Users\\dell\\Desktop\\input"

# specify the DPI for the output images
dpi = (300, 300)

# loop through the images in the directory
for filename in tqdm(os.listdir(folder)):
    if filename.endswith(".jpg"):
        # open the image
        image = Image.open(os.path.join(folder, filename))
        # invert the colors
        inverted_image = ImageOps.invert(image)
        # set the DPI of the inverted image
        inverted_image.info['dpi'] = dpi
        # save the inverted image with high quality
        inverted_image.save(os.path.join('C:\\Users\\dell\\Desktop\\output', "inverted_" + filename), "JPEG", quality=95, dpi=dpi)
