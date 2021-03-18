import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConcurrentHashMap")
r2=s2.getRootTopic()
r2.setTitle("ConcurrentHashMap")


content={
'HashMap1.7':[
    '数组+单向链表',
    {'Entry':[
        'key',
        'value',
        'hash 值',
        '用于单向链表的 next'
    ]},
    {'属性':[
        'capacity：当前数组容量，始终保持 2^n，可以扩容，扩容后数组大小为当前的 2 倍',
        'loadFactor：负载因子，默认为 0.75',
        'threshold：扩容的阈值，等于 capacity * loadFactor',
    ]},
    {'put':[
        '1.插入第一个元素时，需先初始化数组大小',
        '2.根据key计算hash值,对数组长度进行取模,得到对应的数组下标',
        '3.遍历对应下标处的链表，看是否有重复key存在，如有，直接覆盖，put方法返回旧值',
        '4.不存在重复key，将entry添加到链表中（先判断是否满足扩容条件，满足先扩容再插入数据）',
        {'数组扩容':[
            '触发条件：当前size>=阈值threshold，且要插入的数组位置上已有元素',
            '操作：建一个新的大数组（小数组的2倍）替换原来的小数组，将原来数组中的值迁移到新的数组中',
            '原来table[i] 中的链表的所有节点，分拆到新的数组的newTable[i]和 newTable[i + oldLength]位置上',
            '如原来数组长16，扩容后，原table[0]处链表中的所有元素会被分配到新数组中newTable[0]和newTable[16]两个位置'
        ]}
    ]},
    {'get':[
        '根据key计算hash值',
        '对数组长度进行取模,找到相应的数组下标：hash & (length - 1)',
        '遍历该数组位置处的链表，直到找到相等(==或equals)的 key'
    ]}
],
'ConcurrentHashMap1.7':[
    '一个Segment数组',
    '锁的粒度一个Segment（继承ReentrantLock）'
]
'原理解析':[
    '使用技术：CAS + synchronized，来保证并发更新的安全',
    '数据结构：数组+链表+红黑树'
    {'':[
        '',
        ''
    ]},
    '',
    '',
    '',
    ''
],
1. 原理解析
1.1. 重要成员变量
1.2. 实例初始化
1.3. put操作
1.3.1 put过程描述
1.3.2 hash算法
1.3.3 定位索引
1.3.4 获取table对应的索引元素f
1.4. table 扩容
1.4.1 addCount
1.4.2 treeify
1.4.3 transfer
1.5. get操作
1.6. 统计size
1.7 删除元素
1.7.1 清空map：clear
1.7.2 删除元素
2. ConcurrentHashMap 在1.7与1.8中的不同
3. ConcurrentHashMap与HashMap的区别
4. ConcurrentHashMap能完全替代HashTable吗？
5. 实战
6. 红黑树的加锁机制（待更新）
Reference
————————————————
版权声明：本文为CSDN博主「猪杂汤饭」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/programmer_at/article/details/79715177
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 