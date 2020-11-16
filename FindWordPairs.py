import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt
fig = plt.figure(1, [20, 8])
raw = open('textdump/suomi24kommentit3.txt').read()
stop_words = set(stopwords.words('finnish'))
word_pairs =[]
tokens = []
sentences = sent_tokenize(raw)


for sent in sentences:
    sentence_tokens = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(sent)
    filtered_sentence = [w for w in sentence_tokens if not w in stop_words]
    pairs = list(nltk.bigrams(filtered_sentence))
    word_pairs.extend(pairs)

a = Counter(word_pairs)
most_common = list(a.most_common(10))
new_list = []

for object in most_common:
    str1 = ""
    for ele in object[0]:
        str1 += ele
    temp_list = []
    temp_list.append(str1)
    temp_list.append(object[1])
    new_list.append(temp_list)
print(new_list)


plt.bar(*zip(*new_list), width=0.5, color='g')
ax = fig.add_subplot(111)
ax.set_xlim(-1,10)
plt.title('Most common word pairs in a sentence')
plt.show()

