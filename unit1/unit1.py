import spacy

bookLoc1 = 'xmascarol1.txt'
bookLoc2 = 'xmascarol2.txt'


nlp = spacy.load('en')

#load part of Dickens, A Christmas Carol into the model
with open(bookLoc1, 'r') as f:
    text1 = f.read()

doc1 = nlp(text1)

with open(bookLoc2, 'r') as f:
    text2 = f.read()


"""
for token in doc:
    print(token.text,
          token.lemma_,
          token.pos_,
          token.dep_,
          token.shape_,
          token.is_stop)
"""

words2learn=set()

for token in doc1:
    words2learn.add((token.lemma_,token.pos_))

#remove punctuation
for token in doc1:
    if token.pos_ == 'PUNCT':
        words2learn.discard((token.lemma_,token.pos_))

#remove stopwords
for token in doc1:
    if token.is_stop:
        words2learn.discard((token.lemma_,token.pos_))

#remove propernouns (?)
for token in doc1:
    if token.pos_ == 'PROPN':
        words2learn.discard((token.lemma_,token.pos_))

"""
for word in words2learn:
    print(word)
"""


learnedWords = set()
#so you start learning the words

learnedWords = learnedWords|words2learn
#now you have learned those words

#function that creates a set of usable words with POS from a text
def text2list(text):
    doc = nlp(text)
    w2l = set()
    for token in doc:
        if token.pos_ not in ['PUNCT','PROPN','SPACE','NUM','SYM'] and not token.is_stop:
            w2l.add((token.lemma_,token.pos_))
    return w2l

#create second list
secondList = text2list(text2)

#eliminate the words 
words2learn = secondList - learnedWords

#and we learned those words
learnedWords = learnedWords|words2learn

#something harder

import urllib
from bs4 import BeautifulSoup

texts = []

for story in range(1,15):
    url = 'https://www.eslfast.com/supereasy/se/supereasy' + ('00'+str(story))[-3:] + '.htm'
    page = urllib.request.urlopen(url).read()
    text = BeautifulSoup(page, "html.parser").find(class_='MsoNormal').text
    texts.append(text)

learnedWords=set()
for text in texts:
    print("Lesson ",texts.index(text)+1,"        Learned words: ",len(learnedWords))
    print(text)
    words2learn = text2list(text)-learnedWords
    for word in words2learn:
        print(word[0],'('+word[1]+')')
    learnedWords = learnedWords|words2learn
    input()
