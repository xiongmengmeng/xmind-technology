import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Connector组件")
r2=s2.getRootTopic()
r2.setTitle("Connector组件")


content={
'HTTP阻塞模式协议——Http11Protocol':[
    {'套接字接收终端——JIoEndpoint':[
        '端口监听客户端请求，接收套接字连接，提供一个线程池处理接收到的套接字连接，负责对连接数的控制，负责安全与非安全套接字连接的实现等',
        {'LimitLatch（连接数控制器)':[
            '控制套接字连接个数->控制流',
            'BIO模式,连接数:线程数=1:1',
            '默认情况，Tomcat处理连接池的线程数为200->BIO流量控制阀门大小也默认为200'
        ]},
        {'Acceptor（套接字接收器）':[
            '监听是否有客户端套接字连接并接收套接字',
            '将套接字交由Executor执行'
        ]},
        {'ServerSocketFactory套接字工厂':[
            '接收终端安全配置不同，套接字不同，引入了工厂模'
        ]},
        {'Executor任务执行器':[
            '使用JUC工具包的ThreadPoolExecutor类'
        ]},
        {'SocketProcessor(任务定义器)':[
            '处理套接字并响应客户端',
            '连接数计数器减1',
            '关闭套接字'
        ]}
    ]},
    {'HTTP阻塞处理器——Http11Processor':[
        '套接字的读写和过滤，请求报文解析,生成Request对象，响应内容解析，生成Response对象',
        '套接字输入缓冲装置——InternalInputBuffer',
        '4个过滤器：IdentityInputFilter、VoidInputFilter、BufferedInputFilter、ChunkedInputFilter',
        {'套接字输出缓冲装置——InternalOutputBuffer':[
            'OutputStream：套接字的输出通道，通过其将字节写入到操作系统底层',
            'OutputStreamOutputBuffer：提供字节流输出的通道,与OutputFilter组合实现过滤效果',
            'OutputFilter：过滤器组件',
            'ByteChunk：为某个流添加缓冲功能'
        ]}
    ]}
],
'HTTP非阻塞模式协议——Http11NioProtocol':[
    {'非阻塞接收终端——NioEndpoint':[
        'LimitLatch（连接数控制器)：对于NIO模式，Tomcat默认流量阀门为10 000',
        'Acceptor（套接字接收器）:负责接收套接字连接并注册到通道队列里面',
        'Poller（轮询器）:负责轮询检查事件列表',
        {'Poller（轮询器）':[
            '负责轮询检查事件列表',
            '内部依赖JDK的Selector对象进行轮询，选择出待处理的事件，每轮询一次就选出若干需要处理的通道'
        ]},
        'Poller池:包含了若干Poller组件',
        {'SocketProcessor（任务定义器）':[
            '用NIO方式读取套接字并进行处理，输出响应报文',
            '连接数计数器减一腾出通道',
            '关闭套接字'  
        ]},
        'Executor（任务执行器）'
    ]},
    {'HTTP非阻塞处理器——Http11NioProcessor':[
        '提供了对HTTP协议非阻塞模式的处理，作用同Http11Processor'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 