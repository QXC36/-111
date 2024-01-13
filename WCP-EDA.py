# player names
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
mpl.rcParams['axes.unicode_minus'] = False
myfont = mpl.font_manager.FontProperties(fname='simhei.ttf')
font = {'family': 'simhei', 'weight': 'normal', 'size': 15, }
world_cups = pd.read_csv("Data/WorldCupsSummary.csv")
world_cup_players = pd.read_csv("Data/WorldCupPlayers.csv")
world_cup_matches = pd.read_csv("Data/WorldCupMatches.csv")

plt.figure()
name = np.array(Image.open('WordCloud/player.jpg'))
worldcloud = WordCloud(mask=name, max_words=5000).generate(' '.join(world_cup_players['Player Name']))
plt.imshow(worldcloud, interpolation='bilinear')
plt.title('WorldCloud--球员名称', fontsize=14)
plt.axis('off')
plt.show()

plt.figure()
name = np.array(Image.open('WordCloud/coach.jpg'))
wordcloud = WordCloud(mask=name, max_words=5000).generate(' '.join(world_cup_players['Coach Name']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('WorldCloud--教练名称', fontsize=14)
plt.axis('off')
plt.show()

# Home Team Name
plt.figure()
name = np.array(Image.open('WordCloud/fifa-cup.jpg'))
wordcloud = WordCloud(background_color="white", mask=name).generate(' '.join(world_cup_matches['Home Team Name']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('WorldCloud--主队名称', fontsize=14)
plt.axis('off')
plt.show()

# Away Team Name
plt.figure()
wordcloud = WordCloud(background_color="white", mask=name).generate(' '.join(world_cup_matches['Away Team Name']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('WorldCloud--客队名称', fontsize=14)
plt.axis('off')
plt.show()
