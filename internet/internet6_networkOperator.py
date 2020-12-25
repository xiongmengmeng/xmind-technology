import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("networkOperator")
r2=s2.getRootTopic()
r2.setTitle("网络运营商")


content={

'PPP和隧道':[
    {'在以太网上传输PPP消息':[
        'PPP消息无法转换成信号:其协议中没有定义以太网中的报头，FCS，信号的格式',
        'PPPoE:PPP消息装入以太网包进行传输的方式',
        'MAC-PPPoE-PPP'
    ]},
    {'接入网的整体工作过程':[
        '接入路由器中需要配置运营商分配的用户名和密码',
        '接入路由器:根据PPPoE的发现机制来寻找BAS的MAC地址(广播)',
        {'用户认证和下发配置':[
            '用户在计算机上输入用户名和密码',
            '根据用户名和密码生成PPP消息',
            '将PPP消息装入以太网包进行发送',
            '将以太网包转换成光信号发送',
            '接收光信号还原成以太网包',
            '从以太网包中取出PPP消息交给认证模块',
            '将用户名和密码发给认证服务器，校验用户身份’',
            'BAS下发TCP/IP参数到互联网接入路由器的BAS端的端口'
        ]},
        '客户端:开始发送用来访问互联网的网络包',
        {'BAS':[
            '收到用户路由器发送的网络包后，去掉MAC头部和PPPoE头部',
            '用隧道机制将包发送给网络运营商的路由器'
        ]}
    ]},
    'ADSL和FTTH中，用户和BAS间通过电缆/光纤连接，没必要验证用户身份',
    '登录是为了根据用户名来切换运营商'
],
'网络运营商内部':[
    {'POP':[
        'ADSL、FTTH等接入网与用户签约的运营商设备',
        '结构：接入骨干的路由器+交换机+连接用户接入网的路由器',
        '互联网的入口',
        '接入骨干的路由器:需配备转发性能和数据吞吐量高的路由器',
        '连接用户接入网的路由器:需配备大量的端口'
    ]},
    {'连接用户接入网路由器的类型':[
        '一般路由器：专线接入',
        'RAS（路由器）:拔号接入',
        '一般路由器+PPPoE专用BAS:PPPoE',
        '一般路由器+BAS:PPPoA'
    ]},
    {'NOC':[
        '运营商的核心设备',
        '从POP传来的网络包集中到这里，并从这里被转发到离目的地更近的POP或其他的运营商',
        '需配备高性能的路由器'
    ]}
],
'跨越运营商的网络包':[
    {'运营商间的路由信息交换':[
        '转接：将互联网中的路由全部告知对方',
        {'对等':[
            '两个运营商间仅告知与各自网络相关的路由信息',
            '通过IX',
            '直接连接'
        ]},
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 