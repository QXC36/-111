# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
mpl.rcParams['axes.unicode_minus'] = False
myfont = mpl.font_manager.FontProperties(fname='simhei.ttf')
font = {'family': 'simhei', 'weight': 'normal', 'size': 15, }
matches = pd.read_csv('Data/WorldCupMatches.csv')
hist_worldcup = pd.read_csv('Data/WorldCupsSummary.csv')
hist_worldcup = hist_worldcup.replace(['Germany FR'], 'Germany')
# print(matches[(matches['Away Team Name'] == 'China PR') | (matches['Home Team Name'] == 'China PR')])

matches = matches.replace(['Germany FR'], 'Germany')
# 类型转化
matches['Home Team Goals'] = matches['Home Team Goals'].astype(int)
matches['Away Team Goals'] = matches['Away Team Goals'].astype(int)
matches['result'] = matches['Home Team Goals'].astype(str) + "-" + matches['Away Team Goals'].astype(str)

top5_attendance = matches.sort_values(by='Attendance', ascending=False)[:5]
top5_attendance['VS'] = top5_attendance['Home Team Name'] + " VS " + top5_attendance['Away Team Name']
# top5_attendance['attend']= top5_attendance['Attendance'].astype(str)
plt.figure(figsize=(12, 6))
ax = sns.barplot(y=top5_attendance['VS'], x=top5_attendance['Attendance'])
sns.despine(right=True)
plt.ylabel('比赛队伍')
plt.xlabel('观赛人数')
plt.title('热门比赛 Top5', size=20)
for i, s in enumerate(
        "Stadium: " + top5_attendance['Stadium'] + "\nDate: " + top5_attendance['Datetime'] + "\nAttendance: " +
        top5_attendance['Attendance'].astype(str)):
    ax.text(1, i, s, fontsize=12, color='white', va='center')
plt.tight_layout()
plt.show()

matches['total_goals'] = matches['Home Team Goals'] + matches['Away Team Goals']
matches['VS'] = matches['Home Team Name'] + " VS " + matches['Away Team Name']
top10_goals = matches.sort_values(by='total_goals', ascending=False)[:10]
top10_goals['VS'] = top10_goals['Home Team Name'] + " VS " + top10_goals['Away Team Name']
top10_goals['total_goals_str'] = top10_goals['total_goals'].astype(str) + " goals scored"
top10_goals['Home Team Goals'] = top10_goals['Home Team Goals'].astype(int)
top10_goals['Away Team Goals'] = top10_goals['Away Team Goals'].astype(int)
top10_goals['result'] = top10_goals['Home Team Goals'].astype(str) + "-" + top10_goals['Away Team Goals'].astype(str)
plt.figure(figsize=(12, 6))
ax = sns.barplot(y=top10_goals['VS'], x=top10_goals['total_goals'])
sns.despine(right=True)
plt.ylabel('比赛队伍')
plt.xlabel('进球数')
plt.yticks(size=12)
plt.xticks(size=12)
plt.title('进球总数 Top10', size=20)
for i, s in enumerate("Stadium " + top10_goals['Stadium'] + ", Date: " + top10_goals['Datetime'] + "\n" +
                      top10_goals['total_goals_str'] + ", match result: " + top10_goals['result']):
    ax.text(1, i, s, fontsize=12, color='white', va='center')
plt.tight_layout()
plt.show()

# 取主客场进球数的绝对值
matches['difference_goals'] = pd.Series.abs(matches['Home Team Goals'] - matches['Away Team Goals'])
top10_difference = matches.sort_values(by='difference_goals', ascending=False)[:10]
top10_difference['difference_goals'] = top10_difference['difference_goals'].astype(int)
top10_difference['difference_goals_str'] = top10_difference['difference_goals'].astype(str) + " goals difference"
top10_difference['result'] = top10_difference['Home Team Goals'].astype(str) + "-" + top10_difference[
    'Away Team Goals'].astype(str)
plt.figure(figsize=(12, 6))
ax = sns.barplot(y=top10_difference['VS'], x=top10_difference['difference_goals'])
sns.despine(right=True)
plt.ylabel('比赛队伍')
plt.xlabel('进球差值')
plt.yticks(size=12)
plt.xticks(size=12)
plt.title('Top10 分差最大的比赛', size=20)
for i, s in enumerate(
        "Stadium " + top10_difference['Stadium'] + ", Date: " + top10_difference['Datetime'] + "\n" + "stage: " +
        top10_difference['Stage'] + ".  " +
        top10_difference['difference_goals_str'] + ", match result: " + top10_difference['result']):
    ax.text(1, i, s, fontsize=12, color='white', va='center')
plt.tight_layout()
plt.show()

list_countries = matches['Home Team Name'].unique().tolist()
# 分主客队来统计：
lista_home = []
lista_away = []
for i in list_countries:
    goals_home = matches.loc[matches['Home Team Name'] == i, 'Home Team Goals'].sum()
    lista_home.append(goals_home)
    goals_away = matches.loc[matches['Away Team Name'] == i, 'Away Team Goals'].sum()
    lista_away.append(goals_away)
df = pd.DataFrame({'country': list_countries, 'total_home_goals': lista_home, 'total_away_goals': lista_away})
df['total_goals'] = df['total_home_goals'] + df['total_away_goals']
most_goals = df.sort_values(by='total_goals', ascending=False)[:10]
fig, ax = plt.subplots(figsize=(12, 6))
plt.title('Top Goals Number by Country', size=16, weight='bold')
most_goals.plot(x="country", y=["total_home_goals", "total_away_goals", "total_goals"], kind="bar", ax=ax)
ax.spines[['right', 'top', 'left']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(labelleft=False, left=False, labelsize=14)
ax.legend(fontsize=20)
for i in ax.containers:
    ax.bar_label(i, fontsize=15)
plt.legend(['主队进球数', '客队进球数', '进球总数'], prop=font, labelspacing=1)
plt.xticks(rotation=300)
plt.tight_layout()
plt.show()

# finalist来自“世界杯成绩分析表”小节，表示进入决赛的队伍
countries = hist_worldcup[['Winner', 'Second', 'Third', 'Fourth']].apply(pd.value_counts).reset_index().fillna(0)
finalist = countries.drop(countries[(countries['Winner'] == 0) & (countries['Second'] == 0)].index)
finalista = finalist['index'].tolist()
# 分主、客场统计：
goalsconceded_home = []
goalsconceded_away = []
match1 = []
match2 = []
for i in finalista:
    goalsconc_home = matches.loc[matches['Home Team Name'] == i, 'Away Team Goals'].sum()
    goalsconceded_home.append(goalsconc_home)
    goalsconc_away = matches.loc[matches['Away Team Name'] == i, 'Home Team Goals'].sum()
    goalsconceded_away.append(goalsconc_away)
    counted1 = (matches['Home Team Name'] == i).sum()
    counted2 = (matches['Away Team Name'] == i).sum()

    match1.append(int(counted1))
    match2.append(int(counted2))
# 按照失球数排序
df = pd.DataFrame(
    {'country': finalista, 'goalsconceded_home': goalsconceded_home, 'goalsconceded_away': goalsconceded_away,
     'matches_home': match1, 'matches_away': match2})
df['total_matches'] = df['matches_home'] + df['matches_away']
df['total_goalsconceded'] = df['goalsconceded_home'] + df['goalsconceded_away']
df['goalmatch_rate'] = (df['total_goalsconceded'] / df['total_matches']).round(2)
goals_conceded = df.sort_values(by='goalmatch_rate')[:10]
fig2, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
goals_conceded.plot(x="country", y="total_goalsconceded", kind="bar", ax=ax[0], color='#ef475d')
ax[0].legend(['失球总数'], prop=font, labelspacing=1, loc=2)  # loc 调整标注框位置
ax[0].set_title('Total Goals Conceded by Country', size=20, weight='bold')
ax[0].spines[['right', 'top']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)

ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)
plt.xticks(rotation=300)
goals_conceded.plot(x="country", y="goalmatch_rate", kind="bar", ax=ax[1], color='#f0c9cf')
ax[1].legend(['失球率'], prop=font, labelspacing=1)
ax[1].set_title('Goals Conceded Ratio by Country', size=20, weight='bold')
ax[1].spines[['right', 'top']].set_visible(False)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[1].containers:
    ax[1].bar_label(i, fontsize=15)
for tick in ax[0].get_xticklabels():
    tick.set_rotation(300)
plt.xticks(rotation=300)
plt.tight_layout()
plt.show()
