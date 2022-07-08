import pdfkit

pdf_options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-bottom': '0in',
    'margin-right': '0in',
    'margin-left': '0in',
    'encoding': "UTF-8",
    'footer-center': '[page]',
    "quiet": "",
    'no-outline': None,
}

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_url('http://127.0.0.1:8000/', 'out.pdf', configuration=config, options=pdf_options)
