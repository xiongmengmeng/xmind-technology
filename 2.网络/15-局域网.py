import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("局域网")
r2=s2.getRootTopic()
r2.setTitle("局域网")


content={
'防火墙':[
    {'包过滤方式':[
        '根据接收方IP地址',
        '发送方IP地址',
        '接收方端口号',
        '发送方端口号',
        '控制位等信息来判断是否允许某个包通过'
    ]},
    '通过接收方IP地址和发送方IP地址限定流向',
    '通过端口号限定应用程序',
    '通过控制位判断连接方向'
],
'负载均衡':[
    '在DNS服务器中填写多个名称相同的记录，每次查询时DNS服务器按顺序返回不同的IP地址',
    '将域名对应的IP地址设置为负载均衡器的IP地址并注册到DNS服务器上,负载均衡器判断将请求转发给哪台Web服务器'
],
'缓存服务器':[
    '一台通过代理机制对数据进行缓存的服务器',
    '代理介于Web服务器和客户端之间，具有对Web服务器访问进行中转的功能',
    '进行中转时，可以将Web服务器返回的数据保存在磁盘中，并代替Web服务器将磁盘中的数据返回给客户端',
    {'3种部署方式':[
        '服务器',
        '客户端：归客户端网络运营管理者所有的，Web服务器的运营者无法控制它',
        '互联网边缘：Web服务器运营者和网络运营商签约，将可以自己控制的缓存服务器放在客户端的运营商处'
    ]}
],
'代理':[
    '正向代理',
    '反向代理',
    '透明代理'
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 