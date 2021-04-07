import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("实践")
r2=s2.getRootTopic()
r2.setTitle("实践")


content={
'ConcurrentHashMap':[
    {'put(K key, V value)':[
        '如key已存在，使用value覆盖原值并返回原值',
        '如不存在把value放入返回null'
    ]},
    {'putIfAbsent(K key, V value)':[
        '如key已存在直接返回原值,不使用value覆盖',
        '如key不存在放入value并返回null',
        '注意，判断key是否存在和放入是原子性操作'
    ]}
],
'ScheduledThreadPoolExecutor':[
    'Timer:多线程生产单线程消费,出异常直接清空队列',
    'ScheduledThreadPoolExecutor:可配置',
    '使用定时器功能时优先使用ScheduledThreadPoolExecutor'
],
'深浅引用':[
    '引用类型作为集合A元素',
    '如使用集合A作为集合B的构造函数参数',
    '两集合里同一个位置的元素指向的是同一个引用',
    '对引用的修改在两个集合中都可见，此时需对引用元素进行深复制'
],
'FutureTask':[
    '线程池中使用FutureTask，当拒绝策略为DiscardPolicy和DiscardOldestPolicy时',
    '被拒绝任务的FutureTask对象上调get()方法会导致调用线程一直阻塞',
    {'原因':[
        'Future有状态',
        'Future状态>COMPLETING，get()方法返回',
        'future初始值new,上述拒绝策略没有重置future的值'
    ]},
    '建议：尽量使用带超时参数的get方法',
],
'并发编程注意事项':[
    '创建线程和线程池时指定与业务相关的名称',
    '使用线程池后要调用shutdown方法关闭，否则会导致线程池线程资源一直不释放'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 