from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.units import inch
import os
from PyPDF2 import PdfMerger


directory = r'C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\projects\random_python_projects\trial_folder'

#total_files = (len([filename for filename in os.scandir(directory) if filename.is_file() and "destination" not in filename.path]))
all_paths = [filename.path for filename in os.scandir(directory) if filename.is_file() and "destination" not in filename.path]
print(all_paths)



def modify_pdf(filepath):
    index = all_paths.index(filepath)
    packet = io.BytesIO()
    lab = Label()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillColorRGB(1,1,1) #choose fill colour
    can.rect(212, 775, 40, 13, fill=1, stroke=0)
    can.setFillColorRGB(0,0,0) #choose your font colour
    can.setFont("Helvetica-Bold", 10) #choose your font type and font size
    can.drawString(212, 780, str(index+1) + " OF " + str(len(all_paths))) # write your text
    can.save()
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(filepath, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(filepath + "destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

def merging(filtering_new_files):
    merger = PdfMerger()
    [merger.append(pdf) for pdf in filtering_new_files]
    merger.write(directory + r"\result.pdf")
    merger.close()


for i in all_paths:
    modify_pdf(i)

filtering_new_files = [filename.path for filename in os.scandir(directory) if "destination" in filename.path]

#merging the files 
merging(filtering_new_files)
#removing files in the directory
[os.remove(i) for i in filtering_new_files]
