import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Reactor反应器的三种模式")
r2=s2.getRootTopic()
r2.setTitle("Reactor反应器的三种模式")


content={
'分类标准':[
    '根据Reactor的数量和处理资源池线程的数量'
],
'单Reactor单线程':[
    {'类似事件驱动模式':[
        '当有事件触发时，事件源会将事件分发到handler处理器进行事件处理'
    ]},
    {'定义':[
        'Reactor反应器和Handers处理器处于一个线程'
    ]},
    {'2个重要方法':[
        {'void attach(Object o)':[
            '主要是将Handler处理器实例，作为附件添加到SelectionKey选择键实例'
        ]},
        {'Object attachment()':[
            '取出之前通过attach(Object o)添加到SelectionKey的附件'
        ]}
    ]},
    {'IOHandler处理器':[
        {'构造器':[
            '1.将新的SocketChannel传输通道，注册到反应器Reactor类的同一个选择器中，保证Reactor类和Handler类在同一个线程',
            '2.将IOHandler自身作为附件，attach到了选择键中，这样在Reactor类分发事件（选择键）时，能执行到IOHandler的run方法'
        ]},
        {'两大职责':[
            '接受新连接',
            '为新连接创建一个输入输出的Handler处理器'
        ]}
    ]}
],
'单Reactor多线程':[
    {'改进':[
        {'升级Handler处理器':[
            '既要使用多线程，又要尽可能高效率，考虑使用线程池'
        ]}
    ]},
],
'主从Reactor多线程':[
    {'说明':[
        '1.Reactor主线程MainReactor对象通过select监听连接事件，收到事件后，通过Acceptor处理连接事件',
        '2.当Acceptor处理连接事件后，MainReactor将连接分配给SubReactor',
        '3.SubReactor将连接加入到连接队列进行监听并创建handler进行各种事件处理',
        '4.当有新事件发生时，SubReactor会调用对应的handler处理',
        '5.handler通过read读取数据，分发给后面的worker线程处理',
        '6.worker线程池分配独立的worker线程进行业务处理，并返回结果',
        '7.handler收到响应的结果后，再通过send将结果返回给client',
        '8.Reactor主线程可对应多个Reactor子线程'
    ]},
    {'改进':[
        {'升级Reactor反应器':[
            '引入多个Selector选择器，提升选择大量通道的能力'
        ]}
    ]},
    {'反应器':[
        '如果服务器为多核CPU，可将反应器线程拆分为多个子反应器（SubReactor）线程',
        '引入多个选择器，每一个SubReactor子线程负责一个选择器,提高反应器管理大量连接，选择大量通道的能力'
    ]},
    {'处理器':[
        '引入一个线程池（ThreadPool），在线程池中执行业务处理的代码',
        '做到业务处理线程和反应器IO事件线程的完全隔离，避免服务器的连接监听受到阻塞'
    ]},
    {'优点':[
        '父线程与子线程的数据交互简单职责明确，父线程只需要接收瓣连接，子线程完成后续的业务处理',
        '父线程与子线程的数据交互简单，Reactor主线程只需把新连接传给子线程，子线程无需返回数据'
    ]},
    {'缺点':[
        '编程复杂度高'
    ]},
    {'应用':[
        'Nginx主从Reactor多进程模型',
        'Memcached主从多线程',
        'Netty主从多线程模型'
    ]}
]        



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 