import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Socket")
r2=s2.getRootTopic()
r2.setTitle("Socket")


content={


'socket()':[
    {'参数':[
        'domain:协议域',
        'type:socket类型',
        'protocol:协议'
    ]},
    '创建一个socket描述符',
    '对应于普通文件的打开操作'
],
'bind()函数':[
    {'参数':[
        'sockfd:socket描述字',
        'addr:要绑定给sockfd的协议地址',
        'addrlen:地址的长度'
    ]},
    '把一个地址族中的特定地址赋给socket',
    '如把一个ipv4或ipv6地址和端口号组合赋给socket'
],
'listen()函数':[
    {'参数':[
        'sockfd:要监听的socket描述字',
        'backlog:socket可以排队的最大连接个数'
    ]},
    '监听这个socket',
    '如果客户端这时调用connect()发出连接请求，服务器端就会接收到这个请求'
],
'connect()函数':[
    {'参数':[
        'sockfd:为客户端的socket描述字',
        'addr:服务器的socket地址',
        'addrlen:socket地址的长度'
    ]},
    '客户端通过调用connect函数来建立与TCP服务器的连接'
],
'accept()函数':[
    {'参数':[
        'sockfd:为客户端的socket描述字',
        'addr:客户端的协议地址',
        'addrlen:客户端的协议地址长度'
    ]},
    '返回的是已连接的socket描述字(内核为每个由服务器进程接受的客户连接创建了一个已连接socket描述字)',
    'TCP服务器监听到这个请求之后，就会调用accept()函数取接收请求,'
],
'read()、write()函数':[
    {'参数':[
        'fd:对方的socket描述字',
        'buf:缓冲区',
        'count'
    ]},
    'read函数是负责从fd中读取内容，返回的值是0表示已经读到文件的结束了，',
    'write函数将buf中的nbytes字节内容写入文件描述符fd.成功时返回写的字节 数'
],
'close()函数':[
    'close一个TCP socket的缺省行为时把该socket标记为以关闭，然后立即返回到调用进程。该描述字不能再由调用进程使用，也就是说不能再作为read或write的第一个参数',
    '注：只是使相应socket描述字的引用计数-1，只有当引用计数为0的时候，才会触发TCP客户端向服务器发送终止连接请求',
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 