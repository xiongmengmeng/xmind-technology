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
'常见的三种模式':[
    {'一个线程处理一个连接(Connection Per Thread)模式':[
        {'定义':[
            '给每一个新的网络连接都分配给一个线程,每个线程独自处理自己负责的输入和输出'
        ]},
        {'缺点':[
            '对应大量连接，需耗费大量线程资源'
        ]}
    ]},
    {'单线程Reactor反应器模式':[
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
    {'多线程Reactor反应器模式':[
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
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 