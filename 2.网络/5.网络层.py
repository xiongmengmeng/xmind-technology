import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("网络层")
r2=s2.getRootTopic()
r2.setTitle("网络层")


content={
'作用':[
    '定义网络地址，区分网段，子网内MAC寻址，对于不同子网的数据包进行路由'
],
'使用协议':[
    'IP协议',
    'ARP协议',
    '路由协议'
],
'IP数据包':[
    '首部:20个字节，主要包括目标IP地址(网关路由的线索和依据)和源IP地址',
    '数据:最大长度为65515字节',
    '注:太网数据包最大长度是1500个字符，如超过这个大小，需对IP数据包进行分割，分成多帧发送'
],
'IP协议':[
    {'作用':[
        '制定网络地址，区分两台主机是否同属一个网络'
    ]},
    '两个版本，分别是IPv4(一个32位的地址，常用4个十进制数字表示)和IPv6',
    {'地址分两部分':[
        '网络地址',
        '主机地址:该主机在局域网中的地址'
    ]},
    '如两IP地址在同一个子网内，网络地址一定相同',
    {'子网掩码':[
        '表示网络地址与主机地址的边界',
        '为1部分：网络地址，为0部分：主机地址',
        'IP地址和子网掩码通过&运算得到网络地址',
        '主机地址全为0：整个子网',
        '主机地址全为1：向子网上所有设备发送包，即广播'
    ]},
    '发送者和接收者的IP地址已知(应用层的协议传入)， 我们只需通过子网掩码对两个IP地址进行&运算后判断双方是否在同一个子网',
    {'子网':[
        '通过路由器连接组成的一个大的网络'
    ]},
    {'网络':[
        '将子网通过路由器连接起来'
    ]},
    {'IP模块':[
        '负责添加两个头部:IP头部+MAC头部',
        'TCP/IP包：MAC头部（以太网控制信息）+IP头部（IP控制信息）+TCP头部+数据块',
    ]}
],
'ARP协议':[
    {'作用':[
        '地址解析协议，根据IP地址获取MAC地址'
    ]},
    {'局限':[
        'ARP的MAC寻址局限在同一个子网中'
    ]},
    {'工作原理':[
        '1.发起一个请求数据包，数据包首部包含目标主机的IP地址',
        '2.数据包会在链路层再次包装，生成以太网数据包，由以太网广播给子网内的所有主机',
        '3.每台主机都会接收到这个数据包，取出里面的IP地址与自己的比较，如相同返回自己的MAC地址，不同就丢弃',
        '4.ARP接收返回消息，以此确定目标机的MAC地址',
        '5.将返回的MAC地址与对应的IP地址存入本机ARP缓存并保留一定时间，下次请求时直接查询ARP缓存以节约资源'
    ]}
],
'路由协议':[
    {'工作原理':[
        '1.通过IP协议判断两主机是否在同一个子网，如在，通过ARP协议查询对应的MAC地址',
        '2.如不在同一子网，以太网将该数据包转发给本子网的网关进行路由',
        '网关(互联网上子网与子网间的桥梁)进行多次转发，最终将该数据包转发到目标IP所在子网，再通过ARP获取目标机MAC'
    ]},
    {'路由器':[
        '完成路由协议的物理设备',
        '扮演者交通枢纽的角色，它会根据信道情况，选择并设定路由，以最佳路径来转发数据包'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 