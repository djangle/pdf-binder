#%%
# Set app info (do I need a class for this?)
class app():
    name = "sh-tk"
    version = "0.1"
    author = "Adam Amodio"

app = app()

# Import libraries
import datetime
import PyPDF2
import tkinter as tk
from tkinter import Label, Menu
from tkinter import filedialog as fd
from tkinter import messagebox
from smtplib import SMTP
# TODO: Setup email service?
#with SMTP("localhost") as smtp:
#    smtp.noop()


# Start program
# TODO: Print log to a widget in tk (scrollingText?)
# Set program start time
programStartTime = datetime.datetime.now()
print("\n#####################################################\nStarting program... \n" + str(programStartTime))

# Configure the UI
ws = tk.Tk()
ws.title(app.name)
# TODO: Rewrite the following with Canvas.Tk()
width = 500
height = 400
x_pos = 300
y_pos = 100
geometry_string = "{}x{}+{}+{}".format(width, height, x_pos, y_pos)
ws.geometry(geometry_string)

# TODO: Create live output widget
logText = str(programStartTime)
log = tk.Label(text = logText)
log.grid(column=0,row=0)

# TODO: Create function to parse files
def parseFiles():
    # TODO: Load multiple files (fd.askopenfilename() for one file, fd.askopenfilenames() for multiple files)
    # Count files
    fileCount = 0
    print('Loading files...')
    filenames = fd.askopenfilenames()
    #pdfFileObj = open(filenames,'rb')
    #pdf = PyPDF2.PDFFileReader(pdfFileObj)

    #for each file in filenames():
        # Count files
        #fileCount += fileCount
        # TODO: Assign variables to each file
        #file1 = filenames[0]
        #file2 = filenames[1]
        # TODO: Display file info (filenames, # of files, # of pages per file)
        #print("Files Opened: ")
        #print(filenames)
        # Extract number of pages
        #print("\nCounting Pages...")
        #pageCount = pdf.numPages
        #print("Page Count: " + str(pageCount))

        # TODO: Scan files being parsed for actual page order
        # Analyze current page order
        #print("\nAnalyzing current page order...")

    # TODO: Merge files
    
    # TODO: Reorder pages
    #print("\nSetting desired page order...")
    # This page order is from the PDF: smallest to largest section code
    #currentPageOrder = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848]
    #print(currentPageOrder)
    # This page order is from Aptify: alphabetically by committee name
    desiredPageOrder = [844,801,837,802,834,803,804,805,806,807,848,808,841,810,838,836,811,812,826,845,842,824,813,814,815,816,817,833,823,818,843,819,820,821,822,847,832,846,839,829,825,827,840,835,828,809,830]

    # TODO: Iterate through the document page by page
    # Read page header for department number (and page number?)
    #print("\nReading all pages...")
    #i = 0
    #for i in range(pageCount):
    #    currentPage = pdf.getPage(pageCount - (pageCount - i))

        # Extract current page department number (i.e. section number)
    #    currentPageText = currentPage.extractText()
    #    currentPageDept = currentPageText.splitlines()[-4:]
    #    print("(Page " + str(i) + " of " + str(pageCount) + "):" + str(currentPageDept))

    # Set array of current page numbers with section department codes (ex. "802","etc")

    # TODO: Create bookmarks

    # TODO: Output (local, email?)
    print("Output files...")
    #print("\nCreating file...")
    #PyPDF2.PdfFileWriter.addPage()
    #print to file
    #outputFilename = "click to open pdf"
    #print("Output filename: " + outputFilename)

# Display info via the 'About' menu option
def about():
    messagebox.showinfo(app.name,"Hello World!\n\n" + "\nVersion: " + app.version + "\nAuthor: " + app.author)



## Setup menu bar
menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
# File Menu
file = Menu(menubar, tearoff=0, foreground='black')  
#file.add_command(label="New")
file.add_command(label="Parse Files", command=parseFiles)
#file.add_command(label="Prepare", command=prepareOutput)
#file.add_command(label="Save")
#file.add_command(label="Save as")
file.add_separator()
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

# Close all files
#for(file) in range(len(filenames)):
#    file.close()

# Goodbye
print("Goodbye")