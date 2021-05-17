import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HTTP协议")
r2=s2.getRootTopic()
r2.setTitle("HTTP协议")


content={
'介绍':[
    '基于HTTP表单的远程调用协议',
    '采用spring的HttpInvoker实现',
],
'特性':[
    {'连接个数':[
        '多连接'
    ]},
    {'连接方式':[
        '短连接'
    ]},
    {'传输协议':[
        'HTTP'
    ]},
    {'传输方式':[
        '同步传输'
    ]},
    {'序列化':[
        '表单序列化'
    ]},
    {'适用范围':[
        '传入传出参数数据包大小混合',
        '提供者比消费者个数多',
        '暂不支持传文件',
    ]},
    {'适用场景':[
        '需同时给应用程序和浏览器JS使用的服务',
    ]},
],
'约束':[
    '参数，返回值符合Bean规范',
],
'详细配置':[ 
    '<dubbo:protocol name="http" port="9090"/>',
],
'注':[
    '如使用servlet派发请求，协议端囗需与servlet容器端囗相同',
    '协议上下文路径contextpath与servlet应用上下文路径相同'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 