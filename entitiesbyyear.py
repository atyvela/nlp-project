import spacy
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

nlp = spacy.load('xx_ent_wiki_sm')
named_entities = []
paths = ["C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2001.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2002.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2003.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2004.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2005.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2006.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2007.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2008.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2009.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2010.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2011.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2012.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2013.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2014.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2015.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2016.txt",
         "C:/Users/elefa/Desktop/suomi24vuodet2/suomi24kommentit2017.txt"]

filter_words = ["asia", "ongelma", "henkilö", "kaikki", "kannattaa", "juttu", "lapsi",]

stop_words = set(stopwords.words('finnish'))

for path in paths:
    with open(path, 'r+') as f:
        for line in f:
            doc = nlp(line)
            for ent in doc.ents:
                if ent.label_ == "LOC" or ent.label_ == "GEO":
                    if(ent.text not in filter_words and ent.text not in stop_words):
                        named_entities.append(ent.text)
                        #print(ent.text, ent.label_)

    a = Counter(named_entities)
    print(path)
    print(a.most_common(30))
    plt.bar(*zip(*a.most_common(10)), width=.5, color='g')
    plt.title(path)
    plt.show()