import bs4 as bs
import urllib.request
import re
import nltk as n
import heapq

def retrieve(query):
    search_query = query
    if search_query[0] == " ":
        search_query = search_query.split(" ")[1]
    search_query = search_query.replace(" ","_")
    print("Searching ... \n",search_query)

    base_url = "http://simple.wikipedia.com/wiki/?search="
    search_url = base_url+search_query

    scaraped_data = urllib.request.urlopen(search_url)
    article = scaraped_data.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text=""
    for p in paragraphs:
        article_text+=p.text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    #article_text = content #Original content might come in handy later
    #article_text = re.sub(r'\[[0-9]*\]', ' ', article_text) #strip the numbers :P 
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


# earch = retrieve(" water")
# print(earch)
