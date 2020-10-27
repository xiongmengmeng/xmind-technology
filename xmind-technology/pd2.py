import pandas,random,openpyxl
#1.创建Series,表示DataFrame的每一列

s=pandas.Series(['apple',42])
print(s)


#2.创建DataFrame:Series对象组成的字典
students=pandas.DataFrame({'Name':['Anna','Tom'],'Age':[10,13],'score':[90,89]})
print(students)

students_info=pandas.DataFrame(
    data={'Age':[10,13,12,15,10],'score':[90,89,78,67,98],'Born':['2010/01/05','2007/12/13','2008/9/21','2005/4/16','2010/6/28']},
    index=['Anna','Tom','Marry','Herry','LILI'],
    columns=['score','Age','Born'])
print(students_info)

#3.Series

#3.1.Series的属性
stu=students_info.loc['Tom']
print(type(stu))
print(stu)
print('\n输出索引：')
print(stu.index)
print('\n输出值：')
print(stu.values)
print('\n输出index属性的别名：')
print(stu.keys())

print('\n使用属性获得第一个索引：')
print(stu.index[0])

print('\n使用方法获取第一个索：')
print(stu.keys()[0])

print('\n使用方法获取第一个索：')
print(stu.keys()[0])


#3.2.Series的方法
age=students_info['Age']
print('\n输出年龄：')
print(age)
print('\n输出基本统计量：')
print(age.describe())
print('\n最小的年龄：')
print(age.min())
print('\n最大的年龄：')
print(age.max())
print('\n平均的年龄：')
print(age.mean())
print('\n年龄的方差：')
print(age.std())

#3.2.Series的布尔子集
print('\n获取大于平均值的年龄：')
print(age[age>age.mean()])


print('\n年龄是否大于平均值：')
print(age>age.mean())


#4.DataFrame
#4.1.DataFrame的布尔子集
print('\n获取大于平均值的年龄的学生信息：')
print(students_info[students_info['Age']>students_info['Age'].mean()])


#5.更改
#5.1添加
print('\n将出生日期格式化：')
bornFormat=pandas.to_datetime(students_info['Born'],format='%Y-%m-%d')
print(bornFormat)
students_info['Born-Format']=bornFormat
print('\n添加一列：')
print(students_info)

#5.2更改列
random.seed(10)
random.shuffle(students_info['Age'])
print(students_info['Age'])

#5.3删除列
print('\n当前数据的所有列：')
print(students_info.columns)

students_dropped=students_info.drop(['Age'],axis=1)
print('\n删除Age列后，数据的所有列：')
print(students_dropped.columns)


#6.导入，导出
#6.1.pickle，数据以二进制形式存储
age.to_pickle("c:\\Users\\btr\\Desktop\\age.pickle")
students_info.to_pickle("c:\\Users\\btr\\Desktop\\students.pickle")


studens_from_pickle=pandas.read_pickle("c:\\Users\\btr\\Desktop\\students.pickle")
print('\n从pickle读取数据：')
print(studens_from_pickle)

#6.2csv
students_info.to_csv("c:\\Users\\btr\\Desktop\\students.csv")
studens_from_csv=pandas.read_csv("c:\\Users\\btr\\Desktop\\students.csv")
print('\n从csv读取数据：')
print(studens_from_csv)


#6.3.excel
students_info.to_excel("c:\\Users\\btr\\Desktop\\students.xlsx")
studens_from_xlsx=pandas.read_excel("c:\\Users\\btr\\Desktop\\students.xlsx")
print('\n从xlsx读取数据：')
print(studens_from_xlsx)