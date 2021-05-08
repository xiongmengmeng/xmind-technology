import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("NioEventLoopGroup")
r2=s2.getRootTopic()
r2.setTitle("NioEventLoopGroup")


content={
'MultithreadEventExecutorGroup':[
    {'属性':[
        {'EventExecutorChooserFactory.EventExecutorChooser chooser':[
            ''
        ]}
    ]},
    {'next()':[
        'chooser.next()'
    ]}
],
'MultithreadEventLoopGroup':[
    {'next()':[
        '(EventLoop) super.next()'
    ]},
    {'register(Channel channel)':[
        'next().register(channel)'
    ]}
],
'NioEventLoopGroup':[
    {'属性':[
        {'EventExecutor[] children':[
            '继承自父类MultithreadEventExecutorGroup'
        ]}
    ]},
    {'构造器':[
        '默认线程个数n:Runtime.getRuntime().availableProcessors() * 2,CPU核数的2倍',
        '创建指定线程数的执行器组children=new EventExecutor[n]',
        '初始化执行器组，添加元素为NioEventLoop实例(实例化时，会初始化一个Selector)',
        '每个NioEventLoop实例添加一个关闭监听器'
    ]},
],
'Netty 接受请求过程梳理':[
    {'总体流程':[
        '接受连接',
        '创建一个新的 NioSocketChannel',
        '注册到一个 worker EventLoop 上',
        '注册 selecot Read 事件'
    ]},
    {'详细':[
        '1.服务器轮询Accept事件，获取事件后调用unsafe的read方法，unsafe是ServerSocket的内部类， 该方法内部由2部分组成',
        {'2.doReadMessages()':[
            '用于创建NioSocketChannel对象，该对象包装JDK的Nio Channel客户端',
            '创建相关的pipeline,unsafe,config'
        ]},
        {'3.pipeline.fireChannelRead()':[
            '将自己绑定到一个chooser选择器选择的workerGroup中的一个EventLoop，并且注册'
        ]}

    ]}
],





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 