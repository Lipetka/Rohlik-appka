"""
File that returns content of PDF file (can be used for any PDF i guess)

"""

# imports

import PyPDF2

def getContents(fileName = "Ver.2\pdfFileName"):

    # importing PDF file

    pdf_file_object   = open( fileName + ".pdf",'rb')    # open file name from GUI (dropdown or drag n drop)
    pdf_read         = PyPDF2.PdfFileReader(pdf_file_object)   # extract PDF contents

    page_count       = pdf_read.numPages  # count pages to loop through them

    output_text     = "" # placeholder for text output        

    for i in range(page_count):
        # loop through all pages and save the output to output_text variable

        page = pdf_read.getPage(i) # get nth page
        output_text = output_text + page.extractText() # read text and append it

    return output_text  # return output text