
"""from PIL import Image
import os

# Set the input and output folder paths
input_folder = 'C:\\Users\\dell\\Desktop\\output'
output_folder = 'C:\\Users\\dell\\Desktop\\inverted'

# Set the DPI and resolution for the PDF
dpi = 300
resolution = (1920, 1080)

# Get a list of all the image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# Create a list to hold the image objects
images = []

# Open each image file and add it to the list of images
for image_file in image_files:
    image = Image.open(os.path.join(input_folder, image_file))
    images.append(image)

# Create the PDF
pdf_file = Image.new("RGB", resolution, (255, 255, 255))
pdf_file.save(os.path.join(output_folder, 'output.pdf'), save_all=True, append_images=images, dpi=(dpi, dpi))
"""

from PIL import Image
import os
from tqdm import tqdm
from natsort import natsorted

# Set the input and output folder paths
input_folder = 'C:\\Users\\dell\\Desktop\\output'
output_folder = 'C:\\Users\\dell\\Desktop\\inverted'

# Set the DPI and resolution for the PDF
dpi = 300
resolution = (1920, 1080)

# Get a list of all the image files in the input folder
image_files = natsorted([f for f in os.listdir(input_folder) if f.endswith('.jpg')])

# Create a list to hold the image objects
images = []

# Open each image file and add it to the list of images
for image_file in tqdm(image_files, desc='Processing images'):
    image = Image.open(os.path.join(input_folder, image_file))
    images.append(image)

# Create the PDF
pdf_file = Image.new("RGB", resolution, (255, 255, 255))
pdf_file.save(os.path.join(output_folder, 'output.pdf'), save_all=True, append_images=images, dpi=(dpi, dpi))


import os
import shutil
folder_path = 'C:\\Users\\dell\\Desktop\\input' # replace with the actual path to the folder

for root, dirs, files in os.walk(folder_path):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))

folder_path = 'C:\\Users\\dell\\Desktop\\output' # replace with the actual path to the folder

for root, dirs, files in os.walk(folder_path):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))

