import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
mpl.rcParams['axes.unicode_minus'] = False
hist_worldcup = pd.read_csv('Data/WorldCupsSummary.csv')

hist_worldcup = hist_worldcup.replace(['Germany FR'], 'Germany')

# print(hist_worldcup)
rng = np.random.RandomState(1)
colors = rng.rand(21)
fig1, ax = plt.subplots(figsize=(10, 6))
plt.title('现场观众人数变化趋势', size=20, weight='bold')
hist_worldcup.plot.scatter(x='Attendance', y='Year', c=colors, ax=ax, zorder=2, s=100)
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel('年份', size=20, loc='top')
ax.set_xlabel('人数', size=20)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(hist_worldcup['Year'].tolist())
ax.set_xticks([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000])
ax.ticklabel_format(style='plain')
plt.tick_params(bottom=False, left=False)
plt.show()

fig2, ax = plt.subplots(figsize=(10, 6))
plt.title('参赛队伍数变化趋势', size=20, weight='bold')
hist_worldcup.plot(y='QualifiedTeams', x='Year', ax=ax, zorder=2)
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xticks(hist_worldcup['Year'].tolist())
ax.set_yticks([0, 16, 24, 32])
plt.tick_params(bottom=False, left=False)
plt.xticks(rotation=300)

fig3, ax = plt.subplots(figsize=(10, 6))
sns.despine(right=True)
g = sns.barplot(x='Year', y='QualifiedTeams', data=hist_worldcup)
g.set_xticklabels(g.get_xticklabels(), rotation=80)
g.set_title('参赛队伍数变化趋势')
plt.show()

name = hist_worldcup['Year']
data = hist_worldcup['GoalsScored']
fig4, ax = plt.subplots(figsize=(10, 6))
b = ax.barh(range(len(name)), data, color='#f1939c')
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' % int(w), ha='left', va='center')
ax.set_yticks(range(len(name)))
ax.set_yticklabels(name)
plt.xticks(())
ax.set_xticks([0, 25, 50, 75, 100, 125, 150, 175])
ax.spines[['right', 'top']].set_visible(False)
plt.title('历界进球数变化趋势', loc='center', fontsize='20', fontweight='bold')
plt.show()

palette = ['coral', '#e16c96', '#e16c96', 'red', 'firebrick', 'coral', 'coral', 'firebrick']
fig5, ax = plt.subplots(figsize=(12, 6))
plt.title('各国夺冠次数', size=20, weight='bold')
sns.countplot(x=hist_worldcup['Winner'], palette=palette, linewidth=2.5, edgecolor=".2")
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False, labelsize=14)
for i in ax.containers:
    ax.bar_label(i, fontsize=15)
plt.show()

countries = hist_worldcup[['Winner', 'Second', 'Third', 'Fourth']].apply(pd.value_counts).reset_index().fillna(0)
countries['SemiFinal'] = countries['Winner'] + countries['Second'] + countries['Third'] + countries['Fourth']
countries['Final'] = countries['Winner'] + countries['Second']
# 设置颜色
clrs = [
    '#ef475d' if (i >= 8) else '#f0c9cf' if (5 <= i < 8) else '#ee4866' if (3 <= i < 5) else 'orangered' if (
            i == 2) else 'red'
    for i in countries['SemiFinal']]
fig6, ax = plt.subplots(figsize=(12, 6))
plt.title('半决赛队伍次数统计', size=20, weight='bold')
sns.barplot(data=countries, x='index', y='SemiFinal', palette=clrs, linewidth=3, edgecolor=".2")
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False, labelsize=14)
plt.xticks(rotation=270)
for i in ax.containers:
    ax.bar_label(i, fontsize=15)
plt.tight_layout()
plt.show()

finalist = countries.drop(countries[(countries['Winner'] == 0) & (countries['Second'] == 0)].index)
clrs = ['#ef475d' if (i >= 6) else '#f0c9cf' if (i == 5) else '#4e2a40' if (3 <= i < 5) else '#e16c96' if (
        i == 2) else 'red' for i
        in finalist['Final']]
fig7, ax = plt.subplots(figsize=(12, 6))
plt.title('决赛队伍次数统计')
sns.barplot(data=finalist, x='index', y='Final', palette=clrs, linewidth=3, edgecolor=".1")
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False, labelsize=14)
plt.xticks(rotation=270)
for i in ax.containers:
    ax.bar_label(i, fontsize=15)
plt.tight_layout()
plt.show()

finalist['rel_final'] = finalist['Winner'] / finalist['Final']  # preprocessing
relationship = np.round(finalist[(finalist['Second'] > 0) | (finalist['Winner'] > 0)], decimals=2)
# Set the color
clrs = ['#ef475d' if (i == 1) else '#f0c9cf' if (0.5 < i < 1) else 'firebrick' if (i == 0.5) else '#4e2a40' if (
        0 < i < 0.5) else 'red' for i in relationship['rel_final']]
fig8, ax = plt.subplots(figsize=(12, 6))
plt.title('进入决赛夺冠概率', size=20, weight='bold')
sns.barplot(data=relationship, x='index', y='rel_final', palette=clrs, linewidth=2.5, edgecolor=".2")
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False, labelsize=14)
plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i, fontsize=15)
plt.tight_layout()
plt.show()

fig9, ax = plt.subplots(figsize=(10, 6))
plt.title('历届夺冠队伍所属洲', size=20, weight='bold')
hist_worldcup.plot.scatter(x='WinnerContinent', y='Year', ax=ax, zorder=2, s=100)
ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(hist_worldcup['Year'].tolist())
plt.show()

index1 = hist_worldcup['WinnerContinent'].value_counts().index.tolist()
value1 = hist_worldcup['WinnerContinent'].value_counts().values.tolist()
palette = ['#ef475d', '#f0c9cf']
fig10, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.countplot(ax=ax[0], x=hist_worldcup['WinnerContinent'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Continent Numbers')
ax[0].spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)
plt.pie(value1, labels=index1, autopct='%.0f%%', colors=['#ef475d', '#f0c9cf'], wedgeprops={"edgecolor": "0",
                                                                                            'linewidth': 2.5,
                                                                                            'antialiased': True},
        startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Continent Ratios', size=20, weight='bold')
plt.show()


transpose = countries.T.rename(columns=countries.T.iloc[0]).drop(index=['index'])  # preprocessing transpose
transpose = transpose.reset_index()[0:4]
columns = transpose.columns[1:]
clr = ['#ef475d', '#f0c9cf', 'firebrick', '#4e2a40']
fig11, axes = plt.subplots(4, 6, figsize=(16, 8))
fig11.subplots_adjust(hspace=.5, top=1, wspace=.175)
for ax, col in zip(axes.flat, columns):
    sns.barplot(data=transpose, x='index', y=col, ax=ax, palette=clr, linewidth=1, edgecolor=".2")
    ax.spines[['top', 'left', 'right']].set_visible(False)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(labelleft=False, left=False, labelsize=14)
    ax.set_title(col, fontweight="bold")
    for i in ax.containers:
        ax.bar_label(i, fontsize=15)
plt.tight_layout()
plt.show()


# 增加一列判断东道主（主办国）是否进入半决赛（4强）
hist_worldcup['HostTop4'] = hist_worldcup[['Winner', 'Second', 'Third', 'Fourth']].eq(hist_worldcup['HostCountry'], axis=0).any(1)
# 增加一列判断东道主（主办国）是否进入决赛
hist_worldcup['HostTop2'] = hist_worldcup[['Winner', 'Second']].eq(hist_worldcup['HostCountry'], axis=0).any(1)
# 增加一列判断东道主（主办国）是否夺冠
hist_worldcup['HostWinner'] = hist_worldcup['HostCountry'] == hist_worldcup['Winner']
index = hist_worldcup['HostWinner'].value_counts().index.tolist()
value = hist_worldcup['HostWinner'].value_counts().values.tolist()

# 东道主进入半决赛（4强）概率
index = hist_worldcup['HostTop4'].value_counts().index.tolist()
values = hist_worldcup['HostTop4'].value_counts().values.tolist()
palette = ['#f0c9cf', '#ef475d']
fig12, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.countplot(ax=ax[0], x=hist_worldcup['HostTop4'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Host in TOP4?', size=20, weight='bold')
ax[0].spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)
plt.pie(values, labels=index, autopct='%.0f%%', colors=['#f0c9cf', '#ef475d'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Percentage', size=20, weight='bold')
plt.show()

# 东道主进入决赛概率
index = hist_worldcup['HostTop2'].value_counts().index.tolist()
values = hist_worldcup['HostTop2'].value_counts().values.tolist()
fig13, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.countplot(ax=ax[0], x=hist_worldcup['HostTop2'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Host in Top2?', size=20, weight='bold')
ax[0].spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)

plt.pie(values, labels=index, autopct='%.0f%%', colors=palette,
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Percentage', size=20, weight='bold')
plt.show()

# 东道主夺冠概率
index = hist_worldcup['HostWinner'].value_counts().index.tolist()
value = hist_worldcup['HostWinner'].value_counts().values.tolist()

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.countplot(ax=ax[0], x=hist_worldcup['HostWinner'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Number', size=20, weight='bold')
ax[0].spines[['right', 'top', 'left', 'bottom']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)
plt.pie(value, labels=index, autopct='%.0f%%', colors=palette,
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Probability', size=20, weight='bold')
plt.show()
