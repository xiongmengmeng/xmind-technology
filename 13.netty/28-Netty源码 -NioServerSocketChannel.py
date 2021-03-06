import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("NioServerSocketChannel")
r2=s2.getRootTopic()
r2.setTitle("NioServerSocketChannel")


content={
'AbstractChannel':[
    {'属性':[
        {'EventLoop eventLoop':[
            ''
        ]},
        {'DefaultChannelPipeline pipeline':[
            ''
        ]},
        {'Unsafe unsafe':[
            ''
        ]}
    ]},
    {'构造器AbstractChannel(Channel parent)':[
        'id = newId();',
        'unsafe = newUnsafe();',
        'pipeline = newChannelPipeline();'
    ]},
    {'newChannelPipeline()':[
        'new DefaultChannelPipeline(this)'
    ]},
    {'bind(SocketAddress localAddress, ChannelPromise promise)':[
        'pipeline.bind(localAddress, promise)'
    ]},
    {'bind(final SocketAddress localAddress, final ChannelPromise promise)':[
        '调用doBind(localAddress),子类实现'
    ]},
    {'register(EventLoop eventLoop, final ChannelPromise promise)':[
        'eventLoop.execute(()->register0(promise))'
    ]},
    {'register0(ChannelPromise promise)':[
        '调用doRegister()'
    ]},
    {'doRegister()':[
        'selectionKey=javaChannel().register(eventLoop().unwrappedSelector(), 0, this)',
        {'javaChannel()':[
                '返回ch,类型是java nio中ServerSocketChannelImpl'
        ]}
    ]}
],
'AbstractNioChannel':[
    {'属性':[
        {'SelectableChannel ch':[
            'java nio中的channel'
        ]}
    ]},
    {'构造器AbstractNioChannel(Channel parent, SelectableChannel ch, int readInterestOp)':[
        'super(parent)',
        'this.ch = ch',
        'this.readInterestOp = readInterestOp'
    ]}
],
'AbstractNioMessageChannel':[
    {'内部类NioMessageUnsafe':[
        {'read()':[
            'doReadMessages(readBuf)：子类实现',
            'pipeline.fireChannelRead(readBuf.get(i))'
        ]}
    ]},
    {'构造器AbstractNioMessageChannel(Channel parent, SelectableChannel ch, int readInterestOp)':[
        'super(parent, ch, readInterestOp)'
    ]},
    {'newUnsafe()':[
        'new NioMessageUnsafe()'
    ]},
    {'内部类NioMessageUnsafe':[
        {'read()':[
            'doReadMessages(readBuf)',
            'pipeline.fireChannelRead(readBuf.get(i))'
        ]}
    ]}
],
'NioServerSocketChannel':[
    {'构造器NioServerSocketChannel()':[
        'this(newSocket(DEFAULT_SELECTOR_PROVIDER))',
        {'DEFAULT_SELECTOR_PROVIDER':[
            '=SelectorProvider.provider()',
            '返回WindowsSelectorProvider',
            {'WindowsSelectorProvider.openSelector()':[
                'new WindowsSelectorImpl(this)'
            ]}
        ]},
        {'newSocket(SelectorProvider provider)':[
            '=provider.openServerSocketChannel()',
            '返回ServerSocketChannelImpl'
        ]}
    ]},
    {'NioServerSocketChannel(ServerSocketChannel channel)':[
        'super(null, channel, SelectionKey.OP_ACCEPT)',
        'config = new NioServerSocketChannelConfig(this, javaChannel().socket())'
    ]},
    {'doBind(SocketAddress localAddress)':[
        'javaChannel().bind(localAddress, config.getBacklog())'
    ]},
    {'doReadMessages(List<Object> buf)':[
        {'SocketChannel ch=SocketUtils.accept(javaChannel())':[
            '内部调用serverSocketChannel.accept()创建SocketChannel'
        ]},
        {'buf.add(new NioSocketChannel(this, ch))':[
            '将SocketChannel封装进NioSocketChannel，并放入传参'
        ]}
    ]}
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 