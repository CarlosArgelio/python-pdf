import sys
import pdfkit

def generate_pdf(_from: str):

    if _from == 'string':
        pdfkit.from_string('MicroPyramid', 'micro.pdf')
    elif _from == 'url':
        pdfkit.from_url('http://micropyramid.com', 'micro.pdf')
    elif _from == 'file':
        pdfkit.from_file('micropyramid.html', 'micro.pdf')
