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
# read Data
world_cups = pd.read_csv("Data/WorldCupsSummary.csv")
world_cup_players = pd.read_csv("Data/WorldCupPlayers.csv")
world_cup_matches = pd.read_csv("Data/WorldCupMatches.csv")
# WorldCups.csv文件统计了世界杯时间、不同国家队伍获得不同等级奖项的次数
# WorldCupPlayers文件统计了世界杯参赛队伍简称、教练名字、队员的号码、球员名字、球员位置（GK表示守门员）
# WorldCupMatches.csv表示比赛场次、时间、队伍、主客队名称、进球个数、等。

fig, ax = plt.subplots(figsize=(12, 6))
all_pos = world_cups[['Winner', 'Second', 'Third', 'Fourth']]
all_positions = all_pos.apply(pd.value_counts).fillna(0).astype(int)  # 对于空值，我们用0填充
all_positions.plot(y=['Winner', 'Second', 'Third', 'Fourth'], kind='bar', fontsize=12, ax=ax)
plt.xlabel('Teams')
plt.ylabel('Number of winnings')
ax.spines[['right', 'top']].set_visible(False)
# sns.despine(right=True,top=True)
plt.tight_layout()
plt.xticks(rotation=280)
plt.show()

goal = world_cups[['Year', 'GoalsScored']]
fig1, ax = plt.subplots(figsize=(12, 6))
plt.plot(goal['Year'], goal['GoalsScored'], '-p', color='gray', markersize=15, linewidth=6, markerfacecolor='r',
         markeredgecolor='gray')
plt.xlim(1930, 2018)
plt.ylim(60, 180)
plt.xlabel('Year', fontstyle='italic')
ax.spines[['right', 'top']].set_visible(False)
plt.ylabel('进球数', size=15)
plt.title('历届进球总数折线图', size=20)
plt.show()

Crowd = world_cups[['Year', 'Attendance']]
fig2, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=Crowd['Year'].astype(int), y=Crowd['Attendance'].astype(int))
ax.spines[['right', 'top']].set_visible(False)
plt.ylabel('Attendance', size=15)
plt.xlabel('Year', size=15)
plt.title('观赛人数 1930 -- 2018', size=20)
plt.show()

# 半场进球数 主队 客队
Half_time = world_cup_matches.groupby('Year')['Half-time Home Goals', 'Half-time Away Goals'].sum().reset_index().astype(int)
fig3, ax = plt.subplots(figsize=(12, 6))
df = pd.DataFrame({'Half-time Away Goals': Half_time['Half-time Away Goals'],
                   'Half-time Home Goals': Half_time['Half-time Home Goals']})
df.plot(kind='bar', stacked=True, ax=ax)
ax.legend(['半场客队进球数', '半场主队进球数'], prop=font, labelspacing=1, loc=0)
plt.title('半场时主客队进球数')
r = range(0, 20)
plt.xticks(r, Half_time['Year'])
plt.xlabel('Year')
ax.spines[['right', 'top']].set_visible(False)
plt.xticks(rotation=300)
plt.show()

fig4, ax = plt.subplots(figsize=(12, 6))
home_team1 = world_cup_matches[['Year', 'Home Team Goals']]
home_team = world_cup_matches[['Year', 'Home Team Goals']].astype(int)
sns.violinplot(x=home_team['Year'], y=home_team['Home Team Goals'], palette='Blues', ax=ax)
ax.spines[['right', 'top']].set_visible(False)
plt.grid(True, color='grey', alpha=0.3)
plt.title("主队进球数", size=20)
plt.show()

fig5, ax = plt.subplots(figsize=(12, 6))
# 客队  Away Team Goals
away_team = world_cup_matches[['Year', 'Away Team Goals']].astype(int)
sns.violinplot(x=away_team['Year'], y=away_team['Away Team Goals'], palette='Greens', ax=ax)
ax.spines[['right', 'top']].set_visible(False)
plt.grid(True, color='grey', alpha=0.3)
plt.title("客队进球数", size=20)
plt.show()

fig6, ax = plt.subplots(figsize=(12, 6))
g = sns.barplot(x='Year', y='GoalsScored', data=world_cups, ax=ax)
ax.spines[['right', 'top']].set_visible(False)
g.set_xticklabels(g.get_xticklabels(), rotation=300)
g.set_title('历届进球数')

for i in ax.containers:
    ax.bar_label(i, )
plt.show()

fig6, ax = plt.subplots(figsize=(12, 6))
g = sns.barplot(x='Year', y='MatchesPlayed', data=world_cups, ax=ax)
ax.spines[['right', 'top']].set_visible(False)
g.set_xticklabels(g.get_xticklabels(), rotation=300)
g.set_title('历届比赛场数')

for i in ax.containers:
    ax.bar_label(i, )
plt.show()

fig7, ax = plt.subplots(figsize=(12, 6))
homeTeambyYear = world_cup_matches.groupby(['Year', 'Home Team Name'])['Home Team Goals'].sum()
awayTeambyYear = world_cup_matches.groupby(['Year', 'Away Team Name'])['Away Team Goals'].sum()
teamsByYear = pd.concat([homeTeambyYear, awayTeambyYear], axis=1)
teamsByYear.fillna(0.0, inplace=True)
teamsByYear = teamsByYear.astype(int)
teamsByYear['Goals'] = teamsByYear['Home Team Goals'] + teamsByYear['Away Team Goals']
teamsByYear = teamsByYear.reset_index()
teamsByYear.columns = teamsByYear.columns.str.replace('level_1', 'Team Name')
teamsByYear = teamsByYear.sort_values(by=['Year', 'Goals'], ascending=[True, False])
top5Teams = teamsByYear.groupby('Year').head(5)
sns.barplot(x="Year", y='Goals', data=top5Teams, hue="Team Name", ax=ax)
ax.spines[['right', 'top']].set_visible(False)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
plt.title('历届进球数 Top5', size=20)
plt.tight_layout()
plt.show()
