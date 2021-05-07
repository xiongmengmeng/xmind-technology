import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("单体IM系统的开发实践")
r2=s2.getRootTopic()
r2.setTitle("单体IM系统的开发实践")


content={

'通信数据包':[
    '魔数:可理解为通信的口令',
    '版本号:如在程序中有协议升级需求，又需同时兼顾新旧版本的协议，用版本号'
],
'IM系统中Protobuf消息格式的设计':[
    '消息类型使用enum定义',
    '使用一个Protobufmessage结构定义一类消息',
    '建议给应答消息加上成功标记和应答序号',
    '编解码从顶层消息开始'
],
'客户端会话ClientSession、服务端会话ServerSession':[
    {'导航关系有两个方向':[
        {'正向导航':[
            '通过会话导航到通道，主要用于出站处理的场景，通过会话将数据包写出到通道'
        ]},
        {'反向导航  ':[
            '通过通道导航到会话，主要用于入站处理的场景，通过通道获取会话，以便进一步进行业务处理'
        ]}
    ]},
    {'通道的容器属性':[
        {'Attribute':[
            'Attribute的设值:attr().set()',
            'Attribute的取值:attr().get()'
        ]}
    ]},
    'ServerSession服务器端会话类:每个ServerSession实例都拥有一个唯一标识，为sessionId',
    'SessionMap会话管理器'
],
'心跳检测':[
    {'网络连接的假死':[
        '如底层的TCP连接已断开，但服务器端并没有正常地关闭套接字，服务器端认为这条TCP连接仍是存在的',
        {'解决假死的有效手段':[
            '客户端定时进行心跳检测，服务器端定时进行空闲检测'
        ]}
    ]},
    {'客户端的心跳报文':[
        '客户端定期发送数据包到服务器端的数据包'
    ]},
    {'服务器端的空闲检测':[
        '每隔一段时间，检测子通道是否有数据读写，如有，则子通道正常；如没有，子通道被判定为假死，关掉子通道',
        {'实现':[
            'IdleStateHandler空闲状态处理器(Netty自带)',
            '自定义处理器：对空间检测进一步处理'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 