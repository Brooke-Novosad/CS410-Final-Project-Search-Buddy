import math
import sys
import time
# import metapy
# import pytoml
import os
import io
import numpy as np
from rank_bm25 import BM25Okapi

if __name__ == "__main__":

    file_name_map = {}
    documents = [] 

    def startup():
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

    def searchFun():
        tokenized_corpus = [doc.split(" ") for doc in documents]

        bm25 = BM25Okapi(tokenized_corpus)

        def search(query, top_k):

            tokenized_query = query.split(" ")

            doc_scores = bm25.get_scores(tokenized_query)

            return np.argsort(doc_scores)[::-1][:top_k]

        idx = search("inverse document frequency", 10)

        out_f = open("results.txt", 'w')
        for i in idx:
            out_f.write(file_name_map[i] + '\n')

    args = sys.argv[1:]
    if args[0] == "start":
        startup()
    else: 
        searchFun()