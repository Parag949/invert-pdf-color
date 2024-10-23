"""
#extract images
import os
from PyPDF4 import PdfFileReader
from wand.image import Image

# path to the pdf file
pdf_path = input('pdfpath')

# open the pdf
pdf = PdfFileReader(open(pdf_path, "rb"))

# specify the DPI for the output images
dpi = 300

# user-specified output folder
output_folder = "C:\\Users\\dell\\Desktop\\input"

# loop through all pages in the pdf
for i in range(pdf.getNumPages()):
    # get the current page
    page = pdf.getPage(i)
    # create an image object
    with Image(filename=pdf_path+"[{}]".format(i), resolution=dpi) as img:
        # specify the output image file name
        img_file = "page_{}.jpg".format(i)
        # generate the output path
        output_path = os.path.join(output_folder, img_file)
        # save the image to disk in jpeg format
        img.save(filename=output_path)



"""



import os
from tkinter import *
from tkinter import filedialog
from PyPDF4 import PdfFileReader
from wand.image import Image
from tkinter import ttk

def extract_images():
    global pdf_path
    pdf_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf = PdfFileReader(open(pdf_path, "rb"))
    # specify the DPI for the output images
    dpi = 200
    # user-specified output folder
    output_folder = "C:\\Users\\dell\\Desktop\\input"
    progress_bar.config(maximum = pdf.getNumPages())
    for i in range(pdf.getNumPages()):
        # get the current page
        page = pdf.getPage(i)
        # create an image object
        with Image(filename=pdf_path+"[{}]".format(i), resolution=dpi) as img:
            # specify the output image file name
            img_file = "page_{}.jpg".format(i)
            # generate the output path
            output_path = os.path.join(output_folder, img_file)
            # save the image to disk in jpeg format
            img.save(filename=output_path)
            progress_bar.step(1)
            root.update()

root = Tk()
root.title("PDF Image Extractor")
root.geometry("300x150")

# Create a label for the PDF file path
label = Label(root, text="PDF File:")
label.pack(pady=10)

# Create a button to open a file dialog
browse_button = Button(root, text="Browse", command=extract_images)
browse_button.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient = "horizontal", length = 280, mode = "determinate")
progress_bar.pack(pady=10)

root.mainloop()
