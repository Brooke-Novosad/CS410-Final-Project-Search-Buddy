import os
from PyPDF2 import PdfReader
#Scrapes the lecture pdfs for valid text and puts in corresponding extracted document

slides_dir = "lecture_slides"
extr_dir = "lecture_slides_extractions"

for filename in os.listdir(slides_dir):
    in_f = os.path.join(slides_dir, filename)
    split = filename.split('.', 2)[:2]
    lesson_num = split[0] + '.' + split[1]
    print(lesson_num)
    out_f = os.path.join(extr_dir, lesson_num + '.txt')
    #UTF-16 for special characters in pdfs
    out_f = open(out_f, 'w', encoding='UTF-16')
    reader = PdfReader(in_f)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        for line in text.splitlines():
            out_f.write(line + '\n')
    