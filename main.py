# r/Munich DA

from plt_hndlr import plot_histogram
from pprint import pprint
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

from dt_handler import clean_description

#? Most used words in title (Per flair)

#? Number of upvotes per flair
VIZ = {'text_info': False,
        'flair': True,
        'weekly_dist': False,
        'daily_dist': False,
        'pet_data': False,
        'wordcloud': False,
        'area_price': False
        }

# Read data
r_dtst = pd.read_csv('data\MunichParsedDt.csv', sep='\t', encoding='utf-8')

if VIZ['text_info']:
    pop_words = r_dtst['title'].to_list()
    pop_text = clean_description(pop_words)
    freq = Counter(pop_text.split()).most_common(50)
    ban_list = ['in', 'to', 'for', 'the', 'a', 'i', 'of', 'and', 'with', 'at', 'you', 'from', 'is', 'can', 'it', 'my','s', 'on', 'where', 'this', 'how', 'any', 'your']

    # for ban in ban_list:
    #     freq.pop[ban]
    pprint(freq)

if VIZ['flair']:

    flairs = r_dtst['flair'].value_counts()
    print(flairs)
    hista = flairs.hist(bins = len(flairs))
    plt.show()
    #plot_histogram(flairs, 'yolo')