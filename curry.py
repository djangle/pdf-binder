# Import libraries
import os
#from dataclasses import dataclass
import datetime
from PyPDF2 import PdfFileMerger, PdfFileReader
import tkinter as tk
from tkinter import Label, Menu, messagebox, filedialog as fd
import PyPDF2

# Set app info (do I need a class for this?)
class app():
    name = "Curry"
    version = "0.3"
    aka = "Headless Horseman"
    readme = "Program runs with minimal user interface (i.e. headless)"
    author = "Adam Amodio"
    lastUpdate = "2021"

app = app()

# Start program
# TODO: Print log to a widget in tk (scrollingText?)
# Set program start time
startTime = str(datetime.datetime.now())
print("\n#####################################################\nStarting program... \nNow: " + startTime)

# Configure the UI
ws = tk.Tk()
ws.title(app.name)
# TODO: Rewrite the following with Canvas.Tk()
width = 275
height = 200
x_pos = 300
y_pos = 100
geometry_string = "{}x{}+{}+{}".format(width, height, x_pos, y_pos)
ws.geometry(geometry_string)

# TODO: Define PDF Document (input files, and output file?)
# Define a class?
# Define a function?
#def runProgram():
# TODO: Make a UI
logText = "Making the curry...\n\n"
log = tk.Label(text = logText)
log.grid(column=0,row=0)

print("INSTRUCTIONS: Select two PDF files: 1) month end SOA, 2) month end detail")
# fd.askopenfilename() for one file
# fd.askopenfilenames() for multiple files)
files = fd.askopenfilenames()
#os.system('cmd /k "explorer /select"')
print("Opening Files: " + str(files))

# TODO: Use CMD line?
#os.system('cmd /k "echo start"')
#os.system('cmd /k "echo filenames"')

#TODO: Create functions and classes?
#def parse():
fileCount = 0
print("Loading files...")
filenames = list(files)

for file in filenames:
    fileCount += 1

# TODO: Load each file in filenames to a separate object using a loop
file1 = filenames[0]
file2 = filenames[1]
print("Filenames split")
print("Filename 1: " + file1)
print("Filename 2: " + file2)

fileObj1 = open(file1,'rb')
fileObj2 = open(file2, 'rb')
print("Files opened as objects")

# TODO: Read each file using a loop
pdf1 = PyPDF2.PdfFileReader(fileObj1)
pdf2 = PyPDF2.PdfFileReader(fileObj2)
print("Files read as PDF's")

print("File Count: " + str(fileCount))
# TODO: Display error if filecount is not equal to two

# TODO: Display file info (filenames, # of files, # of pages per file)
#print("Files Opened: " + str(filenames))
# Extract number of pages
#print("\nCounting Pages...")
#pageCount = pdf.numPages
#print("Page Count: " + str(pageCount))

# TODO: Scan files being parsed for actual page order
#print("\nAnalyzing current page order...")
# # This page order is from the PDF: smallest to largest section code
print("Analyzing current page order... (smallest to largest section code)\n")
currentPageOrder = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848]
print(currentPageOrder)

# TODO: Set array of current page numbers with section department codes (ex. "802","etc")
# This page order is from Aptify: alphabetically by committee name
print("Setting desired page order... (alphabetically by committee name)\n")
desiredPageOrder = [844,801,837,802,834,803,804,805,806,807,848,808,841,810,838,836,811,812,826,845,842,824,813,814,815,816,817,833,823,818,843,819,820,821,822,847,832,846,839,829,825,827,840,835,828,809,830]
print(desiredPageOrder)

# TODO: Merge files
# Not guna help: >>>>pdfcat [-h] [-o output.pdf] [-v] input.pdf [page_range...] ...
# Not guna help: pdfcat document-output.pdf filenames[0] 1::2
#option1: combine both files then merge(1:50:2), ex. first of each document thru last after being appended
#option2: setup objects for each pdf and read from each into a new file, seems hard -- started above but not finished
#trying option2
# TODO: Try option1
#outfile = PdfFileMerger.append(file1)
#outfile = PdfFileMerger.append(file2)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Iterate through the document page by page
print("Reading all pages...\n")
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2.numPages):
    pageObj = pdf2.getPage(pageNum)
    pdfWriter.addPage(pageObj)

print("Printing 'merged-files.pdf'...\n")
pdfOutputFile = open('merged-files.pdf','wb')
pdfWriter.write(pdfOutputFile)
print("Print complete. Check the folder!")

# TODO: Extract current page department number (i.e. section number) from header
#    currentPageText = currentPage.extractText()
#    currentPageDept = currentPageText.splitlines()[-4:]
#    print("(Page " + str(i) + " of " + str(pageCount) + "):" + str(currentPageDept))

# TODO: Create bookmarks
# TODO: Make the program more modular. A relic of version 0.2 ...
#runProgram()

# TODO: IMPORTANT!!! Close all files
pdfOutputFile.close()
fileObj1.close()
fileObj2.close()


# Display info via the 'About' menu option
def about():
    messagebox.showinfo(app.name,"Hello World!\n\n" + "\nVersion: " + app.version + "\nAuthor: " + app.author)

## Setup menu bar
menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
# File Menu
file = Menu(menubar, tearoff=0, foreground='black')  
#file.add_command(label="New")
#file.add_command(label="Open Files", command=open())
#file.add_command(label="Parse", command=parse())
#file.add_command(label="Save")
#file.add_command(label="Save as")
#file.add_separator()
file.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="File", menu=file)
# Edit Menu
#edit = Menu(menubar, tearoff=0)
#edit.add_command(label="Undo")
#edit.add_separator()
#edit.add_command(label="Cut")
#edit.add_command(label="Copy")
#edit.add_command(label="Paste")
#menubar.add_cascade(label="Edit", menu=edit)
# Help Menu
help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help)
# End menu setup
ws.config(menu=menubar)

# TODO: Play around with Turtle
#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

# End UI Setup
ws.mainloop()

# Close program
print("\nClosing program...\n-----------------------------------------------------")

# Goodbye
print("Goodbye")