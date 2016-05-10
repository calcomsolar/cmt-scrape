# CCS Scrape PG&E CMT
# version 0.1
# BT


import os
import PyPDF2 as pdf
import tkinter as tk
from tkinter import filedialog
from tkinter import *


# prompt user for file to input
# filepath = tk.filedialog.askopenfilename(filetypes = [("PDF files", "*.pdf")])
# print(filepath)


pdfCMT = open('test-inputs/PGE-CMT.pdf', 'rb')
pdfReader = pdf.PdfFileReader(pdfCMT)
numPgs = pdfReader.numPages
print(numPgs,"pages found")

pageObj = pdfReader.getPage(0)
pageObj.extractText()
