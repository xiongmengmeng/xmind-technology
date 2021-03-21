import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("传输层")
r2=s2.getRootTopic()
r2.setTitle("传输层")


content={
'作用':[
    '定义端口，标识应用程序身份，实现端口到端口的通信'
],
'使用协议':[
    'UDP协议',
    'TCP协议(TCP就是有确认机制的UDP协议):三次握手+ACK确认'
],
'TCP/UDP数据包':[
    '首部8个字节，主要包括源端口和目标端口',
    '数据:UDP最大为65527个字节,TCP不限,但不会超过IP数据包的长度,防止分割'
],
'ACK':[
    {'ACK号等待时间':[
        '据网络包平均往返时间调整ACK号等待时间'
    ]},
    {'方式':[
        '一来一回方式',
        {'滑动窗口方式':[
            '接收方需要告诉发送方自己最多能接收多少数据(接收缓冲区剩余空间)',
            '发送方根据这个值对数据发送操作进行控制',
            'ACK与窗口的合并,减少网络开销'
        ]}
    ]},
    '通过“序号”和“ACK号”确认接收方是否收到了网络包',
],
'用UDP协议收发数据':[
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