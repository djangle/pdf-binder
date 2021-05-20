# Import libraries
import os
import datetime
import tkinter as tk
from tkinter import filedialog as fd, messagebox, Menu
import PyPDF2

class app():
    name = "Curry"

# Start program
startTime = str(datetime.datetime.now())
app = app()
print("\n####################################################\nHello @ " + startTime)

# Make a UI
ws = tk.Tk()
ws.title(app.name)
ws.configure()

# Prepare text for window
logText = "Making the curry...\n"
log = tk.Label(text = logText)
#log.grid(column=0,row=0)
log.pack()

# Ask for input files
#files = fd.askopenfilenames()  # Use to select multiple files at one time
summaryFile = fd.askopenfilename(title="Open the SOA file")
print("Summary file opened.")

detailFile = fd.askopenfilename(title="Open the detail file")
print("Detail file opened.")
logText = "Files opened...\n"

# Convert file* to *file because it's not important right now.
file1 = summaryFile
file2 = detailFile

# Display opened filenames
logText += "Summary of Activities: " + file1 + "\n"
logText += "Statement Details: " + file2 + "\n"

# Open each file
fileObj1 = open(file1,'rb')
fileObj2 = open(file2, 'rb')
print("Files opened as objects.")

# PyPDF2 "read" each file
pdf1 = PyPDF2.PdfFileReader(fileObj1)
pdf2 = PyPDF2.PdfFileReader(fileObj2)
print("Files read as PDF's.")

logText="Make it work"
# TODO: Make it work
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extract section numbers and section names from PDF headers
pageTags = []

for page in range(pdf1.numPages):
    pdfPage = pdf1.getPage(page)
    pageText = pdfPage.extractText()
    pageTag = pageText.splitlines()[-4:-3]  # Read section number and name from page footer
    pageTags += pageTag
    #print("(Page " + str(page) + " of " + str(page) + "):" + str(pageTag))

print("Section numbers and names extracted.")
print(pageTags)

# Order the pages
order = [39,33,1,30,2,3,5,6,43,7,36,9,34,32,10,11,24,40,37,22,12,13,14,15,16,29,21,17,38,18,20,42,41,27,23,25,35,31,26,8,28]
print("Output order set.")

# Prepare to write output file
pdfWriter = PyPDF2.PdfFileWriter()

# Combine the PDF's
for ord in order:
    pageObj1 = pdf1.getPage(ord)
    pdfWriter.addPage(pageObj1)
    pageObj2 = pdf2.getPage(ord)
    pdfWriter.addPage(pageObj2)

# TODO: Add bookmarks
bookmarks = ['Administrative Law','Agricultural Law','Alternative Dispute Resolution','Animal Law','Antitrust, Trade Regulation','Appellate Practice','Business Law','Business Litigation','Cannabis and Psychedelics Law','Civil Rights','Constitutional Law','Construction Law','Consumer Law','Corporate Counsel','Criminal Law','Debtor-Creditor','Disability Law','Diversity','Elder Law','Energy, Telecom & Utility Law','Environmental & Natural Resources','Estate Planning & Administration','Family Law','Government Law','Health Law','Indian Law','Intellectual Property','International Law','Juvenile Law','Labor & Employment','Litigation','Military and Veterans Law','Nonprofit Organizations Law','Products Liability','Real Estate & Land Use','Securities Regulation','Solo and Small Firm','Sustainable Future','Taxation','Technology Law','Workers Compensation']
int = 0
for mark in range(0,82,2):
    pdfWriter.addBookmark(bookmarks[int],mark)
    int += 1

# Write the output file
logText += "Printing 'merged-files.pdf'...\n"
pdfOutputFile = open('merged-files.pdf','wb')
pdfWriter.write(pdfOutputFile)
logText += "Print complete!\n"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Close all files
pdfOutputFile.close()
fileObj1.close()
fileObj2.close()
logText += "Files closed.\n"
print("Files closed.")

# Goodbye
print("\n\nClosing program...")
# TODO: Save all "print()" statements to a log file
logText += "Curry Done! Check your folder. Close me.\n\nGoodbye.\n" + str(datetime.datetime.now())
print("Goodbye @ " + str(datetime.datetime.now()))
print("-----------------------------------------------------\n")
log = tk.Label(text = logText)
log.pack()

ws.mainloop()