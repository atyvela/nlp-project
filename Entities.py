import gzip
import spacy
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

path = "path to your data as plaintext created with s24-reader"
nlp = spacy.load('xx_ent_wiki_sm')
named_entities = []
comments =open("/textdump/suomi24kommentit4.txt", "w+")
entities = "/textdump/entities4.txt"

comments2001 =open("/suomi24vuodet2/suomi24kommentit2001.txt", "w+")
comments2002 =open("/suomi24vuodet2/suomi24kommentit2002.txt", "w+")
comments2003 =open("/suomi24vuodet2/suomi24kommentit2003.txt", "w+")
comments2004 =open("/suomi24vuodet2/suomi24kommentit2004.txt", "w+")
comments2005 =open("/suomi24vuodet2/suomi24kommentit2005.txt", "w+")
comments2006 =open("suomi24vuodet2/suomi24kommentit2006.txt", "w+")
comments2007 =open("/suomi24vuodet2/suomi24kommentit2007.txt", "w+")
comments2008 =open("/suomi24vuodet2/suomi24kommentit2008.txt", "w+")
comments2009 =open("/suomi24vuodet2/suomi24kommentit2009.txt", "w+")
comments2010 =open("/suomi24vuodet2/suomi24kommentit2010.txt", "w+")
comments2011 =open("/suomi24vuodet2/suomi24kommentit2011.txt", "w+")
comments2012 =open("/suomi24vuodet2/suomi24kommentit2012.txt", "w+")
comments2013 =open("/suomi24vuodet2/suomi24kommentit2013.txt", "w+")
comments2014 =open("/suomi24vuodet2/suomi24kommentit2014.txt", "w+")
comments2015 =open("/suomi24vuodet2/suomi24kommentit2015.txt", "w+")
comments2016 =open("/suomi24vuodet2/suomi24kommentit2016.txt", "w+")
comments2017 =open("/suomi24vuodet2/suomi24kommentit2017.txt", "w+")

filter_words = ["asia", "ongelma", "henkilö", "kaikki", "kannattaa", "juttu", "lapsi",]

stop_words = set(stopwords.words('finnish'))

def year(date, comment):
    if "2001" in date:
        comments2001.write(comment)
    elif "2002" in date:
        comments2002.write(comment)
    elif "2003" in date:
        comments2003.write(comment)
    elif "2004" in date:
        comments2004.write(comment)
    elif "2005" in date:
        comments2005.write(comment)
    elif "2006" in date:
        comments2006.write(comment)
    elif "2007" in date:
        comments2007.write(comment)
    elif "2008" in date:
        comments2008.write(comment)
    elif "2009" in date:
        comments2009.write(comment)
    elif "2010" in date:
        comments2010.write(comment)
    elif "2011" in date:
        comments2011.write(comment)
    elif "2012" in date:
        comments2012.write(comment)
    elif "2013" in date:
        comments2013.write(comment)
    elif "2014" in date:
        comments2014.write(comment)
    elif "2015" in date:
        comments2015.write(comment)
    elif "2016" in date:
        comments2016.write(comment)
    elif "2017" in date:
        comments2017.write(comment)
    return

with gzip.open(path, 'rt') as f:
    for line in f:
        if line.startswith("###C: datefrom = "):
            datesplit = line.split("###C: datefrom = ")
            date = datesplit[1]
        if line.startswith("###C: top = Matkailu"):
            #print(next(f))
            nextline = next(f)
            while nextline.startswith("###C"):
                nextline = next(f)
            while not nextline.startswith("###C"):
                if nextline != '\n':
                    #print(nextline)
                    comment = nextline
                    comments.write(comment)
                    year(date, comment)
                    doc = nlp(comment)
                    for ent in doc.ents:
                        if ent.label_ == "LOC" or ent.label_ == "GEO":
                            if ent.text not in stop_words and ent.text not in filter_words:
                                named_entities.append(ent.text)
                                print(ent.text, ent.label_)
                nextline = next(f)


a = Counter(named_entities)
print(a.most_common(10))
with open(entities, "w+") as ent:
    for k,v in a.most_common():
        ent.write("{} {}\n".format(k,v))
plt.bar(*zip(*a.most_common(10)), width=.5, color='g')
plt.show()