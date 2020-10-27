

import pandas 
import csv 

#1.加载数据集
df=pandas.read_excel("c:\\Users\\btr\\Desktop\\screeSharesInfo1.xlsx")
# print("\n查看数据的前5行：",end='')
# print(df.head())

# print("\ndf的类型：",end='')
# print(type(df))

# #获取行数和列数
# print("\n行数和列数：",end='')
# print(df.shape)

# #获取列名
# print("\n列名：",end='')
# print(df.columns)

# #获取每列的dtype
# print("\n每列的dtype：")
# print(df.dtypes)

# #获取更多数据信息
# print("\n更多数据信息：")
# print(df.info())

# #2.查看列，行，单元格


# pe=df['市盈率']
# print("\n查看市盈率列的前5行：")
# print(pe.head())

# print("\n查看市盈率列的后5行：")
# print(pe.tail())


# subset=df[['股票名称','市盈率']]

# print("\n查看股票名称，市盈率列的前5行：")
# print(subset.head())

# #2.1通过索引标签获取行子集：loc
# print("\n获取第1行：")
# print(df.loc[0])

# print("\n获取第100行：")
# print(df.loc[99])

# print("\n获取最后1行(loc)：")
# print(df.loc[df.shape[0]-1])

# print("\n获取多行(loc)：")
# print(df.loc[[0,2,5]])

# print("\n获取最后1行(tail)：")
# print(df.tail(n=1))

# print("使用loc获取一行，返回类型")
# print(type(df.loc[0]))

# print("使用head函数获取一行，返回类型")
# print(type(df.head(n=1)))

# #2.2通过行号获取行：iloc(索引标签不限于行号)

# print("\n获取第2行(iloc)：")
# print(df.iloc[1])

# print("\n获取最后1行(iloc)：")
# print(df.iloc[-1])


# print("\n获取多行(iloc)：")
# print(df.iloc[[0,2,5]])

# #2.3混合

# print("\n获取第2列(loc)：")
# print(df.loc[:,'股票名称'])

# print("\n获取第2,5,7列的第3，6，7行(iloc)：")
# print(df.iloc[[2,5,6],[1,4,6]])

# print("\n获取第2~7列的第1行(使用range函数)：")
# print(df.iloc[0,list(range(2,8))])

# print("\n获取第2~7列的第1行(使用切片)：")
# print(df.iloc[0,2:8])


#3.分组和聚合

print("\n每个行业的平均市盈率：")
print(df.groupby('行业一级')['市盈率'].mean())


print("\n分组：")
print(type(df.groupby('行业一级')))

print("\n分组->感兴趣的列：")
print(type(df.groupby('行业一级')['市盈率']))

industry_statistics=df.groupby('行业一级')['市盈率'].mean()
print(type(df.groupby('行业一级')['市盈率'].mean()))
aa=pandas.DataFrame(industry_statistics)
print(aa)
input()
