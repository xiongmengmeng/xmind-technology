import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("DNS查询服务器")
r2=s2.getRootTopic()
r2.setTitle("DNS查询服务器")


content={
'DNS服务器工作原理':[
    '1.客户端首先访问最近一台DNS服务器',
    '2.最近的DNS服务器保存了根域DNS服务器信息，将消息转发给根域DNS服务器',
    '3.根域DNS服务器返回其下com域的DNS服务器,最近的DNS服务器向com域的DNS服务器发送消息',
    '4.com域服务器会返回其下glasscom.com域的DNS服务器的IP地址，最近的DNS服务器向...',
    '5.重复前面步骤,找到目标DNS服务器',
    '实际情况：通过缓存加快DNS服务器的响应'
],
'根据域名查IP地址过程':[
    '1.浏览器调用Socket库中的gethostbyname的程序组件(解析器)',
    '2.Socket库中的解析器:组装给DNS服务器的查询消息',
    '3.委托操作系统内部的协议栈发消息给DNS服务器',
    '4.协议栈：通过网卡将消息发送给DNS服务器',
    '5.DNS服务器：将IP地址写入响应消息并返回给客户端',
    '6.消息->网络->客户端，经过协议栈->解析器',
    '7.解析器:读取IP地址，传给应用程序（写入应用程序指定的内存地址）',
    {'注':[
        'Socket库：调用网络功能的程序组件集合',
        '协议栈:根据套接字中记录的控制信息来工作的'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 