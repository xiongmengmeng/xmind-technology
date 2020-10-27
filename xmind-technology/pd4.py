import pandas

import seaborn as sns
import matplotlib.pyplot as plt

#使用seaborn画图

tips=sns.load_dataset("tips")
print(tips)

# #1.1直方图+密度图（kde)+频数图：displot
# #使用subplots创建画布
# # hist,ax=plt.subplots()
# #使用seaborn 的displot 绘图
# ax=sns.displot(tips['total_bill'], kde = True, rug = True)
# ax.set_titles('Total Bill Histogram with Density Plot')
# ax.set_xlabels('Total Bill')
# ax.set_ylabels('Frequency')
# plt.show()

# #1.2计数图（条形图）：displot
# ax=sns.displot(tips['day'])
# ax.set_titles('Count of day')
# ax.set_xlabels('Day of the Week')
# ax.set_ylabels('Frequency')
# plt.show()

# #1.3. 散点图(拟合回归线)：regplot
# sc=sns.regplot(x=tips['total_bill'],y=tips['tip'])
# plt.show()

#1.4. 蜂巢图：jointplot
hexbin=sns.jointplot(x=tips['total_bill'],y=tips['tip'])
hexbin.set_axis_labels(xlabel='Total Bill',ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip',fontsize=10,y=1.03)
plt.show()
