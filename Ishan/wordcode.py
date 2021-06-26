import numpy as np
import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pariwise import cosine_similarity


responses = []
answers = []
with open('responses.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        
        responses.append(line)

with open('answers.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        answers.append(line)



tfidf = TfidfVectorizer(
    input='content',
    strip_accents='ascii',
    lowercase='True',
    stop_words='english')

r = tfidf.fit_transform(responses)
a = tfidf.transform(answers)


print(tfidf.get_feature_names())

cosine_sim = cosine_similarity(a, r)
print(cosine_sim)
