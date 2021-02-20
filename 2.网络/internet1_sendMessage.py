import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("sendMessage")
r2=s2.getRootTopic()
r2.setTitle("浏览器生成消息")


content={
'1.组装HTTP请求消息':[
    {'URL解析':[
        '访问数据源机制（协议）+web服务器名+文件路径名',
        '协议类型：http,ftp,mailto，file'
    ]},
    {'请求消息':[
        '第一行：请求方式 请求地址 协议',
        '第二行：消息头',
        '空行',
        '消息体',
    ]},
    {'响应消息':[
        '第一行：状态码和响应短语',
        '...'
    ]}
],
'2.请求DNS查询服务器IP地址':[
    {'根据域名查IP地址':[
        'Socket库：调用网络功能的程序组件集合',
        '协议栈:根据套接字中记录的控制信息来工作的',
        '1.浏览器调用Socket库中的gethostbyname的程序组件(解析器)',
        '2.Socket库中的解析器:组装给DNS服务器的查询消息',
        '3.委托操作系统内部的协议栈发消息给DNS服务器',
        '4.协议栈：通过网卡将消息发送给DNS服务器',
        '5.DNS服务器：将IP地址写入响应消息并返回给客户端',
        '6.消息->网络->客户端，经过协议栈->解析器',
        '7.解析器:读取IP地址，传给应用程序（写入应用程序指定的内存地址）'
    ]},
    {'TCP/IP的基本思路':[
        '子网:通过路由器连接组成的一个大的网络',
        '网络:将子网通过路由器连接起来',
        '1.发送者发出的消息->子网中的集线器->距离发送者最近的路由器',
        '2.路由器根据消息的目的地判断下一个路由器位置，将消息发送到下一个路由器(委托集线器)',
        '3.前面过程不断重复，最终消息就被传送到目的地'
    ]},
    {'IP地址':[
        '网络中，所有的设备都会被分配一个地址',
        '网络号：主机号',
        '子网掩码表示网络号与主机号的边界',
        '子网掩码为1的部分：网络号，子网掩码为0的部分：主机号',
        '主机号全为0：整个子网',
        '主机号全为1：向子网上所有设备发送包，即“广播”'
    ]},
    {'DNS服务器工作原理':[
        '1.客户端首先访问最近一台DNS服务器',
        '2.最近的DNS服务器保存了根域DNS服务器信息，将消息转发给根域DNS服务器',
        '3.根域DNS服务器返回其下com域的DNS服务器,最近的DNS服务器向com域的DNS服务器发送消息',
        '4.com域服务器会返回其下glasscom.com域的DNS服务器的IP地址，最近的DNS服务器向...',
        '5.重复前面步骤,找到目标DNS服务器',
        '实际情况：通过缓存加快DNS服务器的响应'
    ]}
],
'3.委托协议栈发送消息':[
    {'1.创建套接字阶段':[
        '调用Socket库中socket程序组件,协议栈返回一个描述符'
    ]},
    {'2.连接阶段':[
        '调用Socket库中connect程序组件',
        '需指定描述符、服务器IP地址和端口号这3个参数',
        '描述符：应用程序用来识别套接字的机制',
        'IP地址和端口号:客户端和服务器之间识别对方套接字的机制'
    ]},
    {'3.通信阶段（收发数据）':[
        '发送消息：调用Socket库中write程序组件',
        '需指定描述符和发送数据',
        '接收消息：调用Socket库中的read程序组件'
    ]},
    {'4.断开阶段':[
        '调用Socket库中的close程序组件',
        'Web服务器会首先调用close来断开连接',
        '浏览器调用read得知收发数据已结束，也会调用close进入断开阶段',
        '一段时间后删除套接字'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 