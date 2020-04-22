# -----------------------------------------------------------
#  pdf2image library in Python 3 is used for converting PDF
#  to image. This library wraps pdftoppm and pdftocairo to
#  convert PDF to an image object.
#
# (C) 2020, Himanshu Shukla
# email acmehimanshu@gmail.com
# -----------------------------------------------------------
import os
import tempfile
from pdf2image import convert_from_path
from PyPDF3 import PdfFileWriter, PdfFileReader

path="D:/N18PersonalWorkspace/pythondemo/pdftoimg/"
output_folder_path="D:/N18PersonalWorkspace/pythondemo/pdftoimg/output/"
pdfname=path+"javacollections.pdf"

images = convert_from_path(pdfname)
i = 1
len=len(images)
print("Number of pages in PDF="+str(len))
for image in images:
	image.save(output_folder_path + str(i) + '.jpg', 'JPEG')
	i = i + 1