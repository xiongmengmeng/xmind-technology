import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式锁")
r2=s2.getRootTopic()
r2.setTitle("分布式锁")


content={
'非公平锁':[
    {'1.当前锁是否已有其它事务创建':[
        {'是':[
            '监听当前锁'
        ]},
        {'否':[
            '创建锁',
            '执行完业务逻辑后删除锁'
        ]}
    ]},
    {'问题':[
        '并发问题比较严重时，性能较差',
        '所有连接都对同一个节点进行监听，当服务器检测到删除事件时，要通知所有的连接',
        '所有的连接同时收到事件，再次并发竞争，出现羊群效应'
    ]}  
],
'公平锁':[
    {'实现':[
        '1.在/lock节点下创建一个临时顺序节点',
        {'2.判断自己是否是/lock节点下的最小节点':[
            {'是':[
                '获得锁',
                '执行完业务逻辑后删除锁',
                '后继第一个节点将会收到通知'
            ]},
            {'否':[
                '对前面的节点进行监听'
            ]}
        ]},
    ]},
    {'优点':[
        '借助于临时顺序节点，可避免同时多个节点的并发竞争锁，缓解了服务端压力'
    ]},
    {'问题思考':[
        '最小节点的客户端挂掉，最小节点因为是临时节点，会被删除,后续节点会收到通知',
        '非最小节点的客户端挂掉,下一节点会收到通知，判断自己不是最小节点，会去监听上一节点'
    ]},
    {'实现细节':[
        'lock节点:为容器节点，后续不用再单独去删除',
        '自己不是lock节点下的最小节点，会调用wait()阻塞',
        '前一节点释放锁，在回调方法里调用notifyAll()'
    ]},
    {'redis与zk分布式锁的区别':[
        {'redis':[
            'master-slave主从模式',
            '主节点挂掉，数据还未同步给从节点，主从切换可能导致锁丢失',
            '性能好，但存在丢失锁的问题'
        ]},
        {'zk':[
            'lead-follower的模块',
            '数据要写入到follower才算写入成功，更安全，但性能会差'
        ]}
    ]}
],
'共享锁':[
    {'read请求':[
        '如前面的节点都是读锁，直接获取锁',
        '如前面有写请求，则该读请求不能获得锁，即需对前面的写节点进行监听',
        '如是多个写请求，只对最后的写请求进行监听即可'
    ]},
    {'write请求':[
        '只需对前面的节点进行监听和互斥锁处理机制一样'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 