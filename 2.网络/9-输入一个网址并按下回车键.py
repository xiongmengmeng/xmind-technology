import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("输入一个网址并按下回车键")
r2=s2.getRootTopic()
r2.setTitle("输入一个网址并按下回车键")


content={
'网络请求的各主要组件':[
    {'应用程序':[
        '网络应用程序+Socket库'
    ]},
    {'操作系统的协议栈':[
        'TCP,UDP协议',
        'IP,ARP,路由协议'
    ]},
    '网卡驱动程序',
    {'硬件':[
        '网卡'
    ]}
],
'详细':[
    '1.首先，应用层协议对该请求包做了格式定义':,
    '2.紧接着传输层协议加上了双方的端口号，确认了双方通信的应用程序',
    '3.然后网络协议加上了双方的IP地址，确认了双方的网络位置',
    '4.最后链路层协议加上了双方的MAC地址，确认了双方的物理位置,',
    '同时将数据进行分组，形成数据帧，采用广播方式，通过传输介质发送给对方主机',
    '5.对于不同网段，该数据包首先会转发给网关路由器，经过多次转发后，最终被发送到目标主机',
    '6.目标机接收到数据包后，采用对应的协议，对帧数据进行组装',
    '7.然后再通过一层一层的协议进行解析',
    '8.最终被应用层的协议解析并交给服务器处理',
],
'简述':[
    '当通过http发起一个请求时，应用层、传输层、网络层和链路层的相关协议依次对该请求进行包装并携带对应的首部',
    '最终在链路层生成以太网数据包',
    '以太网数据包通过物理介质传输给对方主机',
    '对方接收到数据包以后，然后再一层一层采用对应的协议进行拆包，最后把应用层数据交给应用程序处理'
],
'学习':[
    'https://zhuanlan.zhihu.com/p/273434776'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 