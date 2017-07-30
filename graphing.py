import numpy as np
import matplotlib.pyplot as plt
 
def plotData(n_groups, words, scores, occurances):
     
    # create plot
    fig, ax1 = plt.subplots()
    
    index = np.arange(len(words))
    bar_width = .35
    print(scores)
    ax1.bar(index,
            scores,
            bar_width,
            alpha=.6,
            color='b')
    #plt.title('Scores >1 Occurance for subreddit')
     
    ax2 = ax1.twinx()
    ax2.bar(index + bar_width,
            occurances,
            bar_width,
            alpha=.6,
            color='g')
    ax2.tick_params('y', colors='g')
    plt.xticks(index + bar_width / 2, words)
    plt.title("Highest Avg Karma words occuring >1")
    plt.show()
