import pdfplumber
import tabula
import camelot
import ctypes
from ctypes.util import find_library
find_library("".join(("gsdll", str(ctypes.sizeof(ctypes.c_voidp) * 8), ".dll")))


def t(path):
    df = tabula.read_pdf(path, pages='1', multiple_tables=True)
    print(df)


def c(path):
    df = camelot.read_pdf(path)
    print(df)


def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        pages = []
        for i in range(len(pdf.pages)):
            pages.append(pdf.pages[i].extract_text().split('\n'))
    return pages


def extract_register(pages):
    b_type = pages[0][1].split('- ')[1].split(' -')[0]
    address = pages[0][3].split('] ')[1]
    owners = pages[0][17].split('소유자  ')[1].split('-')[0].split('  ')
    print(b_type)
    print(address)
    print(owners)
    # for page in pages:


file_name = 'test_pdf2.pdf'


# for i, n in enumerate(plum_daldal(file_name)[0]):
#     print(i, n)
# print("#" * 100)
# extract_register(plum_daldal(file_name))
# t(file_name)
c(file_name)

