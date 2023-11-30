import math
import sys
import time
import os
import io
import numpy as np
from rank_bm25 import BM25Okapi

#Run once on start of website
#Takes the extracted text from the lecture slides and transcripts and puts them in a map
def startup():

    file_name_map = {}
    documents = [] 

    file_idx = 0

    slides = "lecture_slides_extractions"
    transcripts = "lecture_transcripts"

    for filename in os.listdir(transcripts):
        fp = os.path.join(transcripts, filename)
        in_f = open(fp)
        file_name_map[file_idx] = filename
        doc = ""
        for num, line in enumerate(in_f):
            doc = doc + line.lower().strip() + " "
        documents.append(doc)
        file_idx += 1

    for filename in os.listdir(slides):
            fp = os.path.join(slides, filename)
            in_f = io.open(fp, encoding='UTF-16')
            file_name_map[file_idx] = filename
            doc = ""
            for num, line in enumerate(in_f):
                doc = doc + line.lower().strip() + " "
            documents.append(doc)
            file_idx += 1    

    tokenized_corpus = [doc.split(" ") for doc in documents]

    bm25 = BM25Okapi(tokenized_corpus)

    return file_name_map, documents, bm25

#Using the BM25Okapi on the documents with the user inputted query
#We return the top 10 documents that match the query
def search(query,file_name_map, bm25):
    top_k = 10

    tokenized_query = query.split(" ")

    doc_scores = bm25.get_scores(tokenized_query)

    results = np.argsort(doc_scores)[::-1][:top_k]

    return [file_name_map[i] for i in results]