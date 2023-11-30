# CS 410 Search Buddy

**Team Members:** Joanna Huang (joannah2), Drshika Asher (drshika2), Brooke Novosad (novosad3), Rainy Yan (yuzheng9)
**Team Captain:** Brooke Novosad (novosad3)
**Team Name:** Autumn Lovers

**Project Description:** Our application allows you to enter any CS410 related search query to find the 10 most relevant course materials (CS410 Lecture Transcripts and Slides) to match your query. 

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

Run the app on localhost:
```
$ python app.py
```

## Libraries Used

- [**Rank_bm25:**](https://github.com/dorianbrown/rank_bm25) this library has the Okapi BM25 ranking function to get the 10 most relevant document names.
- [**Flask:**](https://flask.palletsprojects.com/en/3.0.x/) this is a framework used to make GET and POST requests for the user query and the search results from our backend.
- [**Numpy:**](https://pypi.org/project/numpy/) this library was used to sort the outputted list from most to least relevant.
- [**BeautifulSoup:**](https://pypi.org/project/beautifulsoup4/) this library was used to parse the HTML web pages from the CS410 course website to get the documents that users can search for. 
- [**PyPDF2:**](https://pypi.org/project/PyPDF2/) This library was used to scrape PDFs into text.


## Application Structure 

```.
|──────extraction_scripts/
| |──────get_pdf.py
| |──────get_transcripts.py
|──────html_files/
|──────lecture_slides/
|──────lecture_slides_extractions/
|──────lecture_transcripts/
|──────templates/
| |────answer.html
| |────home.html
|──────app.py
```
