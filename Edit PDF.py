from PyPDF2 import PdfWriter, PdfReader
from io import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PyPDF4 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

os.chdir(r'C:/Temp')

def rotate():
    # Open the PDF file
    reader = PdfReader("TEST.pdf")
    writer = PdfWriter()
    
    # Modify the first page
    page = reader.pages[0]
    page.rotate(90)
    
    # Add the modified page to the writer
    writer.add_page(page)
    
    # Save the modified PDF
    with open("output.pdf", "wb") as output_file:
        writer.write(output_file)

def create_watermark(watermark_text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 40)
    can.setFillColorRGB(1, 0, 0)
    can.saveState()
    can.translate(300, 400)
    can.rotate(45)
    can.drawCentredString(0, 0, watermark_text)
    can.restoreState()
    can.save()
    packet.seek(0)
    return PdfFileReader(packet)

def add_watermark(input_pdf, output_pdf, watermark_text):
    watermark = create_watermark(watermark_text)
    pdf_reader = PdfFileReader(open(input_pdf, "rb"))
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page)
        page_obj.mergePage(watermark.getPage(0))
        pdf_writer.addPage(page_obj)

    with open(output_pdf, "wb") as out_file:
        pdf_writer.write(out_file)
    
def main():
    add_watermark("input.pdf", "output.pdf", "CONFIDENTIAL")
    
if __name__ == '__main__':
    main()    