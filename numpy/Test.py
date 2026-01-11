import numpy as np
import matplotlib.pyplot as plt  # 导入matplotlib

# 准备x轴和y轴数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(2,figsize=(10,5))


ax[0].set_title('sin(x)')
ax[0].set_xlim(0, 10)  # 设置x轴的范围
ax[0].set_ylim(-1, 1)  # 设置y轴的范围
ax[0].set_xlabel("x")  # 设置x轴的标签
ax[0].set_ylabel("sin(x)")  # 设置y轴的标签
ax[0].set_title("sin")  # 设置子图的标题
ax[0].plot(x, y1)  # 绘制曲线

plt.show()