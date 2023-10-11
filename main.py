# WORKING

import os
import sys
import subprocess
# from config import config

if __name__ == '__main__':
    arg: str = sys.argv[1]

    # os.system("deactivate")
    # os.system("cd libraries/pdfkit")
    # os.system("source .venv/bin/activate")

    from libraries.pdfkit.basic.generate_pdf import generate_pdf
    generate_pdf(arg)
