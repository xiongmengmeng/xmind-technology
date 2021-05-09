import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HashMap")
r2=s2.getRootTopic()
r2.setTitle("HashMap")


content={
'HashMap()':[
    '构造一个初始容量为16，加载因子为0.75的容器'
],
'思考':[
    {'1.容量有何作用，加载有何作用':[
        ''
    ]},
    {'2.什么时候创建':[
        ''
    ]},
    'jdk1.7,HashMap底层基于数组+链表',
    {'3.数组作用是什么，链表作用是什么':[
        ''
    ]},
    {'4.什么时候创建数组，什么时候形成链表':[
        '数组：不是在创建map对象时创建,而是在put数据时',
        '链表：hash冲突的时候产生'
    ]},
    {'5.为何在put时创建数组':[
        '1.数组在内存里面是一段连续的内存空间',
        '2.防止在第一次putAll时就扩容',
        
    ]},
    {'6.怎么确认键值对在数组中的位置':[
        '通过key的hash值与数组最大索引进行位运算，确定在数组中的位置',
        '索引i=(数组长度n-1)&hash'
    ]},
],
'变量':[
    {'int DEFAULT_INITIAL_CAPACITY = 1 << 4':[
        '初始默认容量16'
    ]},
    {'int MAXIMUM_CAPACITY = 1 << 30':[
        '数据最大容量'
    ]},
    {'float DEFAULT_LOAD_FACTOR = 0.75f':[
        '默认加载因子0.75'
    ]},
    {'int TREEIFY_THRESHOLD = 8':[
        '判断链表是否要转换为红黑树'
    ]},
    {'int UNTREEIFY_THRESHOLD = 6':[
        '判断红黑树是否要转换为链表'
    ]},
    {'int MIN_TREEIFY_CAPACITY = 64':[
        '判断链表转换为红黑树，还是进行数组扩容'
    ]}
],
'hashmap存储过程':[
    '1.根据key计算一个hash值',
    '2.put时判断数组是否存在，不存在:调用resize方法创建默认容量为16,加载因子为0.75的数组',
    '3.确定node在数组中的位置：根据【hash值】与【数组最大索引值】进行【与运算】得到【索引位置】',
    '4.判断该位置是否有元素，没有元素：直接新建一个Node放在该位置',
    '5.如有元素，判断key是否相同，相同：把原来的node赋值给一个变量',
    '6.key不同：判断该位置是红黑树还是链表',
    '7.是红黑树：以红黑树方式将node放在红黑树上',
    '8.是链表：遍历链表，将node放在最后一位',
    {'放完后判断链表长度是否超过8':[
        {'超过':[
            {'判断数组容量<64':[
                '是，只进行数组扩容',
                '否，进行链表转换'
            ]}
        ]},
        {'不超过':[
            '返回'
        ]}
    ]},
    '9.返回被覆盖的值',
    '10.判断新插入这个值是否导致size已经超过了阈值，是：进行扩容'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 