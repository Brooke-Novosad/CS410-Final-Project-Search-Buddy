import ranking_function
import numpy as np
import pytest

file_name_map, documents, bm25 = ranking_function.startup()

def test_QueryFromLecture1():
        testresults1 = ['Lesson 1.2_ Text Access _ Coursera_result.txt', 'lesson1.2.txt', 'Lesson 6.9_ Recommender Systems_ Collaborative Filtering - Part 3 _ Coursera_result.txt', 'Lesson 6.4_ Future of Web Search _ Coursera_result.txt', 'lesson6.3.txt', 'lesson6.4.txt', 'Lesson 6.10_ Summary for Exam 1 _ Coursera_result.txt', 'Lesson 6.5_ Recommender Systems_ Content-Based Filtering - Part 1 _ Coursera_result.txt', 'lesson6.5.txt', '10.4 Text Clustering_ Generative Probabilistic Models Part 3 (OPTIONAL) _ Coursera_result.txt']
        results1 = ranking_function.search("push pull", file_name_map, bm25)
        assert results1 == testresults1
        assert len(results1) == 10

def test_QueryFromLecture2():
        testresults2 = ['lesson2.5.txt', 'lesson2.4.txt', 'Lesson 2.6_ System Implementation - Fast Search _ Coursera_result.txt', 'lesson2.6.txt', 'Lesson 2.4_ Implementation of TR Systems _ Coursera_result.txt', 'Lesson 2.5_ System Implementation - Inverted Index Construction _ Coursera_result.txt', 'Lesson 5.5_ Web Indexing _ Coursera_result.txt', 'lesson5.5.txt', 'lesson6.5.txt', 'Lesson 6.10_ Summary for Exam 1 _ Coursera_result.txt']
        results2 = ranking_function.search("inverted index", file_name_map, bm25)
        print(results2)
        assert results2 == testresults2
        assert len(results2) == 10

def test_QueryFromLecture3():
        testresults3 = ['lesson3.3.txt', 'lesson3.2.txt', 'lesson11.4.txt', 'lesson3.4.txt', 'Lesson 3.2_ Evaluation of TR Systems - Basic Measures _ Coursera_result.txt', 'Lesson 3.3_ Evaluation of TR Systems - Evaluating Ranked Lists - Part 1 _ Coursera_result.txt', 'lesson11.3.txt', '11.4 Text Categorization_ Evaluation Part 2 _ Coursera_result.txt', '11.3 Text Categorization_ Evaluation Part 1 _ Coursera_result.txt', 'Lesson 3.4_ Evaluation of TR Systems - Evaluating Ranked Lists - Part 2 _ Coursera_result.txt']
        results3 = ranking_function.search("precision recall ", file_name_map, bm25)
        print(results3)
        assert results3 == testresults3
        assert len(results3) == 10

def test_QueryFromLecture4():
        testresults4 = ['lesson4.2.txt', 'lesson8.7.txt', 'Lesson 4.2_ Statistical Language Model _ Coursera_result.txt', '8.8 Probabilistic Topic Models_ Overview of Statistical Language Models_ Part 1 _ Coursera_result.txt', 'lesson5.3.txt', 'lesson4.7.txt', 'lesson1.4.txt', 'lesson12.8.txt', 'lesson1.1.txt', 'lesson7.2.txt']
        results4 = ranking_function.search("statistical language model", file_name_map, bm25)
        assert results4 == testresults4
        assert len(results4) == 10

def test_QueryFromLecture5():
        testresults5 = ['lesson5.2.txt', 'Lesson 5.2_ Feedback in Vector Space Model - Rocchio _ Coursera_result.txt', 'lesson6.5.txt', 'Lesson 6.3_ Learning to Rank - Part 3 (OPTIONAL) _ Coursera_result.txt', 'lesson6.1.txt', 'Lesson 6.10_ Summary for Exam 1 _ Coursera_result.txt', 'Lesson 5.3_ Feedback in Text Retrieval - Feedback in LM _ Coursera_result.txt', 'lesson5.3.txt', 'lesson5.1.txt', 'Lesson 5.1_ Feedback in Text Retrieval _ Coursera_result.txt']
        results5 = ranking_function.search("rocchio feedback", file_name_map, bm25)
        assert results5 == testresults5
        assert len(results5) == 10

def test_QueryFromLecture6():
        testresults6 = ['lesson6.3.txt', 'lesson6.4.txt', 'Lesson 6.5_ Recommender Systems_ Content-Based Filtering - Part 1 _ Coursera_result.txt', 'Lesson 6.7_ Recommender Systems_ Collaborative Filtering - Part 1 _ Coursera_result.txt', 'Lesson 6.9_ Recommender Systems_ Collaborative Filtering - Part 3 _ Coursera_result.txt', 'Lesson 6.6_ Recommender Systems_ Content-Based Filtering - Part 2 _ Coursera_result.txt', 'lesson6.5.txt', 'lesson1.2.txt', 'Lesson 1.2_ Text Access _ Coursera_result.txt', 'Lesson 6.8_ Recommender Systems_ Collaborative Filtering - Part 2 _ Coursera_result.txt']
        results6 = ranking_function.search("filtering", file_name_map, bm25)
        assert results6 == testresults6
        assert len(results6) == 10
        
def test_QueryFromLecture7():
        testresults7 = ['7.7 Word Association Mining and Analysis _ Coursera_result.txt', 'lesson7.4.txt', '8.4 Syntagmatic Relation Discovery_ Mutual Information_ Part 2 _ Coursera_result.txt', '7.9 Paradigmatic Relation Discovery Part 2 _ Coursera_result.txt', 'lesson7.5.txt', 'lesson8.3.txt', 'lesson12.8.txt', '8.5 Topic Mining and Analysis_ Motivation and Task Definition _ Coursera_result.txt', 'lesson8.2.txt', '8.2 Syntagmatic Relation Discovery_ Conditional Entropy _ Coursera_result.txt']
        results7 = ranking_function.search("paradigmatic and syntagmatic", file_name_map, bm25)
        assert results7 == testresults7
        assert len(results7) == 10

def test_QueryFromLecture8():
        testresults8 = ['8.6 Topic Mining and Analysis_ Term as Topic _ Coursera_result.txt', 'lesson8.5.txt', 'lesson8.6.txt', 'lesson7.5.txt', 'Lesson 1.5_ Vector Space Model - Basic Idea _ Coursera_result.txt', '8.10 Probabilistic Topic Models_ Mining One Topic _ Coursera_result.txt', '9.8 Probabilistic Latent Semantic Analysis (PLSA)_ Part 2 _ Coursera_result.txt', '8.7 Topic Mining and Analysis_ Probabilistic Topic Models _ Coursera_result.txt', 'Lesson 4.5_ Statistical Language Model - Part 2 _ Coursera_result.txt', '12.6 Contextual Text Mining_ Mining Topics with Social Network Context _ Coursera_result.txt']
        results8 = ranking_function.search("term as topic", file_name_map, bm25)
        assert results8 == testresults8
        assert len(results8) == 10

def test_QueryFromLecture9():
        testresults9 = ['8.9 Probabilistic Topic Models_ Overview of Statistical Language Models_ Part 2 _ Coursera_result.txt', '9.6 Probabilistic Topic Models_ Expectation-Maximization Algorithm_ Part 3 _ Coursera_result.txt', '8.10 Probabilistic Topic Models_ Mining One Topic _ Coursera_result.txt', '9.3 Probabilistic Topic Models_ Mixture Model Estimation_ Part 2 _ Coursera_result.txt', 'Lesson 5.3_ Feedback in Text Retrieval - Feedback in LM _ Coursera_result.txt', '9.10 Latent Dirichlet Allocation (LDA)_ Part 2 _ Coursera_result.txt', 'Lesson 4.6_ Smoothing Methods - Part 1 _ Coursera_result.txt', '9.1 Probabilistic Topic Models_ Mixture of Unigram Language Models _ Coursera_result.txt', '9.7 Probabilistic Latent Semantic Analysis (PLSA)_ Part 1 _ Coursera_result.txt', '9.8 Probabilistic Latent Semantic Analysis (PLSA)_ Part 2 _ Coursera_result.txt']
        results9 = ranking_function.search("likelihood and ML", file_name_map, bm25)
        assert results9 == testresults9
        assert len(results9) == 10

def test_QueryFromLecture10():
        testresults10 = ['10.7 Text Categorization_ Motivation _ Coursera_result.txt', 'lesson10.7.txt', '8.8 Probabilistic Topic Models_ Overview of Statistical Language Models_ Part 1 _ Coursera_result.txt', '9.8 Probabilistic Latent Semantic Analysis (PLSA)_ Part 2 _ Coursera_result.txt', '11.2 Text Categorization_ Discriminative Classifier Part 2 (OPTIONAL) _ Coursera_result.txt', '7.1 Overview Text Mining and Analytics_ Part 1 _ Coursera_result.txt', 'lesson12.8.txt', 'lesson7.1.txt', 'lesson10.1.txt', 'lesson12.3.txt']
        results10 = ranking_function.search("categorize text", file_name_map, bm25)
        assert results10 == testresults10
        assert len(results10) == 10

def test_QueryFromLecture11():
        testresults11 = ['lesson11.5.txt', '11.5 Opinion Mining and Sentiment Analysis_ Motivation _ Coursera_result.txt', 'lesson11.6.txt', 'lesson12.1.txt', 'lesson12.8.txt', 'lesson12.2.txt', 'lesson7.3.txt', '12.2 Opinion Mining and Sentiment Analysis_ Latent Aspect Rating Analysis Part 2 (OPTIONAL) _ Coursera_result.txt', '11.6 Opinion Mining and Sentiment Analysis_ Sentiment Classification _ Coursera_result.txt', 'lesson7.1.txt']
        results11 = ranking_function.search("opinion mining", file_name_map, bm25)
        assert results11 == testresults11
        assert len(results11) == 10

def test_QueryFromLecture12():
        testresults12 = ['lesson12.7.txt', 'lesson3.1.txt', 'lesson3.6.txt', 'Lesson 3.1_ Evaluation of TR Systems _ Coursera_result.txt', 'lesson11.3.txt', 'lesson10.6.txt', '12.3 Text-Based Prediction _ Coursera_result.txt', '12.8 Summary for Exam 2 _ Coursera_result.txt', 'lesson3.2.txt', 'Lesson 6.2_ Learning to Rank - Part 2 (OPTIONAL) _ Coursera_result.txt']
        results12 = ranking_function.search("test based prediction", file_name_map, bm25)
        assert results12 == testresults12
        assert len(results12) == 10

def test_LongQuery():
        testresults = ['10.6 Text Clustering_ Evaluation _ Coursera_result.txt', '10.1 Text Clustering_ Motivation _ Coursera_result.txt', '12.4 Contextual Text Mining_ Motivation _ Coursera_result.txt', '10.5 Text Clustering_ Similarity-based Approaches _ Coursera_result.txt', '10.2 Text Clustering_ Generative Probabilistic Models Part 1 (OPTIONAL) _ Coursera_result.txt', '7.2 Overview Text Mining and Analytics_ Part 2 _ Coursera_result.txt', 'lesson10.3.txt', 'Lesson 6.1_ Learning to Rank - Part 1 (OPTIONAL) _ Coursera_result.txt', '11.5 Opinion Mining and Sentiment Analysis_ Motivation _ Coursera_result.txt', '12.8 Summary for Exam 2 _ Coursera_result.txt']
        results = ranking_function.search("lessons that include information about clustering", file_name_map, bm25)
        assert results == testresults
        assert len(results) == 10

def test_ShortQuery():
        testresults = ['lesson3.4.txt', 'Lesson 3.4_ Evaluation of TR Systems - Evaluating Ranked Lists - Part 2 _ Coursera_result.txt', 'lesson6.1.txt', 'Lesson 3.5_ Evaluation of TR Systems - Multi-Level Judgements _ Coursera_result.txt', 'Lesson 6.1_ Learning to Rank - Part 1 (OPTIONAL) _ Coursera_result.txt', '11.4 Text Categorization_ Evaluation Part 2 _ Coursera_result.txt', 'Lesson 1.6_ Vector Space Retrieval Model - Simplest Instantiation _ Coursera_result.txt', 'Lesson 5.1_ Feedback in Text Retrieval _ Coursera_result.txt', 'Lesson 6.3_ Learning to Rank - Part 3 (OPTIONAL) _ Coursera_result.txt', 'Lesson 1.4_ Overview of Text Retrieval Methods _ Coursera_result.txt']
        results = ranking_function.search("rank", file_name_map, bm25)
        assert results == testresults
        assert len(results) == 10