import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("算法")
r2=s2.getRootTopic()
r2.setTitle("算法")


content={
'基础':[
    '时间复杂度',
    '递归',
    '异或运算',
    ''
],
'数据结构':[
    '数组',
    '链表',
    '栈',
    '队列',
    '哈希表和有序表',
    '堆'
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 