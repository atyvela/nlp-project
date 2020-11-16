import stanfordnlp
from collections import Counter
from spacy_stanfordnlp import StanfordNLPLanguage
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from polyglot.text import Text, Word
from polyglot.downloader import downloader
downloader.download("sentiment2.fi")

entities = "/textdump/entities4.txt"
adjectives = []
verbs = []

raw = open('/textdump/suomi24kommentit3.txt').read()
sentences = sent_tokenize(raw)
stop_words = set(stopwords.words('finnish'))

#Top 20 most common namend entities in the comments
words = ["asia", "Suomi", "Turkki", "Helsinki", "Thaimaa", "Kanaria", "Kreikka", "Australia",  "USA", "Thaimaa",
         "Alanyassa", "Italia", "Bulgaria", "Intia", "Gambia", "Teneriffa", "Turku", "Tunisia", "Tampere", "Usa"]

#initialize spacy with standord-nlp pipeline model for finnish language
snlp = stanfordnlp.Pipeline(lang="fi", processors="tokenize,mwt,lemma,pos")
nlp = StanfordNLPLanguage(snlp)

#Find adjectives and verbs from the comments:

for sentence in sentences:
    for word in words:
        if word in sentence:
            doc = nlp(sentence)
            for token in doc:
                if (token.text not in stop_words and token.pos_ == "ADJ"):
                    print(token.text, token.pos_)
                    adjectives.append((token.text))
                if (token.text not in stop_words and token.pos_ == "VERB"):
                    print(token.text, token.pos_)
                    verbs.append((token.text))
# a = Counter(adjectives)
# print(a.most_common(20))
# print(len(a))
# b = Counter(verbs)
# print(b.most_common(20))
# print(len(b))

#init lists for adjective types:
positive_adjectives = []
neutral_adjectives = []
negative_adjectives = []

#find out adjective sentiment and append to lists accordingly
for adjective in adjectives:
    w = Word(adjective, language="fi")
    if (w.polarity == -1):
        negative_adjectives.append(w)
    elif (w.polarity == 1):
        positive_adjectives.append(w)
    else:
        neutral_adjectives.append(w)

print(len(positive_adjectives))
print(len(negative_adjectives))
print(len(neutral_adjectives))

pos_a = Counter(positive_adjectives)
neg_a = Counter(negative_adjectives)
neut_a = Counter(neutral_adjectives)

#print 10 most commong positive, negative and neutral adjectives:
print(pos_a.most_common(10))
print(neg_a.most_common(10))
print(neut_a.most_common(10))

#init lists for verb types
positive_verbs = []
neutral_verbs = []
negative_verbs = []

#find out verbs sentiment and append to lists accordingly
for verb in verbs:
    w = Word(verb, language="fi")
    if (w.polarity == -1):
        negative_verbs.append(w)
    elif (w.polarity == 1):
        positive_verbs.append(w)
    else:
        neutral_verbs.append(w)

print(len(positive_verbs))
print(len(negative_verbs))
print(len(neutral_verbs))

pos_v = Counter(positive_verbs)
neg_v = Counter(negative_verbs)
neut_v = Counter(neutral_verbs)

#print 10 most commong positive, negative and neutral verbs:
print(pos_v.most_common(10))
print(neg_v.most_common(30))
print(neut_v.most_common(10))

positive_sentence = []
negative_sentence = []
neutral_sentence = []
positive_with_negative_adjective = []
positive_with_negative_verb = []

positive_with_positive_adjective = []
positive_with_positive_verb = []

negative_with_positive_adjective= []
negative_with_positive_verb = []


negative_with_negative_adjective = []
negative_with_negative_verb = []

text = Text(raw, hint_language_code='fi')

for sentence in text.sentences:
    for word in words:
        #check if comment has entity in it
        if word in sentence:
            sentence_polarity = sentence.polarity
            if sentence_polarity < 0:
                negative_sentence.append(sentence)
            elif sentence_polarity > 0:
                positive_sentence.append(sentence)
            elif sentence_polarity == 0:
                neutral_sentence.append((sentence))



print(len(positive_sentence))
print(len(negative_sentence))
print(len(neutral_sentence))

for sentence in positive_sentence:
    if any(adjective in sentence for adjective in negative_adjectives):
        positive_with_negative_adjective.append(sentence)
    if any(adjective in sentence for adjective in positive_adjectives):
        positive_with_positive_adjective.append(sentence)
    if any(verb in sentence for verb in negative_verbs):
        positive_with_negative_verb.append(sentence)
    if any(verb in sentence for verb in positive_verbs):
        positive_with_positive_verb.append(sentence)

for sentence in negative_sentence:
    if any(adjective in sentence for adjective in negative_adjectives):
        negative_with_negative_adjective.append(sentence)
    if any(adjective in sentence for adjective in positive_adjectives):
        negative_with_positive_adjective.append(sentence)
    if any(verb in sentence for verb in negative_verbs):
        negative_with_negative_verb.append(sentence)
    if any(verb in sentence for verb in positive_verbs):
        negative_with_positive_verb.append(sentence)

print(len(positive_with_negative_adjective))
print(len(positive_with_negative_verb))

print(len(positive_with_positive_adjective))
print(len(positive_with_positive_verb))

print(len(negative_with_positive_adjective))
print(len(negative_with_positive_verb))


print(len(negative_with_negative_adjective))
print(len(negative_with_negative_verb))

