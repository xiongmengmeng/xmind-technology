import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("过期删除机制")
r2=s2.getRootTopic()
r2.setTitle("过期删除机制")


content={
'三种':[
    {'定时过期':[
        '每个设置过期时间的key需创建一个定时器，过期立即清除，占用cpu'
    ]},
    {'惰性过期':[
        '访问key时，判断key是否过期，过期则清除,占用内存'
    ]},
    {'定期过期':[
        '每秒执行N次删除(可配置)',
        '每次随机抽取100个key，当有25%的数据超时时，继续抽取，直到25%以下',
        '每次执行时长确定为250ms/N，时间一到如果还没执行完就停下，下次继续'
    ]}
],
'Redis中同时使用了惰性过期和定期过期两种过期策略':[],
'RDB对过期键的处理':[
    {'生成RDB文件':[
        '过滤过期的键'
    ]},
    {'载入RDB文件':[
        '如服务器以主服务器模式运行,过期的键会被过滤',
    ]}
],
'AOF对过期键的处理':[
    {'AOF文件写入':[
        '当过期键被惰性或定期删除后，程序向AOF文件追加一个DEL命令，显式记录该键已被删除'
    ]},
    {'AOF重写':[
        '过滤过期的键',
    ]}
],
'复制对过期键的处理':[
    '主服务器删除一个过期键后，会显示向所有从服务器发送一个DEL命令，告知从服务器删除这个过期键',
    '有客户端向从服务器发送命令GET message,虽键过期，但依旧可返回'
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 