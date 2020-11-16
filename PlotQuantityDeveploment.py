import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('xx-small')
#Values manually extracted from textdumps
suomi = [121, 321, 704, 2601, 5514, 9016, 12529, 15761, 18767, 21219, 23512, 25699, 27883, 30362, 32057, 33997, 35596]
turkki = [122, 238, 582, 2719, 6573, 9957, 12489, 14475, 16245, 18310, 20237, 22356, 24693, 27037, 28178, 30346, 31274]
helsinki = [52, 189, 507, 2305, 5078, 8424, 11175, 13743, 15968,17973,19689,21642, 23664, 25502, 26554, 27839, 28822]
thaimaa = [62, 259, 413, 1129, 2383, 3734, 5279, 7070, 8938, 10812, 12645, 13803, 15323, 17014, 18817, 20935, 23029]
kanaria = [73, 191, 329, 862, 1646, 2994, 4843, 7416, 9717, 11369, 12668, 13256, 15512, 16948, 17732, 18569, 18913, ]
kreikka = [82, 227, 430, 886, 1760, 3064, 4172, 4999, 5700, 6510, 7336, 8490, 9099, 9634, 10333, 10685, 10839]
alanya = [0, 0, 126, 750, 1365, 2018, 2771, 3456, 4101, 4782, 5545, 6625, 7712, 8695, 9144, 10222, 10665]
italia = [145, 306, 533, 1103, 2041, 3218, 4264, 5568, 6434, 7038, 7549, 8074, 8680, 9047, 9244, 9436, 9604]
bulgaria = [60, 165, 452, 985, 2192, 4949, 6659, 7564, 8094, 8430, 8702, 8974, 9190, 9308, 9369, 9474, 9552]
intia = [27, 100, 188, 404,866, 1504, 2753, 3999, 4738, 5449, 5979, 6483, 6895, 7548, 7993, 8187, 8433]

x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
plt.plot(x, suomi, label="Finland")
plt.plot(x, turkki, label="Turkey")
plt.plot(x, helsinki, label="Helsinki")
plt.plot(x, thaimaa, label="Thailand")
plt.plot(x, italia, label="Italy")
plt.plot(x, kanaria, label="Canary Islands")
plt.plot(x, kreikka, label="Greece")
plt.plot(x, alanya, label="Alanya")
plt.plot(x, bulgaria, label="Bulgaria")
plt.plot(x, intia, label="India")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title("Top-10 quantity deveploment")
plt.show()

