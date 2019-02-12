# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:00:25 2018

@author: USER
"""

import gc
import time
import re


def post_summarizer(article):
    stopWords = ['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't",
    'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how',
    'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
    're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very',
    'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
    art_words = re.split("\W", article)
    sentence_list = article.split('.')
    #sentence_list = re.split(r"\.\s*", article)

    xab = {}
    for i in art_words:
        if i.lower() not in stopWords:
            if i not in xab.keys():
                xab[i] = 1
            else:
                xab[i] += 1 
        else:
            continue
    
    max_weight = max(xab.values())
    xac = {}
    for i in xab.keys():
        xac[i] = xab[i]/max_weight
    
    xad = {}
    for i in sentence_list:
        xae = 0
        split_k = re.split("\s|,", i)
        for l in split_k:
            if l in xac.keys():
                xae += xac[l]
            else: pass
        xad[i] = xae
    
    maxy = sorted(xad.values())
    maxx = maxy[-1]
    
    summary_list = []
    for i in xad.keys():
        if xad[i] == maxx:
            summary_list.append(i)
        else: pass

    summary = summary_list[-1]
    return(summary)
    del article, stopWords, art_words, sentence_list, i, xab, max_weight, xac, xad, l, xae, split_k, maxy, maxx, summary_list, summary
    gc.collect()


va = "Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and other animals. Many tools are used in AI, including versions of search and mathematical optimization, artificial neural networks, and methods based on statistics, probability and economics. The traditional problems (or goals) of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception and the ability to move and manipulate objects. When access to digital computers became possible in the middle 1950s, AI research began to explore the possibility that human intelligence could be reduced to symbol manipulation. One proposal to deal with this is to ensure that the first generally intelligent AI is 'Friendly AI', and will then be able to control subsequently developed AIs. Nowadays, the vast majority of current AI researchers work instead on tractable 'narrow AI' applications (such as medical diagnosis or automobile navigation). Machine learning, a fundamental concept of AI research since the field's inception, is the study of computer algorithms that improve automatically through experience."
print(post_summarizer(va))
