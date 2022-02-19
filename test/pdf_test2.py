import pdfplumber

def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            print(page.layout)
            # print(page.extract_text())
            print("########" * 10)


plum_daldal('test_pdf.pdf')
#plum_daldal('test_pdf2.pdf')



