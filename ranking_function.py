import math
import sys
import time
# import metapy
# import pytoml
import os
import io
import numpy as np
from rank_bm25 import BM25Okapi

file_idx = 0
file_name_map = {}

slides = "lecture_slides_extractions"
transcripts = "lecture_transcripts"

documents = []

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

def search(query, top_k):

    tokenized_query = query.split(" ")

    doc_scores = bm25.get_scores(tokenized_query)

    return np.argsort(doc_scores)[::-1][:top_k]

idx = search("inverse document frequency", 10)

for i in idx:
    print(file_name_map[i])
