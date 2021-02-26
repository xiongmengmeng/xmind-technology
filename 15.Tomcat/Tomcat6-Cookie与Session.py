import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Cookie与Session")
r2=s2.getRootTopic()
r2.setTitle("Cookie与Session")


content={
'会话机制':[
   '前因：客户端与服务器的通讯是通过HTTP协议，而HTTP是一种无状态协议',
   '目的:对HTTP无状态协议的一种扩展，帮助服务器记住客户端状态（标识用户，跟踪状态）',
],
'会话':[
    '为了唯一标识一个用户并记录其状态',
    '当服务器无法断定客户端时，一次会话就结束',
    {'服务器无法断定一个客户端的两种情况':[
        '服务器不行了（session失效）',
        '客户端不行了（cookie失效）'
    ]},
    {'会话跟踪常用的有两种技术':[
        'Cookie和Session，且Session底层依赖于Cookie'
    ]}
],
'Cookie':[
    '服务器响应给客户端，并且存储在客户端的一份小数据',
    '客户端再次访问服务器时，会自动带上这个Cookie',
    '服务器通过Cookie区分客户端',
    {'一次会话':[
        '1.浏览器输入URL,向服务器发起请求',
        '2.Servlet内部：response.addCookie(new Cookie("",""))',
        '3.Tomcat会从Response对象中取出相关信息,Set-Cookie响应头，向浏览器发送HTTP响应',
        '4.浏览器接收到响应头后，会把它们作为Cookie文件存在客户端',
        '4.浏览器接再次向服务器发送请求，会带上Cookie'
    ]},
    {'两种类型':[
        {'会话Cookie (Session Cookie)':[
            '不设置MaxAge，默认',
            'Cookie存在于浏览器的内存',
            'Cookie随浏览器关闭而消失'
        ]},
        {'持久性Cookie (Persistent Cookie)':[
            '设置MaxAge>0',
            'Cookie存在电脑硬盘的特定文件夹下（浏览器自定义的）'
        ]},
        {'注意':[
            '设置Cookie的MaxAge=0，会删除已经存在客户端的此Cookie',
            '对于每种浏览器，不管是会话Cookie还是持久性Cookie，Cookie都是相对独立的'
        ]}
    ]}
],
'Session':[
    '服务端的东西,本质上类似一个大Map，内容以键值对的形式存储',
    {'Session序列化':[
        '以Tomcat为例',
        '服务器关闭时，服务器的Session会被保存在work目录的对应项目下',
        '服务器重启时，该SESSIONS.ser文件会被重新读取，读取后文件会从磁盘消失'
    ]},
    {'Session的钝化和活化':[
        '需在Tomcat的conf目录下的context.xml中配置',
        '默认不钝化',
        {'钝化':[
            '一个Session长时间不活动，被序列化到磁盘中',
            '每个Session单独一个文件，而不是SESSIONS.ser'
        ]},
        {'活化':[
            '当该Session再次被访问时，才会被反序列化',
            '即使Session活化回到内存，磁盘的文件也不消失'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 