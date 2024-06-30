from sympy import *
from sympy.abc import x, y
import matplotlib.pyplot as plt
import numpy as np
import sys

# 求函数与x轴的交点


def cross_x_axis(a, b, c):
    eq = Eq(a*x**2 + b*x + c, 0)
    res = solve(eq)
    # res = res.xreplace({n: round(n, 3) for n in res.atoms(Number)})
    return res

# 求函数折点


def get_turning_point(a, b, c):
    x = (-1 * b) / (2 * a)
    y = ((4*a*c) - (b**2)) / (4*a)
    return (x, y)


# 输入常数项
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
# 二次项系数是否为零
if a == 0:
    print("二次项系数怎么能为零呢？")
    sys.exit(0)
# 获取折点
turning_point = get_turning_point(a, b, c)
# 用于储存横轴交点的列表，元素类型为数组
x_cross_points = []
# 纵轴交点（元组）
y_cross_point = ()
# 检测是否与横轴有两个交点
if (turning_point[1] > 0 and a < 0) or (turning_point[1] < 0 and a > 0):
    x_cross_points = [(round(float(cross_x_axis(a, b, c)[0]), 3), 0),
                      (round(float(cross_x_axis(a, b, c)[1]), 3), 0)]
    y_cross_point = (0, c)
# 如果只有一个交点（拐点y=0）
elif turning_point[1] == 0:
    x_cross_points = [turning_point]
    y_cross_point = (0, c)
# 没有交点
else:
    x_cross_points = [None]
    y_cross_point = (0, c)
print("===================")
print("折点：", turning_point)
print("x轴交点：", x_cross_points)
print("y轴交点：", y_cross_point)

# 画图用数据集
x_number = np.arange(-10, 10, 0.1)
y_number = a*x_number**2 + b*x_number + c

# 调整坐标轴
fig = plt.figure()
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# 移到原点
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


# 画图
plt.plot(x_number, y_number)
# 设置x，y轴范围
# 如果没有横轴交点则取拐点

x_left = int(turning_point[0]) - 10
x_right = int(turning_point[0]) + 10
plt.xlim(x_left, x_right)

if y_cross_point[1] >= turning_point[1]:
    y_up = int(y_cross_point[1]) + 10
    y_down = int(turning_point[1]) - 10
    plt.ylim(y_down, y_up)
else:
    y_down = int(y_cross_point[1]) - 10
    y_up = int(turning_point[1]) + 10
    plt.ylim(y_down, y_up)
# 标点
# 拐点
plt.scatter(turning_point[0], turning_point[1], s=25, c='r')
# 考虑函数方向
if a > 0:
    plt.text(turning_point[0], turning_point[1]-0.3, str(turning_point),
             ha='center', va='top', fontsize=10.5, c='r')
else:
    plt.text(turning_point[0], turning_point[1]+0.3, str(turning_point),
             ha='center', va='bottom', fontsize=10.5, c='r')


if x_cross_points != [None]:
    # 第一个交点
    plt.scatter(x_cross_points[0][0], x_cross_points[0][1], s=25, c='r')
    plt.text(x_cross_points[0][0]+0.15, x_cross_points[0][1]+0.3, str(x_cross_points[0]),
             ha='center', va='bottom', fontsize=10.5, c='b')
    # 第二个交点
    plt.scatter(x_cross_points[1][0], x_cross_points[1][1], s=25, c='r')
    plt.text(x_cross_points[1][0]+0.15, x_cross_points[1][1]+0.3, str(x_cross_points[1]),
             ha='center', va='bottom', fontsize=10.5, c='b')

# 纵轴交点
plt.scatter(y_cross_point[0], y_cross_point[1], s=25, c='r')
if y_cross_point[1] >= 0:
    plt.text(y_cross_point[0]+1, y_cross_point[1]+0.3, str(y_cross_point),
             ha='center', va='bottom', fontsize=10.5, c='b')
else:
    plt.text(y_cross_point[0]+1, y_cross_point[1]-0.3, str(y_cross_point),
             ha='center', va='top', fontsize=10.5, c='b')


plt.show()
