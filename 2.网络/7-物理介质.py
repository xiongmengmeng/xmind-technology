import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("物理介质")
r2=s2.getRootTopic()
r2.setTitle("物理介质")


content={
'物理介质':[
    '把电脑连接起来的物理手段，常见有双绞线，光纤以及无线电波',
    '决定了电信号(0和1)的传输方式',
    '决定了电信号的传输带宽、速率、传输距离以及抗干扰性等等'
],
'双绞线':[
    '两根信号线的缠绕抵消外源性噪声',
    '节距控制抑制内源性噪声'
],
'集线器':[
    '将信号发送给所有连接在它上面的线路',
    '原封不动将信号广播出去'
],
'交换机':[
    '全双工模式:同时进行发送和接收操作',
    '端口的MAC模块不具有MAC地址,不核对接收方MAC地址',
    {'交换电路':[
        '通过交换开关切换信息流向',
        '交换开关由电子电路构成，可快速切换'
    ]},
    {'过程':[
        '1.信号到达网线接口，由PHY（MAU）模块进行接收',
        '2.PHY（MAU）模块:信号->通用格式，传递给MAC模块',
        '3.MAC模块:信号->数字信息，通过包末尾的FCS校验错误，没问题,包->缓冲区',
        '4.MAC地址表中查询【包的接收方MAC地址】->【端囗】',
        '5.包->交换电路->缓冲区->MAC模块->PHY模块->端口->网线'
    ]},
    {'MAC地址表维护':[
        '收到包:发送方MAC地址，输入端口->写入MAC地址表',
        '过时自动删除地址表中记录'
    ]},
    {'特殊':[
        '交换机发现一个包要发回到原端口，直接丢弃包'
    ]}
],
'路由器':[
    '各个端口都具有MAC和IP地址,只接收与自身地址匹配的包，不匹配直接丢弃',
    {'路由表':[
        '忽略主机号，只匹配网络号',
        {'维护':[
            '手动维护',
            '路由器间的信息交换自行维护'
        ]}
    ]},
    {'转发目标':[
        '路由表',
        '包的IP头部中接收方IP地址',
        '网络号最长，跃点计数较小',
        '网关列为IP地址，该地址为下一个转发目标',
        '网关列为空，IP头部中的接收方IP地址是下一个转发目标',
        '通过ARP来查转发目标的MAC地址'
        '无匹配记录，丢弃包，并通过ICMP消息告知发送方',
        '可设置默认路由'
    ]},
    {'过程':[
        '1.信号->网线接口',
        '2.PHY（MAU）模块和MAC模块:信号->数字信息',
        '3.通过包末尾的FCS进行错误校验:没问题则检查MAC头部中的接收方MAC地址，匹配将包放到缓冲区，否则丢弃',
        '4.通过路由表找到下一路由，更新MAC,IP头部中的TTL,把信号转发出去',
        '5.委托端口模块将包发送出去'
    ]},
    {'分片':[
        '对一个完整的包再进行拆分的过程',
        '条件：长度>输出端口的MTU&&TCP标志字段可分片',
        '不满足：丢弃包，并通过ICMP消息通知发送方'
    ]},
    {'路由器&交换机':[
        'IP （路由器）负责将包发送给通信对象这一整体过程',
        '其中将包传输到下一个路由器的过程则是由以太网（交换机）来负责的'
    ]},
    {'附加功能':[
        '地址转换',
        '包过滤'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 