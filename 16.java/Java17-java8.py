import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("java8")
r2=s2.getRootTopic()
r2.setTitle("java8")


content={
'Collector(四部分组成)':[
    {'Supplier<A> supplier()':[
        '创建新的结果'
    ]},
    {'BiConsumer<A, T> accumulator()':[
        '将元素添加到结果容器'
    ]},
    {'BinaryOperator<A> combiner()':[
        '将两个结果容器合并为一个结果容器'
    ]},
    {'Function<A, R> finisher()':[
        '对结果容器作相应的变换'
    ]},
    'https://blog.csdn.net/io_field/article/details/54971555',
    '写了一个自定义的Collector来理解一个它的原理',
],
'ForkJoinPool':[
    'https://blog.csdn.net/niyuelin1990/article/details/78658251'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 