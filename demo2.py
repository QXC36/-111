import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from wordcloud import WordCloud
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
myfont = mpl.font_manager.FontProperties(fname='simhei.ttf')
font = {'family': 'simhei', 'weight': 'normal', 'size': 15, }
# read Data
world_cups = pd.read_csv("Data/WorldCupsSummary.csv")
world_cup_players = pd.read_csv("Data/WorldCupPlayers.csv")
world_cup_matches = pd.read_csv("Data/WorldCupMatches.csv")

gold = world_cups["Winner"]
silver = world_cups["Second"]
bronze = world_cups["Third"]

gold_count = pd.DataFrame.from_dict(gold.value_counts())
silver_count = pd.DataFrame.from_dict(silver.value_counts())
bronze_count = pd.DataFrame.from_dict(bronze.value_counts())
podium_count = gold_count.join(silver_count, how='outer').join(bronze_count, how='outer')
podium_count = podium_count.fillna(0)
podium_count.columns = ['WINNER', 'SECOND', 'THIRD']
podium_count = podium_count.astype('int64')
podium_count = podium_count.sort_values(by=['WINNER', 'SECOND', 'THIRD'], ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
podium_count.plot(y=['WINNER', 'SECOND', 'THIRD'], kind="bar",
                  color=['gold', 'silver', 'brown'], fontsize=14, width=0.8, align='center', ax=ax)
ax.spines[['right', 'top']].set_visible(False)
plt.xlabel('Countries')
plt.ylabel('Number of podium')
plt.title('Number of podium by country')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
plt.subplot(221)
g1 = sns.barplot(x="Year", y="Attendance", data=world_cups, palette="Blues")
g1.set_title("ATTENDANCE PER CUP", size=14)
plt.subplot(222)
g2 = sns.barplot(x="Year", y="QualifiedTeams", data=world_cups, palette="Blues")
g2.set_title("NUMBER OF TEAMS PER CUP", size=14)
plt.subplot(223)
g2 = sns.barplot(x="Year", y="MatchesPlayed", data=world_cups, palette="Blues")
g2.set_title("NUMBER OF MATCHS PER CUP", size=14)
plt.subplot(224)
g2 = sns.barplot(x="Year", y="GoalsScored", data=world_cups, palette="Blues")
g2.set_title("NUMBER OF GOALS PER CUP", size=14)
plt.subplots_adjust(wspace=0.2, hspace=0.4, top=0.9)
plt.tight_layout()
plt.show()

winner_by_score_home = world_cup_matches['Home Team Goals'] > world_cup_matches['Away Team Goals']
winner_by_score_away = world_cup_matches['Home Team Goals'] < world_cup_matches['Away Team Goals']
win_by_score = winner_by_score_home | winner_by_score_away

win_team_home = np.where(winner_by_score_home, world_cup_matches['Home Team Name'], '')
win_team_away = np.where(winner_by_score_away, world_cup_matches['Away Team Name'], '')

win_team = np.where(win_team_home != '', win_team_home, win_team_away)
world_cup_matches.loc[:, 'Winner'] = win_team
world_cup_matches.loc[:, 'Looser'] = np.where(win_team == world_cup_matches['Home Team Name'],
                                              world_cup_matches['Away Team Name'],
                                              world_cup_matches['Home Team Name'])

cup_mask = np.array(Image.open("WordCloud/fifa-cup.jpg"))
wc_cup = WordCloud(background_color="white", max_words=2000, mask=cup_mask)
winner_text = ' '.join(world_cup_matches['Winner'].dropna().tolist())
wc_cup.generate(winner_text)
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
plt.title('Word cloud of the team that have the most wins', fontsize=14)
plt.imshow(wc_cup, interpolation='bilinear')
plt.axis("off")
plt.show()

