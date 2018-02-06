#!/usr/bin/env python
# pip install pypdf2
# To use simply do python split.py pdf_to_split.pdf

import os
import re
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


def split(file_):
    input1 = PdfFileReader(open(file_, "rb"))
    pages = input1.getNumPages()
    new_file_prefix = os.path.splitext(file_)[0]
    for i in range(pages):
        current_page = input1.getPage(i)
        page_text = current_page.extractText()
        match_object = re.match(r"^\s*\w+ \d+, \d\d\d\d\s*([^\:]+)", page_text)
        if match_object:
            report_name = match_object.group(1).lower().replace(' ', '_')
            output = PdfFileWriter()
            outputStream = file("%s_%s.pdf" % (new_file_prefix, report_name), "wb")
            output.addPage(current_page)
            output.write(outputStream)
        else:
            print "Unable to parse report name for page %d!" % i


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Please pass in the name of the pdf to split")

    split(sys.argv[1])
