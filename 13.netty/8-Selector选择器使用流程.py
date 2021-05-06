import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Java NIO-选择器使用流程")
r2=s2.getRootTopic()
r2.setTitle("Java NIO-选择器使用流程")


content={
'1.获取选择器实例':[
    {'open()':[
        '向选择器SPI发出请求，通过默认的SelectorProvider（选择器提供者）对象，获取一个新的选择器实例'
    ]},
    {'调用Selector的静态方法open()获取实例':[
        'Selector selector=Selector.open()'
    ]}
],
'2.将通道注册到选择器中':[
    '调用通道的register()方法，将通道注册到了一个选择器上',
    {'获取通道':[
        'ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();',
    ]},
    {'设置为非阻塞':[
        'serverSocketChannel.configureBlocking(false)'
    ]},
    {'绑定连接':[
        'serverSocketChannel.bind(new InetSocketAddress(SystemConfig.SOCKET_SERVER_PORT))'
    ]},
    {'将通道注册到选择器上，并制定监听事件为：“接收连接”事件':[
        'serverSocketChannel.register(selector, SelectionKey.OP_ACCEPT)'
    ]},
],
'3.轮询感兴趣的IO就绪事件（选择键集合）':[
    {'1.Selector选择器的select()方法':[
        '选出已经注册的、已经就绪的IO事件，保存到SelectionKey选择键集合中',
        {'select()':[
            '阻塞调用',
            '监控注册通道，当其中有IO操作可行时，将对应SelectionKey加入到内部集合Set<SelectioonKey> selectedKeys',
            '返回的整数值（int整数类型）:发生的IO事件的通道数量'
        ]},
        {'selectNow()':[
            '非阻塞调用'
        ]}
    ]},
    {'2.遍历SelectionKey集合，拿到IO事件':[
        {'selectedKeys()':[
            '取得选择键集合'
        ]},
        {'遍历SelectionKey集合':[
            'SelectionKey集合保存在选择器实例内部，是一个元素为SelectionKey类型的集合（Set）'
        ]}
    ]},
    {'3.处理完，需将选择键从SelectionKey集合中移除':[
        'keyIterator.remove()',
        '防止下一次循环的时候，被重复的处理'
    ]},

],
'例':[
    '//轮询，选择感兴趣的IO就绪事件（选择键集合）',
    'while (selector.select() > 0) {',
    '   Set selectedKeys = selector.selectedKeys();',
    '   Iterator keyIterator = selectedKeys.iterator();',
    '   while(keyIterator.hasNext()) {',
    '       SelectionKey key = keyIterator.next();',
    '       //根据具体的IO事件类型，执行对应的业务操作',
    '       if(key.isAcceptable()) {',
    '           // IO事件：ServerSocketChannel服务器监听通道有新连接',
    '           SocketChannel channel=serverSocketChannel.accept();',
    '           channel.register(selector,SelectionKey.OP_READ)',
    '       } else if (key.isConnectable()) {',
    '           // IO事件：传输通道连接成功',
    '       } else if (key.isReadable()) {',
    '           // IO事件：传输通道可读',
    '           SocketChannel channel=(SocketChannel）key.channel();',
    '       } else if (key.isWritable()) {',
    '           // IO事件：传输通道可写',
    '       }',
    '   }',
    '   //处理完成后，移除选择键',
    '   keyIterator.remove();',
    '}'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 