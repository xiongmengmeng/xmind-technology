import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("应用层")
r2=s2.getRootTopic()
r2.setTitle("应用层")


content={
'作用':[
    '定义数据格式，并按照对应的格式解读数据'
],
'使用协议':[
    'HTTP、FTP、SMTP(规范数据格式)'
],
'具体':[
    '在 Resquest Headers 中，Accept 表示客户端期望接收的数据格式',
    '服务端处理完请求后，按照客户端要求的格式返回',
    '客户端收到结果后，按照服务端返回的格式进行解析'
],
'HTTP请求消息':[
    {'URL解析':[
        '访问数据源机制（协议）+web服务器名+文件路径名',
        '协议类型：http,ftp,mailto，file'
    ]},
    {'请求消息':[
        '第一行：请求方式 请求地址 协议',
        '第二行：消息头',
        '空行',
        '消息体',
    ]},
    {'响应消息':[
        '第一行：状态码和响应短语',
        '...'
    ]}
],
'客户端发送消息':[
    {'1.创建套接字阶段':[
        '调用Socket库中socket程序组件,协议栈返回一个描述符'
    ]},
    {'2.连接阶段':[
        '调用Socket库中connect程序组件',
        '需指定描述符、服务器IP地址和端口号这3个参数',
        '描述符：应用程序用来识别套接字的机制',
        'IP地址和端口号:客户端和服务器之间识别对方套接字的机制'
    ]},
    {'3.通信阶段（收发数据）':[
        '发送消息：调用Socket库中write程序组件',
        '需指定描述符和发送数据',
        '接收消息：调用Socket库中的read程序组件'
    ]},
    {'4.断开阶段':[
        '调用Socket库中的close程序组件',
        'Web服务器会首先调用close来断开连接',
        '浏览器调用read得知收发数据已结束，也会调用close进入断开阶段',
        '一段时间后删除套接字'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 