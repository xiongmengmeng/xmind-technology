import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka高并发")
r2=s2.getRootTopic()
r2.setTitle("kafka高并发")


content={
'数据接收时':[
    'Kafka每次接收到数据都会将数据写到磁盘',
    {'为了保证数据写入性能':[
        {'页缓存':[
            'page cache/os cache',
            '操作系统本身有的一层缓存(是在内存里的缓存)',
            '相当于写内存',
        ]},
        {'磁盘顺序写':[
            '性能基本上同写内存的性能',
        ]},
        '基于上面两点，kafka实现了写入数据的超高性能',
        '如写入一条数据花费0.01s，1s就可写十万条数据'
    ]}
],
'数据消费时':[
    {'无优化':[
        '1.如要读的数据在不在os cache里，要从磁盘文件里读取数据后放入os cache',
        '2.接着从操作系统的os cache里拷贝数据到应用程序进程的缓存',
        '3.再从应用程序进程的缓存里拷贝数据到操作系统层面的Socket缓存',
        '4.最后从Socket缓存里提取数据后发送到网卡',
        '5.最后发送出去给下游消费',
        {'问题':[
            '2,3步两次拷贝没必要',
            '且会发生好几次上下文切换'
        ]}
    ]},
    {'零拷贝技术':[
        '直接让操作系统的cache中的数据发送到网卡后传输给下游的消费者',
        '且Socket缓存中仅仅拷贝一个描述符过去，不会拷贝数据到Socket缓存',
        '跳过了两次拷贝数据步骤（其中sokect只拷贝一个描述符）'
    ]},
    '如kafka集群经过调优，大量的数据都可直接写入os cache中，然后读数据时也是从os cache中读',
    '实现基于内存提供数据的写和读'
],
'高并发写入原理':[
    '页缓存技术 + 磁盘顺序写',
    '零拷贝技术'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 