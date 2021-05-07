import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Selector选择器")
r2=s2.getRootTopic()
r2.setTitle("Selector选择器")


content={
'定义':[
    '通过选择器，一个线程可以查询多个通道的IO事件的就绪状态',
    '选择器和通道的关系，是监控和被监控的关系',
],
'类':[
    'Selector',
    'AbstractSelector',
    {'SelectorImpl':[
        {'Set<SelectionKey> selectedKeys':[
            '有事件的通道'
        ]},
        {'HashSet<SelectionKey> keys':[
            '注册的通道'
        ]}
    ]},
    'WindowsSelectorImpl',
],
'channel注册':[
    'channel.register（Selector sel, int ops）',
    {'方法参数':[
        'Selector sel：指定通道注册到的选择器实例',
        'int ops:选择器要监控的IO事件类型',
        {'IO事件类型':[
            '1.可读：SelectionKey.OP_READ = 1 << 0',
            '2.可写：SelectionKey.OP_WRITE = 1 << 2',
            '3.连接：SelectionKey.OP_CONNECT = 1 << 3',
            '4.接收：SelectionKey.OP_ACCEPT = 1 << 4'
        ]}
    ]},
    '一条通道若能被选择，必须继承SelectableChannel类'
],
'SelectionKey选择键':[
    '那些被选择器选中的IO事件',
    {'作用':[
        '获得通道的IO事件类型，比方说SelectionKey.OP_READ',
        '获得发生IO事件所在的通道',
        '获得选出选择键的选择器实例'
    ]},
    {'方法':[
        {'selector()':[
            '得到与之关联的Selector对象'
        ]},
        {'channel()':[
            '得到与之关联的通道'
        ]},
        {'attachment()':[
            '得到与之关联的共享数据，如ByteBuffer '
        ]},
        {'isAcceptable()':[
            '是否可以accept'
        ]},
        {'isReadable()':[
            '是否可以读'
        ]},
        {'isWritable()':[
            '是否可以写'
        ]}
    ]}
],
'Selector,Selectionkey,ServerSocketChannel和SocketChannel的关系':[
    '1.服务器启动时，将ServerSocketChannel注册到selector上',
    '2.selector开始监听...'
    '3.当客户端连接时，通过ServerSocketChannel得到SocketChannel',
    {'4.将SocketChannel注册到Selector上':[
        'register(Selector sel,int ops)',
        '一个Selector可注册多个SocketChannel'
    ]},
    '5.注册后返回一个SelectionKey,会和该Selector关联(集合)',
    '6.selector进行监听,select()方法，返回有事件发生的通道的个数',
    '7.进一步得到各个SelectionKey(有事件发生)',
    '8.在通过SelectionKey反向获取SocketChannel，channel()方法',
    '9.通过得到的channel，完成业务处理'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 