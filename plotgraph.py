import matplotlib.pyplot as plt

def bar_graph(sentiment):
    values = list(sentiment.values())
    categories = list(sentiment.keys())
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Number of comments')
    plt.title('Comment Sentiment Distribution')
    plt.show()
