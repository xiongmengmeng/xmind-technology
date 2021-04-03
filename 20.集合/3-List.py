import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("List集合")
r2=s2.getRootTopic()
r2.setTitle("List集合")


content={
'数组和集合的比较':[
    '1.数组能存放基本数据类型和对象，而集合类存放的都是对象，集合类不能存放基本数据类型',
    '2.数组容易固定无法动态改变，集合类可动态改变',
    '3.数组无法判断其中实际存有多少元素，length只告诉了数组的容量，而集合的size()可以确切知道元素的个数',
    '4.集合有多种实现方式和不同适用场合，数组仅采用顺序表方式',
    '5.集合以类的形式存在，具有封装、继承、多态等类的特性，通过简单的方法和属性即可实现各种复杂操作'
],
'List集合':[
    '有序列表，允许存放重复的元素'
],
'ArrayList':[
    {'底层':[
        '数组'
    ]},
    '查询快，增删慢',
    '线程不安全',
    {'自动扩充机制':[
        '实现：ArrayList.ensureCapacity(int minCapacity)',
        '首先得到当前elementData,属性的长度oldCapacity',
        '如minCapacity>oldCapacity,对当前的List对象进行扩容',
        '扩容的的策略：取(oldCapacity * 3)/2 + 1和minCapacity之间更大的',
        '使用数组拷贝方法，把以前存放的数据转移到新的数组对象'
    ]}
],
'LinkedList':[
    {'底层':[
        '双向循环链表'
    ]},
    '增删快，查询慢,线程不安全',
    {'每个数据节点由三部分组成':[
        '前指针',
        '数据',
        '后指针:最后一个节点的后指针指向第一个节点，形成一个循环'
    ]},
    {'特有方法':[
        'addFirst()、addLast()',
        'getFirst()、getLast()',
        'removeFirst()、removeLast()'
    ]},
    '可实现栈(stack)、队列(queue)、双向队列(double-ended queue )'
],
'Vector':[
    {'底层':[
        '数组，重量级,线程安全'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 