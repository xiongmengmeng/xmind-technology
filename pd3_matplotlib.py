import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

 
anscombe=sns.load_dataset("anscombe")
print(anscombe)

dataset_1=anscombe[anscombe['dataset']=='I']
dataset_2=anscombe[anscombe['dataset']=='II']
dataset_3=anscombe[anscombe['dataset']=='II']
dataset_4=anscombe[anscombe['dataset']=='IV']
# plt.plot(dataset_1['x'],dataset_1['y'])

# plt.plot(dataset_1['x'],dataset_1['y'],'o')

# #创建画布，用于放置子图
# fig=plt.figure()

# #子图有两行两列，位置是1
# axes1=fig.add_subplot(2,2,1)
# #子图有两行两列，位置是2
# axes2=fig.add_subplot(2,2,2)
# #子图有两行两列，位置是3
# axes3=fig.add_subplot(2,2,3)
# #子图有两行两列，位置是4
# axes4=fig.add_subplot(2,2,4)

# #在上面创建的各个轴域中绘制图
# axes1.plot(dataset_1['x'],dataset_1['y'],'o')
# axes2.plot(dataset_2['x'],dataset_2['y'],'o')
# axes3.plot(dataset_3['x'],dataset_3['y'],'o')
# axes4.plot(dataset_4['x'],dataset_4['y'],'o')

# #向各幅子图添加小标题
# axes1.set_title("dataset_1")
# axes2.set_title("dataset_2")
# axes3.set_title("dataset_3")
# axes4.set_title("dataset_4")

# #向各幅子图添加x,y轴标签
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')

# #为整幅图添加一个大标题
# fig.suptitle("Anscombe Data")

# #使用紧凑布局
# fig.tight_layout()
# fig.show()
# input()

#2.使用matplotlib绘制统计图
#2.1.直方图
# tips=sns.load_dataset("tips")
# print(tips.head())
# fig=plt.figure()
# histogram=fig.add_subplot(1,1,1)
# histogram.hist(tips['total_bill'],bins=10)
# histogram.set_title("Histogram of Total Bill")
# histogram.set_xlabel("Frequency")
# histogram.set_ylabel("Total Bill")
# fig.show()
# input()

# #2.2.散点图(双变量)
tips=sns.load_dataset("tips")
fig=plt.figure()
scatter_plot=fig.add_subplot(1,1,1)
scatter_plot.scatter(tips['total_bill'],tips['tip'])
scatter_plot.set_title("Scatterplot of Total Bill vs Tip")
scatter_plot.set_xlabel("Total Bill")
scatter_plot.set_ylabel("Tip")
fig.show()
input()

#2.3.散点图（多变量）
tips=sns.load_dataset("tips")
print(tips)

def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1

tips['sex_color']=tips['sex'].apply(recode_sex)

fig=plt.figure()
scatter_plot=fig.add_subplot(1,1,1)
scatter_plot.scatter(tips['total_bill'],
    tips['tip'],
    #根据聚餐人数设置点的大小，乘上10以放大不同
    s=tips['size']*10,
    #为sex设置颜色
    c=tips['sex_color'],
    #设置alpha值，增加点的透明度，以表现重叠的点
    alpha=0.5)
scatter_plot.set_title("Total Bill vs Tip Colored by Sex and Size by Size")
scatter_plot.set_xlabel("Total Bill")
scatter_plot.set_ylabel("Tip")
fig.show()
input()