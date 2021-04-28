#%%
# This program is intended to:
# Merge monthly financial statements from Sage (PDF's), in order of section name
# Developed by Adam Amodio, 2021 for the Oregon State Bar

# Import libraries
import logging
import PyPDF2
import tkinter as tk
from tkinter import filedialog as fd

# Start program
print("\n#####################################################\nStarting program...\n")
logging.info('Program started.')

# Setup UI
#window = tk.Tk()
#window.title("parse-sage-pdfs.py")
#width = 400
#height = 500
#x_pos = 300
#y_pos = 300
#geometry_string = "{}x{}+{}+{}".format(width, height, x_pos, y_pos)
#window.geometry(geometry_string)
# Create widgets here
#window.mainloop()

# Define parseMSF()
#def parseMSF():


# Ask user to select files to process
print("Select one or more files to be processed.")
filenames = fd.askopenfilenames()
print(filenames)
logging.info('Files Selected.')

# Parse 'filesnames'
#pdfFileObjs = list()
#for file in range(len(filenames)):
#    pdfFileObjs.append(PyPDF2.PDFFileReader(file))

#pdfFileObj = open(file,'rb')
#pdfReader = PyPDF2.PDFFileReader(pdfFileObj)
#pageCount = pdfReader.numPages
#print(pageCount)
#    parseMSF() for each file



pdfFilename = '2021-02-Section-SOA.pdf'
print("Current File: " + pdfFilename)

print("Reading File...")
pdfFileObj = open(pdfFilename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Extract number of pages
print("\nCounting Pages...")
pageCount = pdfReader.numPages
print("Page Count: " + str(pageCount))

# Should this section be moved out of scope? 
print("\nAnalyzing current page order...")
currentPageOrderFromAptify = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848]
currentPageOrder = []
print(currentPageOrderFromAptify)

# Iterate through the document page by page
print("\nReading all pages...")
i = 0
for i in range(pageCount):
    currentPage = pdfReader.getPage(pageCount - (pageCount - i))

    # Extract current page department number (i.e. section number)
    currentPageText = currentPage.extractText()
    currentPageDept = currentPageText.splitlines()[-4:]
    print("(Page " + str(i) + " of " + str(pageCount) + "):" + str(currentPageDept))

# Set array of current page numbers with section department codes (ex. "802","etc")


# TODO: Output desired PDF
# Set array of desired page numbers
print("\nSetting desired page order...")
desiredPageOrder = [844,801,837,802,834,803,804,805,806,807,848,808,841,810,838,836,811,812,826,845,842,824,813,814,815,816,817,833,823,818,843,819,820,821,822,847,832,846,839,829,825,827,840,835,828,809,830]
print(desiredPageOrder)

print("\nPrinting to file...")

# TODO: add pages to pdf
#PyPDF2.PdfFileWriter.addPage()

# TODO: save pdf


# TODO: distribute pdf
outputFilename = "click to open pdf"
print("Output filename: " + outputFilename)

# Close PDF
print("\nClosing program...\n-----------------------------------------------------")
pdfFileObj.close()