# r/Munich DA

from plt_hndlr import plot_histogram
from pprint import pprint
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

from dt_handler import clean_description

#TODO Most used words in title (Per flair)
#? Averege N of likes per flair
#? Number of posts per flair

#? Number of upvotes per flair
VIZ = {'text_info': False,
        'flair': False,
        'flair_avr_ups': True,
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
    #hista = flairs.hist(bins = len(flairs))
    bar = flairs.plot.bar()
    plt.show()
    #plot_histogram(flairs, 'yolo')

if VIZ['flair_avr_ups']:
    r_dtst['flair'] = r_dtst['flair'].fillna(value='Not Specified')
    uniq_flairs = r_dtst['flair'].unique() # Get a list of unique flairs
    flair_ls = []
    for uniq_flair in uniq_flairs:
        flair_ups = r_dtst[r_dtst['flair'].values == uniq_flair]
        #print(uniq_flair, flair_ups['upvotes'].mean())
        flair_dict = {}
        flair_dict['upvotes'] = int(flair_ups['upvotes'].mean())
        flair_dict['flair'] = uniq_flair
        flair_ls.append(flair_dict)

    flair_ds = pd.DataFrame(flair_ls).sort_values('upvotes', ascending=False)
    bar = flair_ds.plot.bar(x='flair', y='upvotes')
    plt.show()

