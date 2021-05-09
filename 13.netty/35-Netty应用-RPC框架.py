import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("netty应用--RPC框架")
r2=s2.getRootTopic()
r2.setTitle("netty应用--RPC框架")


content={
'RPC':[
    'Remote Procedure Call----远程过程调用',
    '一个计算机通信协议',
    '协议允许运行于一台计算机的程序调用另一台计算机的子程序，而程序员无需额外地为这个交互作用编程'
],
'常见RPC框架':[
    '阿里的Dubbo',
    'Apache的thrift',
    'Spring Cloud'
],
'PRC调用流程说明':[
    '1) 服务消费方(client)以本地调用方式调用服务',
    '2) client stub 接收到调用后负责将方法、参数等封装成能够进行网络传输的消息体',
    '3) client stub 将消息进行编码并发送到服务端',
    '4) server stub 收到消息后进行解码',
    '5) server stub 根据解码结果调用本地的服务',
    '6) 本地服务执行并将结果返回给 server stub',
    '7) server stub 将返回导入结果进行编码并发送至消费方',
    '8) client stub 接收到消息并进行解码',
    '9) 服务消费方(client)得到结果',
    {'小结':[
        'RPC的目标将2-8步骤封装起来，用户无需关心这些细节，可以像调用本地方法一样完成远程服务调用'
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 