import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConcurrentLinkedQueue")
r2=s2.getRootTopic()
r2.setTitle("ConcurrentLinkedQueue")


content={

'Tomcat中NioEndPoint的实现,多生产者-单消费者模型,使用ConcurrentLinkedQueue实现':[],
'NioEndpoint':[
    {'Acceptor':[
        '套接字接受线程(Socket acceptor thread)',
        '接受用户请求并把请求封装为事件任务放入Poller队列',
        '一个Connector里面只有一个Acceptor'
    ]},
    {'Poller':[
        '套接字处理线程(Socket poller thread)，Poller内部有一个队列',
        'Poller线程从自己的队列里获取具体的事件任务，将其交给Worker进行处理',
        'Poller线程的个数与处理器的核数有关'
    ]},
    {'Worker':[
        '实际处理请求的线程',
        'Worker是组件名字',
        '真正任务执行者是SocketProcessor'
    ]}
],
'使用ConcurrentLinkedQueue队列把接受请求与处理请求操作进行解耦，实现异步处理':[],
'生产者——Acceptor线程':[
    '接受客户端发来的连接请求并将其放入Poller的事件队列:',
    '1.无限循环等待客户端连接',
    '2.控制客户端请求连接数量，如果连接数量达到设置阈值，当前请求会被挂起',
    '3.从TCP缓存获取一个完成三次握手的套接字，如当前没有，线程会被阻塞挂起',
    '4.获取到一个连接套接字后,封装为事件任务，放入poller队列'
],
'消费者——Poller线程':[
    '从事件队列里面获取事件并进行处理',
    '1.从事件队列获取事件',
    '2.遍历感兴趣的channel并对感兴趣的事件进行处理'
],
'注意':[
    'ConcurrentLinkedQueue是无界队列,需合理队列大小免造成OOM'
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 