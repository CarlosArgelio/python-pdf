import sys
import pdfkit

def generate_pdf(_from: str):

    if _from == 'string':
        pdfkit.from_string('MicroPyramid', 'micro.pdf')
    elif _from == 'url':
        pdfkit.from_url('http://micropyramid.com', 'micro.pdf')
    elif _from == 'file':
        pdfkit.from_file('templates/dinamics/basic.html', 'micro.pdf')

if __name__ == '__main__':
    arg: str = sys.argv[1]
    generate_pdf(arg)