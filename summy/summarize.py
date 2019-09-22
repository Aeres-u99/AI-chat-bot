import nltk as n
import re
import heapq
import requests as rs
from bs4 import BeautifulSoup

def summarize(stuffs):
    url = "http://"
    if "http" not in stuffs:
        url += stuffs
    else:
        url = stuffs
    print(url)
    page = rs.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    content = soup.get_text()
    article_text = content #Original content might come in handy later
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text) #strip the numbers :P 
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', article_text)    
    #print(formatted_article_text)

    sentence_list = n.sent_tokenize(article_text) #tokenize stuffs
    stopwords = n.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in n.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    
    maximum_frequncy = max(word_frequencies.values())
    
    #find word frequency
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in n.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

# test = summarize("www.wikipedia.com")
# print(test)
