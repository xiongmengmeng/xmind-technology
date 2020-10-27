import pandas 
import csv 

df=pandas.read_csv("c:/Users/btr/Desktop/screeSharesInfo.csv",sep='\t')
print(df.head())


print(type(df))

#获取行数和列数
print(df.shape)

#获取列名
print(df.columns)

#获取每列的dtype
print(df.dtypes)

#获取更多数据信息
print(df.info())
