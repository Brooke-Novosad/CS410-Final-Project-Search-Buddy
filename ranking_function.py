import math
import sys
import time
import metapy
import pytoml
import os

def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate, 
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    return metapy.index.OkapiBM25(1.2, .75, 500.0)

def search(top_k):
    
    slides = "lecture_slides_extractions"
    transcripts = "lecture_transcripts"

    documents = []
    # for filename in os.listdir(transcripts):
    #     in_f = os.path.join(transcripts, filename)
    #     doc = ""
    #     for num, line in enumerate(in_f):
    #         doc = doc + line
    #     documents.append(doc)
        
    for filename in os.listdir(slides):
        in_f = os.path.join(slides, filename)
        doc = ""
        for num, line in enumerate(in_f):
            doc = doc + line
        documents.append(doc)

    return documents

docs = search(10)
print(docs)

    










    # cfg = "config.toml"
    # idx = metapy.index.make_inverted_index(cfg)
    # ranker = load_ranker(cfg)

    # with open(cfg, 'r') as fin:
    #     cfg_d = pytoml.load(fin)

    # query_cfg = cfg_d['query-runner']
    # if query_cfg is None:
    #     print("query-runner table needed in {}".format(cfg))
    #     sys.exit(1)

    # query_path = query_cfg.get('query-path', 'queries.txt')

    # query = metapy.index.Document()

    # with open(query_path) as query_file:
    #     line = query_path.readline()
    #     query.content(line.strip())
    #     results = ranker.score(idx, query, top_k)
    
    