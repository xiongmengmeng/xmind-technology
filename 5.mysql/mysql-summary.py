import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("summary")
r2=s2.getRootTopic()
r2.setTitle("summary")


content={
'drop、delete、truncate的区别':[
    'drop删表,truncate和delete只删除数据',
    'delete删数据，删除操作作为事务记录在日志中，可进行回滚',
    'truncate一次性删除表中所有的数据,无操作记录日志，不能恢复'
],
'用自增列作为主键':[
    '防止页断裂造成的空洞'
],
'使用索引能提高效率':[
    '索引是B+树结构，数据是有序的'
],
'MVCC最大的好处':[
    '读不加锁，读写不冲突'
],
'MySQL的binlog有几种录入格式':[
    'statement:记录单元为语句',
    'row:记录单元为每一行的改动',
    'mix:普通操作使用statement记录,当无法使用statement的时候使用row'
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 