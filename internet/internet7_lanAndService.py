import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("lanAndService")
r2=s2.getRootTopic()
r2.setTitle("局域网和服务器")


content={
'局域网':[
    {'防火墙':[
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
    ]},
    {'负载均衡':[
        '在DNS服务器中填写多个名称相同的记录，每次查询时DNS服务器按顺序返回不同的IP地址',
        '将域名对应的IP地址设置为负载均衡器的IP地址并注册到DNS服务器上,负载均衡器判断将请求转发给哪台Web服务器'
    ]},
    {'缓存服务器':[
        '一台通过代理机制对数据进行缓存的服务器',
        '代理介于Web服务器和客户端之间，具有对Web服务器访问进行中转的功能',
        '进行中转时，可以将Web服务器返回的数据保存在磁盘中，并代替Web服务器将磁盘中的数据返回给客户端',
        {'3种部署方式':[
            '服务器',
            '客户端：归客户端网络运营管理者所有的，Web服务器的运营者无法控制它',
            '互联网边缘：Web服务器运营者和网络运营商签约，将可以自己控制的缓存服务器放在客户端的运营商处'
        ]}
    ]},
    {'代理':[
        '正向代理',
        '反向代理',
        '透明代理'
    ]}],
'服务器(上)':[
    {'结构':[
        '等待连接模块',
        '负责与客户端通信的模块'
    ]},
    {'过程':[
        '1.服务器程序启动,读取配置文件,完成初始化操作后，会运行等待连接模块',
        '该模块会创建套接字，然后进入等待连接的暂停状态',
        '2.客户端连发起连接时，该模块会恢复运行并接受连接，然后启动客户端通信模块，并移交完成连接的套接字',
        '客户端通信模块会使用已连接的套接字与客户端进行通信，通信结束后，这个模块就退出了',
        '注：每次有新的客户端发起连接，都会启动一个新的客户端通信模块，其与客户端是一对一的关系'
    ]}
],
'服务器（下）':[
    {'服务器程序调用Socket库':[
        {'1 创建套接字（创建套接字阶段）':[
            '<描述符1>=socket()'
        ]},
        {'2.1 将套接字设置为等待连接状态（等待连接阶段）':[
            'bind(<描述符1>,<端囗号>,...)',
            'listen(<描述符1>,...)'
        ]},
        {'2.2 接受连接（接受连接阶段）':[
            '<描述符2>=accept(<描述符1>,...)',
            '客户端包到达->',
            '协议栈给等待连接的套接字复制一个副本->','将连接对象等控制信息写入新的套接字中'
        ]},
        {'3 收发数据（收发阶段）':[
            'read(<描述符2>,<接收缓冲区>,...)',
            'write(<描述符2>,<发送数据>,...)'
        ]},
        {'4 断开管道并删除套接字（断开阶段）':[
            'close(<描述符2>)'
        ]}
    ]},
    {'使用描述符来指代套接字的原因':[
        '等待连接的套接字中没有客户端IP地址和端口号',
        '使用描述符这一种信息比较简单'
    ]},
    {'接收操作':[
        {'1.网卡接收到信号，将其还原成数字信息':[
            '网卡的MAC模块将网络包从信号->数字信息，校验FCS并存入缓冲区',
            '过程中，服务器的CPU并不是一直在监控网络包的到达，因此并不知道此时网络包已经到达',
            '网卡需要通过中断将网络包到达的事件通知CPU',
            'CPU暂停当前的工作，切换到网卡的任务',
            '网卡驱动会根据MAC头部判断协议类型，并将包交给相应的协议栈',
        ]},
        {'2.协议栈的IP模块的接收操作':[
            '判断是不是发给自己的',
            '判断网络包是否经过分片',
            '将包转交给TCP模块或UDP模块'
        ]},
        {'3.1 TCP模块处理连接包':[
            '确认TCP头部的控制位SYN',
            '检查接收方端口号',
            '为相应的等待连接套接字复制一个新的副本',
            '记录发送方IP地址和端口号等信息'
        ]},
        {'3.2 TCP模块处理数据包':[
            '根据收到的包的发送方IP地址、发送方端口号、接收方IP地址、接收方端口号找到相对应的套接字',
            '将数据块拼合起来并保存在接收缓冲区中',
            '向客户端返回ACK'
        ]},
        {'4. TCP模块的断开操作':[
            '服务器:调用Socket库的close,TCP生成一个控制位FIN为1的TCP头部->客户端',
            '客户端:收到包后,调用close，生成一个FIN为1的TCP头部,一个ACK号->服务器',
            '服务器:再返回ACK号',
            '断开操作完成后，套接字会在一段时间后被删除'
        ]}
    ]},
    '解释请求消息并作出响应',
    '浏览器接收响应消息并显示内容']

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 