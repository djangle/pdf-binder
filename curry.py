# Import libraries
import os
import datetime
from PyPDF2 import PdfFileMerger, PdfFileReader
import tkinter as tk
from tkinter import Label, Menu, messagebox, filedialog as fd
import PyPDF2

# Set app info (do I need a class for this? Still learning classes...)
class app():
    name = "Curry"
    version = "0.1 'Ocre'"
    aka = "Headless Horseman"
    readme = "Program runs with minimal user interface (i.e. headless)"
    author = "Adam Amodio"

app = app()

# TODO: Print live log (CLI?) to a widget in tk
# Start program
startTime = str(datetime.datetime.now())
print("\n#####################################################\nStarting program... \nNow: " + startTime)

# TODO: Make a UI
ws = tk.Tk()
ws.title(app.name)
# TODO: Rewrite the following with Canvas.Tk()
width = 275
height = 200
x_pos = 300
y_pos = 100
geometry_string = "{}x{}+{}+{}".format(width, height, x_pos, y_pos)
ws.geometry(geometry_string)

# TODO: Prepare to output a log file
logText = "Making the curry..."
log = tk.Label(text = logText)
log.grid(column=0,row=0)
#log.pack()

# TODO: Play around with Turtle, might be a nice progress bar
# TODO: import only what I need from turtle
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

files = fd.askopenfilenames()
print("Opening Files: " + str(files))

fileCount = 0
print("Loading files...")
filenames = list(files)

for file in filenames:
    fileCount += 1

# TODO: Validate two files were selected
# TODO: Display error if filecount is not equal to two
print("File Count: " + str(fileCount))

# Load each file in filenames to a separate object using a loop
file1 = filenames[0]
file2 = filenames[1]

# Print each filename
print("Filenames split...")
print("Filename 1: " + file1)
print("Filename 2: " + file2)

# Open each file
print("Opening files...")
fileObj1 = open(file1,'rb')
fileObj2 = open(file2, 'rb')
print("Files opened as objects.")

# TODO: Read each file using a loop
# TODO: Display each file info
print("Read files as PDF's...")
pdf1 = PyPDF2.PdfFileReader(fileObj1)
pdf2 = PyPDF2.PdfFileReader(fileObj2)
print("Files read as PDF's.")


# TODO: Scan files being parsed for actual page order
#print("Analyzing current page order...")
# # This page order is from the PDF: smallest to largest section code
#print("Reading current page order... (smallest to largest section code)")
#currentPageOrder = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848]
#print(currentPageOrder)

# TODO: Set array of current page numbers with section department codes (ex. "802","etc")
# This page order is from Aptify: alphabetically by committee name
#print("Setting desired page order... (alphabetically by committee name)")
#desiredPageOrder = [844,801,837,802,834,803,804,805,806,807,848,808,841,810,838,836,811,812,826,845,842,824,813,814,815,816,817,833,823,818,843,819,820,821,822,847,832,846,839,829,825,827,840,835,828,809,830]
#print(desiredPageOrder + "\n\n")

# TODO: Test dictionaries for section/page num correlation
#print("\n\nWorking with dictionaries...")
#pOrd = {}
#for i in desiredPageOrder:
#    pOrd[desiredPageOrder[i]]
#pOrd['844'] = 23
#print(pOrd)

# Prepare to write output file
pdfWriter = PyPDF2.PdfFileWriter()

# Method 1: Merge back to back --- THIS WORKS! Combine PDF's 1+2
#for pageNum in range(pdf1.numPages):
#    pageObj = pdf1.getPage(pageNum)
#    pdfWriter.addPage(pageObj)

#for pageNum in range(pdf2.numPages):
#    pageObj = pdf2.getPage(pageNum)
#    pdfWriter.addPage(pageObj)
####


# Method 2: Cherry pick pages --- THIS WORKS! Shuffle PDF's 1/1, 2/2, 3/3, ...
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pageObj = pdf2.getPage(pageNum)
    pdfWriter.addPage(pageObj)


# TODO: Create bookmarks

# Write the output file
print("Printing 'merged-files.pdf'...")
pdfOutputFile = open('merged-files.pdf','wb')
pdfWriter.write(pdfOutputFile)

# IMPORTANT!!! Close all files
pdfOutputFile.close()
fileObj1.close()
fileObj2.close()

#outFile = open('merged-files.pdf','rb')
#outPDF = PyPDF2.PdfFileReader(outFile)   # ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Goodnight.

#print("Scanning merged file...")
# Extract current page department number (i.e. section number) from header: MOVE TO LOOPS ABOVE
#for page in range(outPDF.numPages):
#    pageText = outPDF.extractText()
#    pageDept = pageText.splitlines()[-4:]
#    print("(Page " + str(page) + " of " + str(page) + "):" + str(pageDept))

print("Print complete. Check the folder!")

# Close program
print("Closing program...\n-----------------------------------------------------")

# IMPORTANT!!! Close all files
#outFile.close()

# Goodbye
print("Goodbye @ " + str(datetime.datetime.now()) + "\n\n\n")

# TODO: Print all "print()" statements to a log file, namedby datetime


# Define 'About' menu option
#def about():
#    messagebox.showinfo(app.name,"Hello World!")

## Setup menu bar
#menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
# File Menu
#file = Menu(menubar, tearoff=0, foreground='black')  
#file.add_command(label="New")
#file.add_command(label="Open Files", command=open())
#file.add_command(label="Parse", command=parse())
#file.add_command(label="Save")
#file.add_command(label="Save as")
#file.add_separator()
#file.add_command(label="Exit", command=ws.quit)
#menubar.add_cascade(label="File", menu=file)
# Edit Menu
#edit = Menu(menubar, tearoff=0)
#edit.add_command(label="Undo")
#edit.add_separator()
#edit.add_command(label="Cut")
#edit.add_command(label="Copy")
#edit.add_command(label="Paste")
#menubar.add_cascade(label="Edit", menu=edit)
# Help Menu
#help = Menu(menubar, tearoff=0)
#help.add_command(label="About", command=about)
#menubar.add_cascade(label="Help", menu=help)
# End menu setup
#ws.config(menu=menubar)

# End UI Setup
ws.mainloop()