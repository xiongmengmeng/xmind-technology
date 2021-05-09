import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("常见面试题")
r2=s2.getRootTopic()
r2.setTitle("常见面试题")


content={

'1.hashmap在jdk1.7与1.8两个版本中有什么区别':[
    '1.7:数组+链表',
    '1.8:数组+链表+红黑树'
],
'2.工作原理':[],
'3.如何确认键值对位置？如何解决hash冲突':[
    'key的【hash值】与【数组最大索引值】进行【与运算】得到【索引位置】',
    '链表或红黑树'
],
'4.存储过程中什么时候进行数组扩容':[
    '数据量超过数组大小的0.75时',
    '有链表存放数据>=8个节点&&数组<64时'
],
'5.扩容为什么每次都是2的次幂':[
    'key的hash值与n-1进行【异或】运算时，数组长度2的次幂，计算出的索引值更分散',
    '数组容量16 最大索引15 01111',
    'n-1  01111  01111  01111  01111',
    'hash 01000  00111  01010  01011',
    '索引 01000  00111  01010  01011'
],
'6.底层为什么要使用异或运算符':[
    '位运算符，快',
    '使数据更分散 '
],
'7.加载因子为什么是0.75，如果调整为1':[
    '平衡【使用空间】和【hash冲突】',
    '0.5:hash冲突可能性小了，但空间使用率下降',
    '1:空间使用率高，但hash冲突可能性也变高了'
],
'8.线程安全发生在哪个阶段':[
    'put值的时候'
],
'9.HashMap与ConcurrentHashMap有什么区别':[
    'HashMap:非线程安全的',
    'ConcurrentHashMap:线程安全的'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 