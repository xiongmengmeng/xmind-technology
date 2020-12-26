# import pandas

# import seaborn as sns
# import matplotlib.pyplot as plt

# #使用Pandas画图

# tips=sns.load_dataset("tips")
# print(tips)


# import time
# def compare_time(time1,time2):
#     s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
#     e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
#     return int(s_time) - int(e_time)

# compare_time('1978-10-21','2017-12-12')>0

# # aa=time.strptime('1968-10-21','%Y')
# # print(aa)

# bb='1968-10-21'.split("-")[0]
# print(bb)




# 读入一个数据集, 我使用了美国警方击毙数据集.
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#matplotlib.use('Agg')
plt.style.use('ggplot')
path = 'https://raw.githubusercontent.com/HoijanLai/dataset/master/PoliceKillingsUS.csv'
data = pd.read_csv(path, encoding ='latin1')
data.sample(3)
aa=data.groupby('race')['age'].mean()
print(aa)
bb=data.groupby('race')['signs_of_mental_illness'].value_counts().unstack()
print(bb)
cc=data.groupby('flee')['age']
print(cc)
data.groupby('flee')['age'].plot(kind='kde', legend=True, figsize=(20, 5))
plt.show()
#input()