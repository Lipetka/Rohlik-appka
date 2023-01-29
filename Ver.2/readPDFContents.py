"""
File that returns content of PDF file (can be used for any PDF i guess)

"""

# imports

import PyPDF2

def getContents(fileName = "Ver.2\pdfFileName"):

    # importing PDF file

    pdf_file_object   = open( fileName + ".pdf",'rb')    # open file name from GUI (dropdown or drag n drop)
    pdf_read          = PyPDF2.PdfFileReader(pdf_file_object)   # extract PDF contents

    page_count       = pdf_read.numPages  # count pages to loop through them

    output_text     = "" # placeholder for text output        

    for i in range(page_count):
        # loop through all pages and save the output to output_text variable

        page = pdf_read.getPage(i) # get nth page
        output_text = output_text + page.extractText() # read text and append it

    return output_text  # return output text


def extractOrderedItems(receipt_text):
    # this function extracts only bought items and saves them in dictionary
    # this functon is coded separately.

    removed_header = receipt_text.split("Doručené položky")[1]  # extract top
    removed_footer = removed_header.split("Způsob úhrady")[0]   # extract bottom

    items = removed_footer.split("\n")  # saved sperately for code clarity

    length_of_list      = len(items)    # get length of list of ordered items
    items_dictionary    = {}            # final dictionary placeholder

    for i in range(length_of_list):
        # loop throught all items 

        # protection against empty lines and file end
        if items[i] == '':
            continue
        elif items[i] == 'Sleva v kreditech':
            break

        # check if the first letter is digit
        if items[i][0].isdigit() == False:

            # if first letter isnt digit, check if the second line starts with digit
            # to catch multiline names

            if items[i+1][0].isdigit() == False:
                name = items[i] + items[i+1]    # if the w line is also letter, save both lines as a name
            else:
                name = items[i] # if following line is number, save only the first line as name


        # solving for number
        if items[i][0].isdigit() == True:
            # if the next line starts with letter save the price
            if items[i+1][0].isdigit() == False:
                price = float(items[i].replace(',','.').split()[0]) # save the number
                items_dictionary.update({name:price})   # add new item to dictionary when price is found
            else:
                # if the next line starts with number continue loop
                continue


    return items_dictionary
