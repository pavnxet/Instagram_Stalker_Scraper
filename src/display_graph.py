import matplotlib.pyplot as plt


# Display the bar graph
# Showing likes of each post from older to newer post

def plotBargraph(shortcodes, username):
    likes = [post['likes'] for post in reversed(shortcodes)]
    ind = list(range(len(likes)))

    plt.bar(ind, likes, edgecolor='black', linewidth=0.5)
    plt.xlabel('Posts (oldest → newest)')
    plt.ylabel('Like Count')
    plt.title(f'@{username}')
    plt.tight_layout()
    plt.show()
