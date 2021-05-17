import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Dubbo协议")
r2=s2.getRootTopic()
r2.setTitle("Dubbo协议")


content={
'构成':[
    {'transporter':[
        'mina,netty,grizzy'
    ]},
    {'serialization':[
        'dubbo,hessian2,java,json'
    ]},
    {'dispatcher':[
        'all,direct,message,execution,connection'
    ]},
    {'threadPool':[
        'fix,cached'
    ]}
],
'特性':[
    {'连接个数':[
        '单连接'
    ]},
    {'连接方式':[
        '长连接'
    ]},
    {'传输协议':[
        'TCP'
    ]},
    {'传输方式':[
        'NIO异步传输'
    ]},
    {'序列化':[
        'Hessian2二进制序列化'
    ]},
    {'适用范围':[
        '传入传出的数据包较小(小于100k)',
        '消费者大于提供者,单一消费者无法压满提供者',
        '尽量不要用dubbo协议传输大文件和大字符串'
    ]},
    {'适用场景':[
        '常规远程服务方法调用'
    ]},
],
'约束':[
    '1.参数，返回值需要实现Serializable接囗',
    '2.参数，返回值不能用自定义的list,map,Date,Number等接囗，只能用jdk自带',
    '3.A->B，SerialId不相同，正常传参',
],
'详细配置':[ 
    '<dubbo:protocol name="dubbo" port="9090"',
    {'服务端,客户端的通用实现':[
        'server="netty" client="netty"'
    ]},
    {'编解码,序列化':[
        'codec="dubbo" serialization="hessian2" charset="utf-8"'
    ]},
    {'线程，队列':[
        'threadPool="fixed" threads="100" queues="0" iothreads="9"'
    ]},
    {'缓存区大小,接受连接数,请求响应数据包的大小指定':[
        'buffer="8192" accepts="1000" payload="8388608"/>'
    ]}
],
'几个问题':[
    {'为什么消费者需比提供者个数多':[
        'dubbo协议采用单一长连接',
        '假如网络为千兆网卡(1024Mbit=128MByte)',
        '每条连接最多只能压满7MByte',
        '理论上1个服务提供者需要20个服务消费者才能压满网卡',
    ]},
    {'为什么不能传输大包':[
        '假设每次请求数据包为500kByte',
        '单服务提供者的最大TPS:128MByte/500kByte=262',
        '单消费调用单个服务提供者的最大TPS:7MByte/500kByte=14',
        '结果：大数据量传输时，消费者调用提供性的并发性降低',
        '如能接受，考虑使用，否则网络会成为瓶颈'
    ]},
    {'为什么采用异步单一长连接':[
        'RPC中，通常提供者少，消费者多',
        '如采用常规hessian服务，提供者容易被压挎',
        {'单一连接':[
            '保证单一消费者不会压死提供者',
        ]}, 
        {'长连接':[
            '减少握手，验证等阶段',
        ]},
        {'异步IO+复用线程池':[
            '防止C10K问题(10000万客户端)'
        ]}
    ]}
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 