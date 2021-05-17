import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("RMI协议")
r2=s2.getRootTopic()
r2.setTitle("RMI协议")


content={
'介绍':[
    'JDK标准的java.rmi.*实现',
    '采用【阻塞式的短连接】+【JDK标准序列化方式】',
],
'特性':[
    {'连接个数':[
        '多连接'
    ]},
    {'连接方式':[
        '短连接'
    ]},
    {'传输协议':[
        'TCP'
    ]},
    {'传输方式':[
        '同步传输'
    ]},
    {'序列化':[
        'JAVA标准二进制序列化'
    ]},
    {'适用范围':[
        '传入传出参数数据包大小混合',
        '消费者与提供者个数差不多',
        '可传文件',
    ]},
    {'适用场景':[
        '常规远程服务方法调用',
        '与原生RMI服务相互操作'
    ]},
],
'服务接囗定义':[
    '服务接囗继承"java.rmi.Remote"接口,可与原生RMI相互操作',
    {'服务接囗没有继承"java.rmi.Remote"接口':[
        '1.缺少Dubbo自动生成一个"com.xxx.XxxService$Remote"的接囗',
        '并继承"java.rmi.Remote"接口，并以此接囗暴露服务',
        '2.如设置<dubbo:protocol name="rmi" codec="spring"/>',
        '将不生成"$Remote"接囗,而使用spring的"RmilnvocationHandler"接囗暴露服务'
    ]}
],
'约束':[
    '1.参数，返回值需要实现Serializable接囗',
    '2.参数，返回值不能用自定义的list,map,Date,Number等接囗，只能用jdk自带',
    '3.A->B，SerialId不相同，正常值参',
],
'详细配置':[ 
    '<dubbo:protocol name="rmi" port="9090"/>',
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 