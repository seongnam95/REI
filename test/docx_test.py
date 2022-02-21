from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

document = Document('test_pdf2.docx')
print(document)
tables = document.tables[3]

for row in tables.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            print(para.text)