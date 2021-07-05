import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("图的结构")
r2=s2.getRootTopic()
r2.setTitle("图的结构")


content={
'并查集':[
    '1.每个节点都有一条往上指的指针',
    '2.节点a往上找到的头节点，叫做a所在集合的代表节点',
    '3.查询x和y是否属于同一个集合,就是看看找到的代表节点是不是一个',
    '4.把x,y各自所在集合的所有点合并成一个集合,',
    '只需要小集合的代表点挂在大集合的代表点的下方即可',
    {'详细':[
        '1.有若干样本a,b,c,d...类型假设是V',
        '2.在并查集中一开始认为每个样本都在单独的集合里',
        '3.用户可在任何时候调用如下两个方法：',
        'boolean isSameSet(V x,V y):查询样本x和样本y是否属于一个集合',
        'void union(V x,V y):把x和y各自所在集合的所有样本合并成一个集合',
        '4.isSameSet和union方法的代价越低越好',
    ]}
],
'并查集优化':[
    '1.节点往上找代表点的过程，把沿途的链变成扁平的',
    '2.小集合挂在大集合的下面',
    '3.如果方法调用很频繁,单次调用的代价为O(1),两个方法都如此',
],
'并查集的应用':[
    '解决两大块区域的合并问题',
    '常用在图等领域'
],
'图':[
    '1.由点的集合和边的集合构成',
    '2.虽然存在有向图和无向图的概念，但实际上都可以用有向图来表达',
    '3.边上可能带有权值',
],
'图结构的表达':[
    '1.邻接表法',
    '2.邻接矩阵法',
    '3.除此之外还有其他众多方式',
],
'图的面试题':[
    '图的算法都不算难，只不过coding的代价比较高',
    '1.先用自己最熟悉的方式，实现图结构的表达',
    '2.在自己熟悉的结构上，实现所有常用的图算法作为模版',
    '3.把面试题提供的图结构转化为自己熟悉的图结构，再调用模板或改写即可'
]
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 