# -*- coding: utf-8 -*-
import csv
import pandas as pd
from numpy import *
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils.np_utils import to_categorical
from random import sample

# 把tr_data_after.csv读入
df = pd.read_csv('ML_Predict/tr_data_after.csv', encoding="utf_8_sig")
home_team = df["home_team"]
away_team = df["away_team"]
home_times = df["home_times"]
away_times = df["away_times"]
home_win = df["home_win"]
away_win = df["away_win"]
home_goals = df["home_goals"]
away_goals = df["away_goals"]
home_r_win = df["home_r_win"]
away_r_win = df["away_r_win"]

home_Ave_goal = df["home_Ave_goal"]
away_Ave_goal = df["away_Ave_goal"]
result = df["result"]

team_merge = pd.concat(
    [home_team, away_team, home_times, away_times, home_win, away_win, home_goals, away_goals, home_r_win, away_r_win,
     home_Ave_goal, away_Ave_goal, result], axis=1).drop(['home_team', 'away_team'], axis=1)

play_score_temp = team_merge.iloc[:, :-1]
# 标准分数处理（除了主客队名称和结果集以外数据）
play_score_normal = (play_score_temp - play_score_temp.mean()) / (play_score_temp.std())
play_score_normal = pd.concat([play_score_normal, team_merge.iloc[:, -1]], axis=1)
# print(play_score_normal)

# 获取csv数据的长度（条数）
with open('ML_Predict/tr_data_after.csv', 'r') as f:
    line = len(f.readlines())

# 70%的数据作为训练集
tr_index = sample(range(0, line - 1), int(line * 0.7))
te_index = [i for i in range(0, line - 1) if i not in tr_index]

tr_x = play_score_normal.iloc[tr_index, :-1]  # 训练特征
tr_y = play_score_normal.iloc[tr_index, -1]  # 训练目标

te_x = play_score_normal.iloc[te_index, :-1]  # 测试特征
te_y = play_score_normal.iloc[te_index, -1]  # 测试目标

df2 = pd.read_csv('ML_Predict/data.csv')
country = df2["country"]
times = df2["times"]
win = df2["win"]
goals = df2["goals"]
rate = df2["rate of winning"]
Average = df2["Average goal"]
frames = [country, times, win, goals, rate, Average]
country_all = pd.concat(frames, axis=1).dropna(axis=0, how='any', inplace=False)

num_data = country_all.iloc[:, [1, 2, 3, 4, 5]]
# 测试集标准分数标准化
country_all_MM = (num_data - num_data.mean()) / (num_data.std())
country_all_MM = pd.concat([country, country_all_MM], axis=1)
# country_all_MM.to_csv("tr_data_z.csv",encoding="utf_8_sig")
play_score_normal.reset_index(drop=True)
play_score_normal.to_csv("ML_Predict/play_score_normal.csv")

model_k = Sequential()
model_k.add(Dense(100, input_dim=10, activation='relu'))
model_k.add(Dense(500, input_dim=100, activation='relu'))
model_k.add(Dense(100, input_dim=20, activation='relu'))
model_k.add(Dense(units=2, activation='softmax'))
# 为了保证数据一致性，将目标类转化为独热编码，同时我们想要计算交叉熵损失函数，Adam算法作为优化算法，然后把准确率当做衡量这个算法的指标
y = to_categorical(tr_y, 2)
model_k.compile(loss='categorical_crossentropy',
                optimizer='adam', metrics=['accuracy'])
# 以200个样本为一批进行迭代
model_k.fit(np.asarray(tr_x), y, epochs=200, batch_size=200)
result = model_k.evaluate(np.asarray(tr_x), y)
y_pred = model_k.predict(np.asarray(te_x))
print(result[1])

# 16强
group1 = pd.Series(['Netherlands', 'Argentina', 'Japan', 'Brazil', 'France', 'England', 'Morocco', 'Portugal'])
group2 = pd.Series(['USA', 'Australia', 'Croatia', 'Korea Republic', 'Poland', 'Senegal', 'Spain', 'Switzerland'])

csvFile = open('ML_Predict/16res.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(["times", "team1", "team2", "win"])
print("\n16 to 8")
for i in range(0, 8):
    print("组1：第", i + 1, "队")
    team1 = country_all_MM.loc[country_all['country'] == group1.iloc[i]]

    print(group1.iloc[i])
    print("组2：第", i + 1, "队")
    team2 = country_all_MM.loc[
        country_all['country'] == group2.iloc[i]]

    print(group2.iloc[i])
    vs = pd.concat([team1.reset_index(),
                    team2.reset_index()],
                   axis=1).drop(['index', 'country'], axis=1)

    result = model_k.predict(np.asarray(vs))
    result = result[0]
    print(result)
    if result[0] > result[1]:
        temp = group1.iloc[i]
    else:
        temp = group2.iloc[i]
    print("获胜方：", temp)
    writer.writerow([i, group1.iloc[i], group2.iloc[i], temp])
csvFile.close()
# 8强
df = pd.read_csv('ML_Predict/16res.csv')
win = df['win']
g1_index = [i for i in range(0, 8, 2)]
group1 = pd.Series(win[g1_index]).reset_index(drop=True)
g2_index = [j for j in range(1, 8, 2)]
group2 = pd.Series(win[g2_index]).reset_index(drop=True)

csvFile = open('ML_Predict/8res.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(["times", "team1", "team2", "win"])
print("\n8进4")
for i in range(0, 4):
    print("组1：第", i + 1, "队")
    team1 = country_all_MM.loc[country_all['country'] == group1.iloc[i]]
    print(group1.iloc[i])
    print("组2：第", i + 1, "队")
    team2 = country_all_MM.loc[country_all['country'] == group2.iloc[i]]
    print(group2.iloc[i])
    print("比赛结果")
    vs = pd.concat([team1.reset_index(), team2.reset_index()], axis=1).drop(['index', 'country'], axis=1)
    result = model_k.predict(np.asarray(vs))
    result = result[0]
    print(result)
    if result[0] > result[1]:
        temp = group1.iloc[i]
    else:
        temp = group2.iloc[i]
    print("获胜方：", temp)
    writer.writerow([i, group1.iloc[i], group2.iloc[i], temp])
csvFile.close()

# 4强
df = pd.read_csv('ML_Predict/8res.csv')
win = df['win']

g1_index = [i for i in range(0, 4, 2)]
group1 = pd.Series(win[g1_index]).reset_index(drop=True)
g2_index = [j for j in range(1, 4, 2)]
group2 = pd.Series(win[g2_index]).reset_index(drop=True)

csvFile = open('ML_Predict/4res.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(["times", "team1", "team2", "win"])
print("\n4进2")
for i in range(0, 2):
    print("组1：第", i + 1, "队")
    team1 = country_all_MM.loc[country_all['country'] == group1.iloc[i]]
    print(group1.iloc[i])
    print("组2：第", i + 1, "队")
    team2 = country_all_MM.loc[country_all['country'] == group2.iloc[i]]
    print(group2.iloc[i])
    print("比赛结果")
    vs = pd.concat([team1.reset_index(), team2.reset_index()], axis=1).drop(['index', 'country'], axis=1)
    result = model_k.predict(np.asarray(vs))
    result = result[0]
    print(result)
    if result[0] > result[1]:
        temp = group1.iloc[i]
    else:
        temp = group2.iloc[i]
    print("获胜方：", temp)
    writer.writerow([i, group1.iloc[i], group2.iloc[i], temp])
csvFile.close()

# 决赛
df = pd.read_csv('ML_Predict/4res.csv')
win = df['win']

g1_index = [i for i in range(0, 1)]
group1 = pd.Series(win[g1_index]).reset_index(drop=True)
g2_index = [j for j in range(1, 2)]
group2 = pd.Series(win[g2_index]).reset_index(drop=True)

csvFile = open('ML_Predict/2res.csv', 'w', newline='', encoding="utf_8_sig")
writer = csv.writer(csvFile)
writer.writerow(["times", "team1", "team2", "win"])
print("\n决赛")
for i in range(0, 1):
    print("组1：第", i + 1, "队")
    team1 = country_all_MM.loc[country_all['country'] == group1.iloc[i]]
    print(group1.iloc[i])
    print("组2：第", i + 1, "队")
    team2 = country_all_MM.loc[country_all['country'] == group2.iloc[i]]
    print(group2.iloc[i])
    print("比赛结果")
    vs = pd.concat([team1.reset_index(), team2.reset_index()], axis=1).drop(['index', 'country'], axis=1)
    result = model_k.predict(np.asarray(vs))
    result = result[0]
    print(result)
    if result[0] > result[1]:
        temp = group1.iloc[i]
    else:
        temp = group2.iloc[i]
    print("获胜方：", temp)
    writer.writerow([i, group1.iloc[i], group2.iloc[i], temp])
csvFile.close()
