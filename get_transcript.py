import os
from bs4 import BeautifulSoup

html_dir = "html_files"
trans_dir = "lecture_transcripts"

for filename in os.listdir(html_dir):
    in_f = os.path.join(html_dir, filename)
    lesson_num = filename.split('_')[0]
    out_f = os.path.join(trans_dir, lesson_num + '.txt')

    html = open(in_f)

    soup = BeautifulSoup(html, "html.parser")

    out_f = open(out_f, 'w')
    for i in soup.find_all('div', {'class': 'css-1shylkf'}):
        for p in i.find('div', {'class': 'phrases'}):
            out_f.write(p.text)

