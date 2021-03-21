import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("网络")
r2=s2.getRootTopic()
r2.setTitle("网络")


content={
'应用程序':[
    '网络应用程序',
    {'Socket库':[
        '应用层与TCP/IP协议族通信的中间软件抽象层',
        '是一组接口',
        'Socket函数'
    ]},
    '使用HTTP、FTP、SMTP协议'
],
'操作系统':[
    {'传输层':[
        'TCP/UDP协议',
        '定义端口，标识应用程序身份，实现端口到端口的通信'
    ]},
    {'网络层':[
        'IP协议:定义网络地址，区分网段',
        'APR协议:子网内MAC寻址',
        '路由协议:对于不同子网的数据包进行路由'
    ]}
],
'网卡驱动+网卡':[
    {'链路层':[
        '对电信号进行分组并形成具有特定意义的数据帧',
        '然后以广播形式通过物理介质发送给接收方'
    ]},
    {'组成':[
        '缓冲区',
        'MAC模块',
        'PHY（MAU）模块'
    ]}
],
'物理层':[
    '路由器，集线器',
    {'物理介质':[
        '双绞线',
        '光纤',
        '无线电波'
    ]}
],
'重点':[
    '三次握手',
    '四次挥手',
    '客户端，服务器的Socket编程'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 