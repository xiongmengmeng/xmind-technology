import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Reactor反应器模式")
r2=s2.getRootTopic()
r2.setTitle("Reactor反应器模式")


content={
'反应器模式':[
    '高性能网络编程在设计和架构层面的基础模式',
    '由Reactor反应器线程、Handlers处理器两大角色组成',
    {'Reactor反应器线程':[
        '负责响应IO事件，并且分发到Handlers处理器'
    ]},
    {'Handlers处理器':[
        '非阻塞的执行业务处理逻辑'
    ]},
    {'应用':[
        '“全宇宙最有名的、最高性能”的Web服务器Nginx',
        '最高性能的缓存服务器之一Redis',
        '开源项目中应用极为广泛的高性能通信中间件Netty'
    ]}
],
'常见的三种模式(根据Reactor的数量和处理资源池线程的数量)':[
    {'单Reactor单线程':[
        {'定义':[
            '给每一个新的网络连接都分配给一个线程,每个线程独自处理自己负责的输入和输出'
        ]},
        {'缺点':[
            '对应大量连接，需耗费大量线程资源'
        ]}
    ]},
    {'单Reactor多线程':[
        {'类似事件驱动模式':[
            '当有事件触发时，事件源会将事件分发到handler处理器进行事件处理'
        ]},
        {'定义':[
            'Reactor反应器和Handers处理器处于一个线程'
        ]},
        {'2个重要组件':[
            {'Reactor反应器':[
                '负责查询IO事件，当检测到一个IO事件，将其发送给相应的Handler处理器去处理'
            ]},
            {'Handler处理器':[
                '与IO事件（或者选择键）绑定，负责IO事件的处理',
                '完成真正的连接建立、通道读取、业务逻辑处理、结果写出到通道等'
            ]}
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
    ]},
    {'主从Reactor多线程':[
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
            ]},
            {'升级Handler处理器':[
                '既要使用多线程，又要尽可能高效率，考虑使用线程池'
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
    ]}        
],
'优点':[
    {'响应快':[
        '虽然同一反应器线程本身是同步的，但不会被单个连接的同步IO所阻塞'
    ]},
    {'编程相对简单':[
        '最大程度避免复杂的多线程同步，也避免了多线程的各个进程之间切换的开销'
    ]},
    {'可扩展':[
        '可以方便地通过增加反应器线程的个数来充分利用CPU资源'
    ]}
],
'缺点':[
    '反应器模式需要操作系统底层的【IO多路复用】的支持',
    '同一个Handler业务线程中，如出现一个长时间的数据读写，会影响这个反应器中其他通道的IO处理'
],
'和其他模式的对比':[
    {'和生产者消费者模式对比':[
        '反应器模式是基于查询的，没有专门的队列去缓冲存储IO事件',
    ]},
    {'和观察者模式（Observer Pattern）对比':[
        '每一个IO事件（选择键）被查询后，反应器会将事件分发给所绑定的Handler处理器',
        '观察者模式中，同一个时刻，同一个主题可以被订阅过的多个观察者处理'
    ]}
],
'Netty模型':[
    '1.Netty抽象出两组线程池，BossGroup专门负责接收客户端的连接，WorkerGroup专门负责网络的读写',
    '2.BossGroup和WorkerGroup类型都是NioEventLoopGroup',
    '3.NioEventLoopGroup相当于事件循环组，这个组中包裹有多个事件循环，每个事件循环都是一个NioEventLoop',
    '4.NioEventLoop表示一个不断循环的执行处理任务的线程，每个NioEventLoop都有一个Selector,用于监听绑定在其上socketChannel的网络通讯',
    '5.NioEventLoopGroup可以有多个线程，即可含有多个NioEventLoop',
    {'6.每个Boss NioEventLoop循环执行3个步骤':[
        '6.1.轮询accept事件',
        '6.2.处理accept事件，与client建立连接，生成NioSocketChannel,并将其注册到某个work NioEventLoop上的selector',
        '6.3.处理任务队列的任务，即runAllTasks'
    ]},
    {'7.每个worker NioEventLoop循环执行3个步骤':[
        '7.1.轮询read,write事件',
        '7.2.处理io事件，即read,write事件，在对应的NioSocketChannel处理',
        '7.3.处理任务队列的任务，即runAllTasks'
    ]}
    '',
    ''
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 