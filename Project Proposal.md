# Project Proposal

### Team
Team Members: Joanna Huang (joannah2), Drshika Asher (drshika2), Brooke Novosad (novosad3), Rainy Yan (yuzheng9)

Team Captain: Brooke Novosad (novosad3)

Team Name: Autumn Lovers

### Topic
Chrome extension to scrape Coursera content (lecture transcript, slides) for CS 410 and provide the top k documents relating to the query as well as the specific relevant sections in the documents.

EDIT 11/30/23: We decided to switch routes and do a Website over a Chrome Extension due to the issues with running python in a HTML/JS environment. This does not affect the key functionality of the app: searching for CS410 study materials. We also changed our blurbs for each document to be general blurbs of the first 150 characters starting in the middle of the document. This functionality is not possible with BM25 and would require another library that could be expanded with more time.



1. Briefly describe any datasets, algorithms or techniques you plan to use
	Dataset: Scraping CS410 Lecture Transcripts and slides for the corpus using BeautifulSoup.
	Algorithms: We will use BM25 for the search algorithm.
	Techniques: Tokenization, Removing Special Characters, Removing Stopwords, Normalization and Stemming to prepare the data for the search engine.

2. How will you demonstrate that your approach will work as expected? 
	We will generate a set of example queries and a set of documents that we deem to be the k best results for each query. Then we will run each query on our system and find the MAP for the results that are given by the system vs the results that we came up with. 

3. Which programming language do you plan to use?
	Python, React

4. Please justify that the workload of your topic is at least 20*N hours, N being the total number of students in your team. You may list the main tasks to be completed, and the estimated time cost for each task.
	a. Proposal preparation and revision (5hrs)
	b. Project scoping and approach analysis (5hrs)
	c. Collect all documents in CS 410 Coursera (5 hrs) 
	d. Data clean up (tokenization, remove stop words, etc.) (20 hrs - verification by hand included)
	e. Data processing, analysis, & storage (5 hrs)
	f. Chrome extension
		i. Frontend (5hrs)
		ii. Backend (5hrs)
		iii. Data routing (10hrs) 
		iv. Search algorithms (5hrs)
	g. Summarization blurb for each query (5 hrs)
	h. Verification (5 hrs)
	i. Group Meetings / Project Synchronization (3 hrs)
	j. Presentation (2hrs)
