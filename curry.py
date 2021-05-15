# Import libraries
import os
import datetime
from PyPDF2 import PdfFileMerger, PdfFileReader
import tkinter as tk
from tkinter import *
from tkinter import Label, Menu, PhotoImage, messagebox, filedialog as fd
import PyPDF2
from playsound import playsound

class app():
    name = "Curry"
    version = "0.1 'Ochre'"

app = app()

# Start program
startTime = str(datetime.datetime.now())
print("\n#####################################################\nHello @ " + startTime)
playsound('audio/wookie.wav')

# TODO: Make a UI
ws = tk.Tk()
ws.title(app.name)
canvas = Canvas(ws, bg="blue", width=1200, height=500)
filename = PhotoImage(file = "images/delft.png")
background_label = Label(ws, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()
ws.configure()

# Prepare to output a log file
logText = "Making the curry..."
log = tk.Label(text = logText)
#log.grid(column=0,row=0)
log.pack()

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

print("Read files as PDF's...")
pdf1 = PyPDF2.PdfFileReader(fileObj1)
pdf2 = PyPDF2.PdfFileReader(fileObj2)
print("Files read as PDF's.")

print("Analyzing current page order...")
# Extract current page department number (i.e. section number) from header of file1
for page in range(pdf1.numPages):
    pdfPage = pdf1.getPage(page)
    pageText = pdfPage.extractText()
    pageDept = pageText.splitlines()[-4:]
    print("(Page " + str(page) + " of " + str(page) + "):" + str(pageDept))

# Prepare to write output file
pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Order the pages
playsound('audio/nananana.wav')
orderInput = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848]
orderByAlpha = [844,801,837,802,834,803,804,805,806,807,848,808,841,810,838,836,811,812,826,845,842,824,813,814,815,816,817,833,823,818,843,819,820,821,822,847,832,846,839,829,825,827,840,835,828,809,830]

# Set final output input page order by alpha output
order = set([39,0,33,36,1,30,2,3,4,5,6,43,36,9,37,35,10,11,26,34,41,23,12,13,14,15,17,32,22,17,42,18,19,20,21,42,31,41,38,28,24,26,39,34,37,8,29])

for ord in order:
    pageObj = pdf1.getPage(ord)
    pdfWriter.addPage(pageObj)

    pageObj = pdf2.getPage(ord)
    pdfWriter.addPage(pageObj)

# TODO: Create bookmarks
bookmarks = ["Admin Law","Badminton Law","Cat Law"]
for mark in bookmarks:
    pdfWriter.addBookmark(mark,1)

# Write the output file
print("Printing 'output/merged-files.pdf'...")
pdfOutputFile = open('output/merged-files.pdf','wb')
pdfWriter.write(pdfOutputFile)

# IMPORTANT!!! Close all files
pdfOutputFile.close()
fileObj1.close()
fileObj2.close()

print("Print complete. Check the folder!")
logText = "Curry Done!\n\nCheck your folder.\n\nClose me.\n\nGoodbye."
log = tk.Label(text = logText)
#log.grid(column=0,row=0)
log.pack()

playsound('audio/r2.wav')

# Goodbye
print("Closing program...\n-----------------------------------------------------")
print("Goodbye @ " + str(datetime.datetime.now()) + "\n\n\n")
# TODO: Save all "print()" statements to a log file


# Define 'About' menu option
def about():
    messagebox.showinfo(app.name,"Johannes Vermeer, painted ca. 1659–1661")

## Setup menu bar
menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
# File Menu
file = Menu(menubar, tearoff=0, foreground='black')  
#file.add_command(label="New")
#file.add_command(label="Open", command=open())
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

# End UI Setup
ws.mainloop()