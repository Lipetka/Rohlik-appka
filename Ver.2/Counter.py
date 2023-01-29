import PyPDF2
import sys, os

kika_suma = 0
samko_suma = 0
bytik_suma = 0
cela_suma = 0

datum = input('Dátum [mesiac-den]: ')

def main():

    global samko_suma
    global kika_suma
    global bytik_suma
    global cela_suma

    pdfFileObj = open(datum+'.pdf','rb') # open pdf

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # load pdf object

    num_of_pages = pdfReader.numPages # get number of pages
    print('Number of pages: ' + str(num_of_pages)) # print number of pages to check if data are legit

    for i in range(num_of_pages):

        page = pdfReader.getPage(i) # get nth page
        output = page.extractText() # read text
        lines = output.splitlines() # extract lines

        getBoughtItems(lines) # promts user to describe item manually


    savePriceToDatabase()

def getBoughtItems(lines):

    global samko_suma
    global kika_suma
    global bytik_suma
    global cela_suma

    for j in range(len(lines)):

        while(1):
            group = input(lines[j])
            if group == 's':
                try:
                    samko_suma = samko_suma + float(lines[j].replace(',','.').split()[0])
                    cela_suma = cela_suma + float(lines[j].replace(',','.').split()[0])
                except:
                    print("Incorrect input")
                    continue
                os.system('cls')
                print("Dokopy: " + str(cela_suma))
                print("Kika suma: " + str(kika_suma))
                print("Samko suma: " + str(samko_suma))
                print("Bytik suma: " + str(bytik_suma))
                print("-------------------")

                break
            if group == 'k':
                try:
                    kika_suma = kika_suma + float(lines[j].replace(',','.').split()[0])
                    cela_suma = cela_suma + float(lines[j].replace(',','.').split()[0])
                except:
                    print("Incorrect input")
                    continue
                os.system('cls')
                print("Dokopy: " + str(cela_suma))
                print("Kika suma: " + str(kika_suma))
                print("Samko suma: " + str(samko_suma))
                print("Bytik suma: " + str(bytik_suma))
                print("-------------------")
                break
            if group == 'd':
                try:
                    suma = float(lines[j].replace(',','.').split()[0])
                except:
                    print("Incorrect input")
                    continue
                os.system('cls')
                kika_suma = kika_suma + suma/2
                samko_suma = samko_suma + suma/2
                cela_suma = cela_suma + suma
                print("Dokopy: " + str(cela_suma))
                print("Kika suma: " + str(kika_suma))
                print("Samko suma: " + str(samko_suma))
                print("Bytik suma: " + str(bytik_suma))
                print("-------------------")
                break
            if group == 'b':

                try:
                    suma = float(lines[j].replace(',','.').split()[0])
                except:
                    print("Incorrect input")
                    continue
                os.system('cls')
                kika_suma = kika_suma + suma/4
                samko_suma = samko_suma + suma/4
                bytik_suma = bytik_suma + suma/2
                cela_suma = cela_suma + suma
                print("Dokopy: " + str(cela_suma))
                print("Kika suma: " + str(kika_suma))
                print("Samko suma: " + str(samko_suma))
                print("Bytik suma: " + str(bytik_suma))
                print("-------------------")
                break
            if group == '':
                print("\n")
                break

def savePriceToDatabase():

    global samko_suma
    global kika_suma

    os.system('cls')
    print("Uložené do databázy")
    print("Kika suma: " + str(round(kika_suma,2)))
    print("Samko suma: " + str(round(samko_suma,2)))
    print("Bytik suma: " + str(round(bytik_suma,2)))
    print("Dokopy suma: " + str(round(cela_suma,2)))
    print(str(datum)+ " " + str(round(samko_suma,2)) + " " + str(round(kika_suma,2)) + " " + str(round(cela_suma,2)))

    with open('database.txt','a+') as f:
        f.write("\n" + str(datum)+ " " + str(round(samko_suma,2)) + " " + str(round(kika_suma,2)) + " " + str(round(cela_suma,2)))
        f.close()
    while(1):
        continue
main()
