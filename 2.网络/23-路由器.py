import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("路由器")
r2=s2.getRootTopic()
r2.setTitle("路由器")


content={
'集线器':[
    '无脑将电信号转发到所有出口（广播），不做任何处理',
    '物理层',
    {'MAC 地址':[
        '连接到集线器的设备的唯一标识'
    ]},
    {'传输方式':[
        '广播'
    ]}
],
'交换机':[
    '只发给目标 MAC 地址指向的那台电脑,只比集线器智能一些',
    '数据链路层',
    {'内部维护一张MAC地址表':[
        '记录着每一个 MAC 地址的设备，连接在其哪一个端口上'
    ]},
    {'以太网':[
        '通过这样传输方式而组成的小范围的网络'
    ]},
    {'arp':[
        '根据IP找到对映的MAC地址',
        'arp缓存表，表中记录着IP与MAC地址的对应关系'
    ]}
],
'路由器':[
    '作为一台独立的拥有【MAC 地址】的设备，可以帮着把数据包做一次转发',
    '路由器的每一个端口，都有独立的 MAC 地址',
    '网络层',
    {'IP 地址':[
        '通过子网掩码，标识一个子网'
    ]},
    {'默认网关':[
        '电脑里配置的一个 IP 地址，以便在发给不同子网的机器时，发给这个 IP 地址'
    ]},
    {'路由器':[
        '收到的这个数据包，该从自己的哪个端口出去',
        '目的地址-下一跳-端囗'
    ]}
],
'涉及到的三张表':[
    {'交换机中有 MAC 地址':[
        '映射 MAC 地址和它的端口',
        '通过以太网内各节点之间不断通过交换机通信，不断完善起来的'
    ]},
    {'路由器中有路由表':[
        '映射 IP 地址(段)和它的端口',
        '各种路由算法 + 人工配置逐步完善起来的'
    ]},
    {'电脑和路由器中都有 arp 缓存表':[
        '缓存 IP 和 MAC 地址的映射关系',
        '不断通过 arp 协议的请求逐步完善起来的'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 