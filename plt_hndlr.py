import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(data, title, n_bins = 12):
    """[Plot histogram]
    Args:
        data ([list]): [Data]
        title ([str]): [Plot title]
        n_bins (int, optional): [N of bins on graph]. Defaults to 12.
    Returns:
        [plt]: [Show plot]
    """
    datas = zip(*data)
    ticks = datas[0]
    kek = datas[1]

    plt.hist(kek, n_bins, facecolor='green', alpha= 0.5, rwidth = 0.5)
    plt.xlim(0,24)
    plt.xticks(ticks)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylabel('',fontsize=15)
    plt.xlabel('',fontsize=15)
    plt.title(title)

    return plt.show()