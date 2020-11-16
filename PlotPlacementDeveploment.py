import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('xx-small')

#Values manually extracted from textdumps
suomi1 = [3, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
turkki1 = [2, 4, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
helsinki1 = [11, 7, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
thaimaa1 = [8, 3, 7, 4, 4, 5, 5, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4]
kanaria1 = [6, 6, 8, 8, 8, 8, 6, 5, 4, 4, 4, 4, 4, 5, 5, 5, 5, ]
kreikka1 = [4, 5, 6, 7, 7, 7, 8, 8, 8, 8, 8, 7, 7, 6, 6, 6, 6]
alanya1 = [12, 12, 12, 9, 11, 12, 11, 12, 12, 12, 12, 10, 9, 9, 9, 7, 7]
italia1 = [1, 2, 3, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 8]
bulgaria1 = [9, 8, 5, 6, 5, 4, 4, 4, 6, 6, 6, 6, 6, 7, 7, 8, 9]
intia1 = [13, 13, 13, 13, 13, 13, 12, 10, 10, 10, 10, 11, 11, 10, 10, 10, 10]

x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
plt.plot(x, suomi1, label="Finland")
plt.plot(x, turkki1, label="Turkey")
plt.plot(x, helsinki1, label="Helsinki")
plt.plot(x, thaimaa1, label="Thailand")
plt.plot(x, italia1, label="Italy")
plt.plot(x, kanaria1, label="Canary Islands")
plt.plot(x, kreikka1, label="Greece")
plt.plot(x, alanya1, label="Alanya")
plt.plot(x, bulgaria1, label="Bulgaria")
plt.plot(x, intia1, label="India")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title("Top-10 placement deveploment")
plt.show()