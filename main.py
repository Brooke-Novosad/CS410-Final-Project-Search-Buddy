from bs4 import BeautifulSoup

a = open('html_files/lesson1.1.html')

soup = BeautifulSoup(a, "html.parser")

tfile = open('lecture_transcripts/1.1.txt', 'a+')

for i in soup.find_all('div', {'class': 'css-1shylkf'}):
  for p in i.find('div', {'class': 'phrases'}):
    # print(p.text)
    tfile.write(p.text)