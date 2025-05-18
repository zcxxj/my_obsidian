# visualize.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_words(counter, top_n=20):
    """
    绘制词频柱状图
    """
    top_words = counter.most_common(top_n)
    words, counts = zip(*top_words)

    plt.figure(figsize=(12, 6))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title("Top {} Frequent Words".format(top_n))
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def plot_wordcloud(counter):
    """
    绘制词云图
    """
    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate_from_frequencies(counter)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud")
    plt.show()
