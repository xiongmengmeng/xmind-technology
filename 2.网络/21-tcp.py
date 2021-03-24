import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("tcp")
r2=s2.getRootTopic()
r2.setTitle("tcp")


content={
'TCP的包头':[
    '源端口和目标端口',
    {'包的序号':[
        '解决【乱序问题】',
        '不编好号怎么知道哪个先来，哪个后到',
    ]},
    {'确认序号':[
        '发出去的包应该有确认，才能知道对方是否收到',
        '如没收到就应该重新发送，解决【不丢包的问题】',
    ]},
    {'状态位':[
        'SYN：发起一个链接',
        'ACK:回复',
        'RST:重新连接',
        'FIN:结束连接',
        '因TCP是面向连接的，因此需要双方维护连接状态，这些状态位的包会引起双方的状态变更',
    ]},
    {'窗口大小':[
        'TCP 要做流量控制，需通信双方各声明一个窗口，标识自己当前的处理能力',

    ]},
],
'TCP三次握手':[
    '1.刚开始的时候，客户端和服务器都处于 CLOSED 状态',
    '2.TCP协议是传输层协议，实现的是端口到端口(port)的通信。先是服务端主动监听某个端口，处于 LISTEN 状态',
    '3.然后客户端主动发起连接 SYN，之后处于 SYN-SENT 状态',
    '4.服务端接收了发起的连接，返回 SYN，并且 ACK ( 确认 ) 客户端的 SYN，之后处于 SYN-RCVD 状态',
    '5.客户端接收到服务端发送的 SYN 和 ACK 之后，发送 ACK 的 ACK，之后就处于 ESTAVLISHED 状态，因为它一发一收成功了',
    '6.服务端收到 ACK 的 ACK 之后，也处于 ESTABLISHED 状态，因为它也一发一收了'
],
'TCP四次挥手':[
    '1.断开的时候,客户端主动起断开FIN,进入FIN_WAIT_1 的状态',
    '2.服务端接收客户端发起的断开，返回ACK,进入 CLOSE_WAIT 的状态',
    '3.客户端收到服务端发送的ACK,进入FIN_WAIT_2的状态',
    '4.服务端处理事务完毕，向客户端发起结束请求FIN,进入LAST_ACK状态',
    '5.客户端收到服务端发送的FIN，返回ACK,进入TIME_WAIT状态',
    '6.服务端收到ACK后，进入CLOSED状态',
    '7.客户端在等待2MSL时间后，进入CLOSED状态',
    {'等待2MSL时间':[
        'MSL:Maximum Segment Lifetime 最大报文生存时长',
        '1.保证TCP的全双工连接能可靠关闭:防止服务器在等待2MSL时间没有收到ACK，重新传送FIN结束请求给客户端',
        '2.保证这次连接中重复的数据段从网络中消失,防止端口重用时可能的数据混淆'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 