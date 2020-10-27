import xmind
from xmind.core.markerref import MarkerId

w = xmind.load("c:\\Users\\btr\\Desktop\\tcp.xmind") 
s2=w.createSheet()
s2.setTitle("tcp")
r2=s2.getRootTopic()
r2.setTitle("tcp")


# content={

# '前言':[
#     {'网卡':[
#         '网络适配器（Network Adapter），是连接计算机和传输介质的接口',
#         '主要用来将计算机数据转换为能够通过传输介质传输的信号'
#     ]},
#     {'网络电缆':[
#         '用来连接网络中的各个设备，供设备之间进行数据通信,常见的网络电缆有双绞线、光纤、电话线'
#     ]},
#     {'网络协议':[
#         '为计算机网络中进行数据交换而建立的规则、标准或约定的集合'
#     ]},
#     {'网络互联的7层框架':[
#         '应用层：为应用程序提供服务并规定应用程序中相关的通信细节',
#         '表示层：主要负责数据格式的转换,确保一个系统的应用层信息可被另一个系统应用层读取' ,
#         '会话层：负责建立和断开通信连接（数据流动的逻辑通路），以及记忆数据的分隔等数据传输相关的管理',
#         '传输层：只在通信双方的节点上（比如计算机终端）进行处理，无须在路由器上处理',
#         '网络层：将数据传输到目标地址，主要负责寻找地址和路由选择，网络层还可以实现拥塞控制、网际互联等功能',
#         '数据链路层：负责物理层面上互连的节点间的通信传输',
#         '物理层：利用传输介质为数据链路层提供物理连接，实现比特流的透明传输'
#     ]},
#     {'':[
#         '应用层：为应用程序提供服务并规定应用程序中相关的通信细节',
#         '传输层：为两台主机上的应用程序提供端到端的通信，提供流量控制、错误控制和确认服务',
#         '网际层：提供独立于硬件的逻辑寻址，从而让数据能够在具有不同的物理结构的子网之间传递,负责寻找地址和路由选择的同时，网络层还可以实现拥塞控制、网际互联等功能',
#         '网络访问层：提供了与物理网络连接的接口。针对传输介质设置数据格式，根据硬件的物理地址实现数据的寻址，对数据在物理网络中的传递提供错误控制。'
#     ]},
#     '网络工具集工具netwox:可以创造任意的TCP、UDP和IP数据报文，以实现网络欺骗',
#     '网络分析工具Wireshark:一个网络包分析工具。该工具主要是用来捕获网络数据包，并自动解析数据包，为用户显示数据包的详细信息，供用户对数据包进行分析'
# ],
# '网络访问层':[
#     '对应OSI七层网络模型的物理层和数据链路层',

#     {'物理层':[
#         '提供传送数据的通路和可靠的环境。对于计算机来说，物理层对应的就是网络适配器'
#     ]},
#     {'数据链路层':[
#         '为网络层提供数据传送服务',
#         '定义了数据传输的起始位置，并且通过一些规则来控制这些数据的传输，以保证数据传输的正确性',
#         {'介质访问控制（Media Access Control, MAC）':[
#             '：提供与网络适配器连接的接口。实际上，网络适配器驱动程序通常被称为MAC驱动，而网卡在工厂固化的硬件地址通常被称为MAC地址'
#         ]},
#         {'逻辑链路控制（Logical Link Control, LLC）':[
#             '这个子层对经过子网传递的帧进行错误检查，并且管理子网上通信设备之间的链路'
#         ]}
#     ]},
#     {'网络体系':[
#         {'构成':[
#             '访问方法：定义了计算机使用传输介质的规则',
#             '数据帧格式：定义了数据传输的格式',
#             '布线类型：定义了网络适配器和其他网络设备的连接方式',
#             '布线规则：定义网络适配器和网络设备连接规范'

#         ]}
#     ]}
# ]

# }

content={
'通信':[
    {'信令':[
        '游走于通信各方之间，用于在通信各方传递指令而非信息内容',
        '如拍插簧、挂机等等过程所产生的电磁信号',
    ]}

],
'':[
    '二进制和布尔代数的结合，很容易使用物理方法实现运算。机器中的存储，都采用电压来表示数字',
    '采用两个范围的电压，不仅能避免外界干扰对数据信息准确性的威胁，还能简化计算机在运用电压进行计算时候的运算规则。',
    '把自然信号变为电磁信号，通过通信网络安全传送到目的地，再还原为自然信号。这就是人类200年通信史研究的基础课题',
    '电磁信号其实就是电压和电流，以及由电压和电流形成的节拍。它们携带的，是原始信息',
    '拍插簧、挂机等等过程所产生的电磁信号，叫做“信令”，他们总是游走于通信各方之间，用于在通信各方传递指令而非信息内容',
    '信令只是交换设备之间，以及交换设备和终端之间进行沟通的传令兵。',
    'IP世界的组成元素可谓琳琅满目。为了便于分析和总结，小周将它们分为节点、管线、管理体系、应用系统等几大类组成部分',
    '局域网中枢——以太网交换机'
]
'':[
    '以太网被设计为总线型结构，一根主线贯穿始末，在主线上“分叉”来连接主机。',
    '路由器是组成IP网络最主要的选路设备。路由器是一个能够让进入其中的、携带原始信息的数据包选择出口道路的盒子',
    '路由器还是一个信息中转站，它能够将不同制式的网络连接在一起。',
    ''
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t11 = t1.addSubTopic()
                t11.setTopicHyperlink(t1.getID()) 
                t11.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTopicHyperlink(t11.getID()) 
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTopicHyperlink(t111.getID()) 
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t11111 = t1111.addSubTopic()
                                                    t11111.setTopicHyperlink(t1111.getID()) 
                                                    t11111.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t111111 = t11111.addSubTopic()
                                                                t111111.setTitle(u)
                                                                for y in p[u]:
                                                                    t1111111 = t111111.addSubTopic()
                                                                    t1111111.setTitle(y)
                                                        else:
                                                            t111111 = t11111.addSubTopic()
                                                            t111111.setTopicHyperlink(t11.getID()) 
                                                            t111111.setTitle(p)                                                        
                                            else:
                                                t11111 = t1111.addSubTopic()
                                                t11111.setTopicHyperlink(t111.getID()) 
                                                t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTopicHyperlink(t111.getID()) 
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTopicHyperlink(t11.getID()) 
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTopicHyperlink(t1.getID()) 
            t11.setTitle(i) 


topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\tcp.xmind") 