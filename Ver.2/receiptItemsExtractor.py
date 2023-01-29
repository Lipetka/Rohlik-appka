"""

This file containts code to extract items from receipt
and save contents in dictionary

"""

# imports

import readPDFContents  # file that contains function to extract PDF text

receipt_text    = readPDFContents.getContents()   # enter filename or leave empty for default test file
bough_items_dictionary = receipt_items   = readPDFContents.extractOrderedItems(receipt_text) # enter receipt text and save output as dictionary

# check total sum to verify skript
total_sum = round(sum(bough_items_dictionary.values()),2)
print(total_sum)

