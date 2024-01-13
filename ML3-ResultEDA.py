import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.pyplot import MultipleLocator
from matplotlib import ticker
from matplotlib import cm
from matplotlib.patches import Wedge, Polygon

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=100, facecolor='#AD1457', edgecolor=None)
ax.set_facecolor('#AD1457')
ax.set_xlim(-12, 12)
ax.set_ylim(-7, 7)
y_min, y_max = ax.get_ylim()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.xaxis.set_major_locator(MultipleLocator(1))
fc_t = '#AD1457'
fc_t1 = 'white'
x1 = 11.9
y1 = 6.95
polygon1 = Polygon([[-x1, -y1], [-x1, y1], [x1, y1], [x1, -y1]], ec=fc_t1, fc=fc_t, closed=True, alpha=0.1)
ax.add_artist(polygon1)

# 左侧、右侧大框
x1, x2 = 10.5, 7.7
y1, y2 = 6.5, 4.4
for i in range(4):
    polygon1 = Polygon([[-x1, -y1], [-x1, -y2], [-x2, -y2], [-x2, -y1]], fc=fc_t, ec=fc_t1, closed=True)
    ax.add_artist(polygon1)
    polygon1 = Polygon([[x1, -y1], [x1, -y2], [x2, -y2], [x2, -y1]], fc=fc_t, ec=fc_t1, closed=True)
    ax.add_artist(polygon1)
    y1 -= 3
    y2 -= 3

ax.text(-9, -4.4, 'Group G', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(9, -4.4, 'Group H', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(-9, -1.4, 'Group E', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(9, -1.4, 'Group F', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(-9, 1.6, 'Group C', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(9, 1.6, 'Group D', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(-9, 4.6, 'Group A', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')
ax.text(9, 4.6, 'Group B', ha='center', va='bottom', fontsize=14, color=fc_t1, fontweight='heavy')

# 内部小框1
x1, x2 = 10, 8
y1, y2 = 6.4, 6
for i in range(4):
    polygon1 = Polygon([[-x1, -y1], [-x1, -y2], [-x2, -y2], [-x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    polygon1 = Polygon([[x1, -y1], [x1, -y2], [x2, -y2], [x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    y1 -= 0.5
    y2 -= 0.5

# 内部小框2
y1, y2 = 3.4, 3
for i in range(4):
    polygon1 = Polygon([[-x1, -y1], [-x1, -y2], [-x2, -y2], [-x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    polygon1 = Polygon([[x1, -y1], [x1, -y2], [x2, -y2], [x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    y1 -= 0.5
    y2 -= 0.5

# 内部小框3
y1, y2 = 0.4, 0
for i in range(4):
    polygon1 = Polygon([[-x1, -y1], [-x1, -y2], [-x2, -y2], [-x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    polygon1 = Polygon([[x1, -y1], [x1, -y2], [x2, -y2], [x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    y1 -= 0.5
    y2 -= 0.5

# 内部小框4
y1, y2 = -2.6, -3
for i in range(4):
    polygon1 = Polygon([[-x1, -y1], [-x1, -y2], [-x2, -y2], [-x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    polygon1 = Polygon([[x1, -y1], [x1, -y2], [x2, -y2], [x2, -y1]], fc=fc_t1, closed=True)
    ax.add_artist(polygon1)
    y1 -= 0.5
    y2 -= 0.5

# 一级、二级横线
ax.plot([-7, -5.5], [-6] * 2, color=fc_t1)
ax.plot([-7, -5.5], [-5] * 2, color=fc_t1)
ax.plot([-5.5, -4], [-5.5] * 2, color=fc_t1)
ax.plot([7, 5.5], [-6] * 2, color=fc_t1)
ax.plot([7, 5.5], [-5] * 2, color=fc_t1)
ax.plot([5.5, 4], [-5.5] * 2, color=fc_t1)

ax.plot([-7, -5.5], [-2] * 2, color=fc_t1)
ax.plot([-7, -5.5], [-3] * 2, color=fc_t1)
ax.plot([-5.5, -4], [-2.5] * 2, color=fc_t1)
ax.plot([7, 5.5], [-2] * 2, color=fc_t1)
ax.plot([7, 5.5], [-3] * 2, color=fc_t1)
ax.plot([5.5, 4], [-2.5] * 2, color=fc_t1)
ax.plot([-7, -5.5], [0] * 2, color=fc_t1)
ax.plot([-7, -5.5], [1] * 2, color=fc_t1)
ax.plot([-5.5, -4], [0.5] * 2, color=fc_t1)
ax.plot([7, 5.5], [0] * 2, color=fc_t1)
ax.plot([7, 5.5], [1] * 2, color=fc_t1)
ax.plot([5.5, 4], [0.5] * 2, color=fc_t1)
ax.plot([-7, -5.5], [3] * 2, color=fc_t1)
ax.plot([-7, -5.5], [4] * 2, color=fc_t1)
ax.plot([-5.5, -4], [3.5] * 2, color=fc_t1)
ax.plot([7, 5.5], [3] * 2, color=fc_t1)
ax.plot([7, 5.5], [4] * 2, color=fc_t1)
ax.plot([5.5, 4], [3.5] * 2, color=fc_t1)

ax.scatter([-7] * 8, [-6, -5, -3, -2, 0, 1, 3, 4], s=200, color=fc_t1, marker='o')
ax.scatter([6.98] * 8, [-6, -5, -3, -2, 0, 1, 3, 4], s=200, color=fc_t1, marker='o')
ax.scatter([-7] * 8, [-6, -5, -3, -2, 0, 1, 3, 4], s=200, color=fc_t1, marker='o')
ax.scatter([6.98] * 8, [-6, -5, -3, -2, 0, 1, 3, 4], s=200, color=fc_t1, marker='o')
ax.text(-7, -6.2, 'H2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, -6.2, 'G2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, -5.2, 'G1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, -5.2, 'H1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, -3.2, 'F2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, -3.2, 'E2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, -2.2, 'E1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, -2.2, 'F1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, -0.2, 'D2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, -0.2, 'C2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, 0.8, 'C1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, 0.8, 'D1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, 2.8, 'B2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, 2.8, 'A2', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(-7, 3.8, 'A1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')
ax.text(7, 3.8, 'B1', ha='center', va='bottom', fontsize=10, color=fc_t, fontweight='heavy')

# 一级竖线
ax.plot([5.5] * 2, [-6, -5], color=fc_t1)
ax.plot([-5.5] * 2, [-6, -5], color=fc_t1)
ax.plot([5.5] * 2, [-3, -2], color=fc_t1)
ax.plot([-5.5] * 2, [-3, -2], color=fc_t1)
ax.plot([5.5] * 2, [0, 1], color=fc_t1)
ax.plot([-5.5] * 2, [0, 1], color=fc_t1)
ax.plot([5.5] * 2, [3, 4], color=fc_t1)
ax.plot([-5.5] * 2, [3, 4], color=fc_t1)

# 二级竖线
ax.plot([4] * 2, [-5.5, -2.5], color=fc_t1)
ax.plot([-4] * 2, [-5.5, -2.5], color=fc_t1)
ax.plot([4] * 2, [0.5, 3.5], color=fc_t1)
ax.plot([-4] * 2, [0.5, 3.5], color=fc_t1)

# 三级横线
ax.plot([-4, -2.5], [-4] * 2, color=fc_t1)
ax.plot([4, 2.5], [-4] * 2, color=fc_t1)
ax.plot([-4, -2.5], [2] * 2, color=fc_t1)
ax.plot([4, 2.5], [2] * 2, color=fc_t1)
# 三级竖线
ax.plot([2.5] * 2, [-4, 2], color=fc_t1)
ax.plot([-2.5] * 2, [-4, 2], color=fc_t1)
# 四级横线
ax.plot([-2.5, -1], [-1] * 2, color=fc_t1)
ax.plot([1, 2.5], [-1] * 2, color=fc_t1)

# 三十二强
countries = ['喀麦隆', '韩国', '瑞士', '乌拉圭', '塞尔维亚', '加纳', '巴西', '葡萄牙']
x1, y1 = 9.6, 6.4
x2, y2 = 10, 6.2
for i in range(0, 8, 2):
    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [-x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(-x1, -y1, f'{countries[i]}', ha='left', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')

    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i + 1]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(x1, -y1, f'{countries[i + 1]}', ha='right', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')
    y1 -= 0.5
    y2 -= 0.5

countries = ['日本', '克罗地亚', '德国', '摩洛哥', '哥斯达黎加', '加拿大', '西班牙', '比利时']
x1, y1 = 9.6, 3.4
x2, y2 = 10, 3.2
for i in range(0, 8, 2):
    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [-x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(-x1, -y1, f'{countries[i]}', ha='left', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')

    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i + 1]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(x1, -y1, f'{countries[i + 1]}', ha='right', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')
    y1 -= 0.5
    y2 -= 0.5

countries = ['波兰', '突尼斯', '墨西哥', '丹麦', '沙特', '澳大利亚', '阿根廷', '法国']
x1, y1 = 9.6, 0.4
x2, y2 = 10, 0.2
for i in range(0, 8, 2):
    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [-x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(-x1, -y1, f'{countries[i]}', ha='left', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')

    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i + 1]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(x1, -y1, f'{countries[i + 1]}', ha='right', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')
    y1 -= 0.5
    y2 -= 0.5

countries = ['荷兰', '威尔士', '塞内加尔', '美国', '厄瓜多尔', '伊朗', '卡塔尔', '英格兰']
x1, y1 = 9.6, -2.6
x2, y2 = 10, -2.8
for i in range(0, 8, 2):
    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [-x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(-x1, -y1, f'{countries[i]}', ha='left', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')

    # arr_img = mpimg.imread(f'/home/mw/input/202211273063/pic/pic/{countries[i + 1]}.png')
    # imagebox = OffsetImage(arr_img, zoom=0.2)
    # ab = AnnotationBbox(imagebox, [x2, -y2], pad=0.02, frameon=False)
    # ax.add_artist(ab)
    ax.text(x1, -y1, f'{countries[i + 1]}', ha='right', va='bottom', fontsize=11, color=fc_t, fontweight='heavy')
    y1 -= 0.5
    y2 -= 0.5

# 十六强
zoom_t1 = 0.15
countries = ['Brazil', 'Korea Republic', 'Portugal', 'Switzerland']
x1 = 6.25
y1, y2 = 5, 6
for i in range(0, 4, 2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 1]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y2], pad=0.02, frameon=False)
    ax.add_artist(ab)
    x1 = -x1

countries = ['Japan', 'Croatia', 'Morocco', 'Spain']
x1 = 6.25
y1, y2 = 2, 3
for i in range(0, 4, 2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 1]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y2], pad=0.02, frameon=False)
    ax.add_artist(ab)
    x1 = -x1

countries = ['Argentina', 'Australia', 'France', 'Poland']
x1 = 6.25
y1, y2 = -1, 0
for i in range(0, 4, 2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 1]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y2], pad=0.02, frameon=False)
    ax.add_artist(ab)
    x1 = -x1

countries = ['Netherlands', 'USA', 'England', 'Senegal']
x1 = 6.25
y1, y2 = -4, -3
for i in range(0, 4, 2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 1]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y2], pad=0.02, frameon=False)
    ax.add_artist(ab)
    x1 = -x1

# 八强
zoom_t1 = 0.2
countries = pd.read_csv("ML_Predict/16res.csv")
countries = countries['win']
x1 = 4.75
y1 = 3.5
for i in range(0, 4):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 4]}.png')
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [x1, y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    y1 -= 3

# 四强
zoom_t1 = 0.25
countries = pd.read_csv("ML_Predict/8res.csv")
countries = countries['win']
x1 = 3.25
y1 = 2
for i in range(0, 2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    arr_img = mpimg.imread(f'logo/{countries[i + 2]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [x1, y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    y1 -= 6

# 决赛
zoom_t1 = 0.3
countries = pd.read_csv("ML_Predict/4res.csv")
countries = countries['win']
x1 = 1.25
y1 = 1
for i in range(2):
    arr_img = mpimg.imread(f'logo/{countries[i]}.png')
    # arr_img = arr_img.resize((50, 50))
    imagebox = OffsetImage(arr_img, zoom=zoom_t1)
    ab = AnnotationBbox(imagebox, [-x1, -y1], pad=0.02, frameon=False)
    ax.add_artist(ab)
    x1 = -x1

arr_img = mpimg.imread('logo/大力神杯.png')
imagebox = OffsetImage(arr_img, zoom=0.2)
ab = AnnotationBbox(imagebox, [0, -0.8], pad=0.02, frameon=False)
ax.add_artist(ab)

for i in ['top', 'right', 'left', 'bottom']:
    ax.spines[i].set_visible(False)

ax.text(-5.9, 6, '2022年卡塔尔世界杯决赛圈预测', fontdict={'color': fc_t1, 'size': 28}, fontweight='heavy')
y1 = 4.9
ax.plot([-7, -1.5], [y1] * 2, color=fc_t1)
ax.plot([7, 1.5], [y1] * 2, color=fc_t1)
ax.scatter(0, y1, s=100, color=fc_t1, marker='D')
ax.scatter(-0.7, y1, s=100, color=fc_t1, marker='D')
ax.scatter(0.7, y1, s=100, color=fc_t1, marker='D')

img = plt.imread('logo/世界杯.jpg')
ax.imshow(img, extent=[-10, 10, -6, 4], alpha=0.2)
plt.show()
