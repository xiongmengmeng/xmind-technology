import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("protocol2")
r2=s2.getRootTopic()
r2.setTitle("IP&UDP")


content={
'IP与以太网的包收发操作':[
    '包结构：头部+数据',
    'TCP/IP包：MAC头部（以太网控制信息）+IP头部（IP控制信息）+TCP头部+数据块',
    {'路由器':[
        '使用IP头部，按照【IP规则】传输包的设备',
        'IP协议的表：根据IP头部的目的地信息查出接下来应该发往哪个路由器',
        'IP协议：根据目标地址->下一路由器的MAC地址->委托以太网协议将包传输'
    ]},
    {'集线器':[
        '使用MAC头部，按照【以太网规则】传输包的设备',
        '以太网表：以太网头部中的目的地信息查出相应的传输方向',
        '以太网协议:根据MAC地址->下一个转发设备'
    ]},
    {'IP模块负责添加两个头部':[
        {'MAC头部':[
            '以太网用的头部，包含MAC地址',
            '查询MAC地址需要使用ARP',
            '网卡的ROM中保存着全世界唯一的MAC地址（生产网卡时写入）',
            '网卡中保存的MAC地址会由网卡驱动程序读取并分配给MAC模块'
        ]},
        {'IP头部':[
            'IP用的头部，包含IP地址'
        ]}
    ]},
    {'包收发操作':[
        'TCP模块:在数据块前加上TCP头部，然后整包传递给IP模块',
        'IP模块:在包前加上IP头部和MAC头部，封装好包交给网卡',
        '网卡：将数字信息->电信号或光信号，并通过网线（或光纤）发送出去',
        '信号->集线器、路由器等转发设备->接收方'
    ]},
    {'网卡':[
        {'网卡驱动':[
            '从IP模块获取包，将其复制到网卡内的缓冲区',
            '向MAC模块发送发送包的命令'
        ]},
        {'MAC模块':[
            '将包从缓冲区中取出，生成通用信号',
            '在开头加上报头和起始帧分界符，末尾加上帧校验序列',
            '报头：一段测量时钟信号的特殊信号',
            '起始帧分界符:一个表示包起始位置的标记',
            '帧校验序列:用来检查包传输过程中因噪声导致的波形紊乱、数据错误',
        ]},
        {'PHY（MAU）模块':[
            '信号转换成可在网线中传输的格式，并通过网线发送出去'
        ]}
    ]}
],
'用UDP协议收发数据的操作':[
    '适用：不需要重发的数据',
    {'发送':[
        '没有TCP的接收确认、窗口等机制',
        '收发数据前不需要交换控制信息(不需要建立和断开连接)'
    ]},
    {'接收':[
        '根据IP头部中接收方和发送方IP地址',
        'UDP头部中的接收方和发送方端口号',
        '找到相应的套接字将数据交给相应的应用程序'
    ]},
    '应用：音频和视频数据,缺少某些包不会产生严重问题，只会有一些失真或者卡顿'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 