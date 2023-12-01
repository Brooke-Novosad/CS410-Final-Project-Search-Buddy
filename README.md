# CS 410 Search Buddy

![](https://github.com/https://github.com/drshika/CS410-Final-Project/demo.gif)

**Team Members:** Joanna Huang (joannah2), Drshika Asher (drshika2), Brooke Novosad (novosad3), Rainy Yan (yuzheng9)   
**Team Captain:** Brooke Novosad (novosad3)   
**Team Name:** Autumn Lovers   

**Project Description:** Our application allows you to enter any CS410 related search query to find the 10 most relevant course materials (CS410 Lecture Transcripts and Slides) to match your query. 

## Installation
0. Have python3 and pip installed: [install python](https://packaging.python.org/en/latest/tutorials/installing-packages/)

1. Clone Repository Locally

HTTPS
```
$ git clone https://github.com/drshika/CS410-Final-Project.git
```
SSH
```
$ git clone git@github.com:drshika/CS410-Final-Project.git
```

2. Install requirements with pip:

```
$ pip install -r requirements.txt
```

3. Run the app on localhost:
```
$ python app.py
```
or 
```
$ flask run
```
4. Open in browser

```CS410-Final-Project git:(main) ✗ python3 app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
Paste `http://127.0.0.1:5000` (or whatever port address it assigns) into your browser to view the webpage. 

## Libraries Used

- [**Rank_bm25:**](https://github.com/dorianbrown/rank_bm25) this library has the Okapi BM25 ranking function to get the 10 most relevant document names.
- [**Flask:**](https://flask.palletsprojects.com/en/3.0.x/) this is a framework used to make GET and POST requests for the user query and the search results from our backend.
- [**Numpy:**](https://pypi.org/project/numpy/) this library was used to sort the outputted list from most to least relevant.
- [**BeautifulSoup:**](https://pypi.org/project/beautifulsoup4/) this library was used to parse the HTML web pages from the CS410 course website to get the documents that users can search for. 
- [**PyPDF2:**](https://pypi.org/project/PyPDF2/) This library was used to scrape PDFs into text.


## Application Structure 

```.
├────── extraction_scripts/             # Scripts used to process raw HTML lecture transcripts and slides
│      ├── get_pdf.py                   # Scrapes lecture slide PDFs
│      └── get_transcripts.py           # Scrapes lecture Transcripts
├───── html_files/                      # Raw HTML files from CS410 Coursera Website
├───── lecture_slides/                  # CS410 PDF lecture slides
├───── lecture_slides_extractions/      # Text from CS410 lecture slides
├───── lecture_transcripts/             # Transcripts from CS410 lecture videos
├───── static/images                    # Images used in this repository
├───── project_docs/                    # Misc Project Docs
│     ├── Project Progress Report.md
│     ├── Project Proposal.md
│     └── sources.txt                   # Reference Code Documentation
├───── templates/                       # HTML template pages       
│     ├── answer.html                   # Query response page
│     └── home.html                     # Home page
├───── .gitignore
├───── app.py                           # Main Flask driver code
├───── ranking_function.py              # Utility function to return ranked documents
├───── README.md
└───── requirements.txt                 # Used to install required python libraries
```

## Team Contributions

1. Proposal preparation and revision (5hrs) - all
2. Project scoping and approach analysis (5hrs) -all
3. Collect all documents in CS 410 Coursera (5 hrs) - Brooke, Drshika, Joanna
4. Data clean up (tokenization, remove stop words, etc.) (20 hrs - verification by hand included) - Brooke, Rainy, Drshika, Joanna
5. Data processing, analysis, & storage (5 hrs) - Brooke, Rainy, Joanna
6. Website
7. Frontend (5hrs) - Drshika
8. Backend (5hrs) - Brooke, Rainy, Drshika, Joanna
9. Data routing (10hrs) - Brooke, Rainy, Drshika
10. Search algorithms (5hrs) - Brooke, Rainy, Joanna
11. Summarization blurb for each query (5 hrs) - Brooke, Joanna