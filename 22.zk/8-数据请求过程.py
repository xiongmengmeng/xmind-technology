import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据请求过程")
r2=s2.getRootTopic()
r2.setTitle("数据请求过程")


content={
'客户端':[
    '将请求封装放入outgoingQueue队列,然后线程等待',
    {'线程sendTread':[
        '1.跟服务端建立NIO连接',
        {'2.连接建立后监听读写事件并处理':[
            {'读事件':[
                '将其放到waitingEvents队列',
                '如有监听，将watch加入到path对应的watch集合中去',
                'notifyAll()'
            ]},
            {'写事件':[
                '从outgoingQueue队列中取出写事件，将其发送到服务器'
            ]}
        ]}
    ]},
    {'线程EventTread':[
        '从waitingEvents队列拿到数据进行处理'
    ]}
],
'服务端leader':[
    {'初始化时':[
        '封装一条处理器链'
    ]},
    {'请求依次经过如下处理器链':[
        {'ProposalRequestProcessor':[
            '给所有follower发送proposal',
            '将请求放入queuedPackets队列中',
            'LearnerHander线程会将请求发送到服务端的follower'
        ]},
        {'SyncRequestProcessor':[
            '将数据存储到本机数据文件',
            '将请求放入queuedRequests队列中',
            'SyncRequestProcessor线程会将数据存储到本机数据文件'
        ]},
        {'AckRequestProcessor':[
            '处理ack',
            '将请求放入ackSets中',
            'LearnerHander线程会判断是否接收到过半的ack',
            '是，发送commit给所有follower，同步消息给observer',
            'notifyall()通知CommitProcessor'
        ]},
        {'CommitProcessor':[
            '从queuedRequests队列拿出请求，交给ToBeAppliedRequestProcessor',
            '它再把请求往后传，交给FinalRequestProcessor'
        ]},
        {'FinalRequestProcessor':[
            '写内存数据+加监听+删除监听+节点变动，通知客户端',
            '从watchTable.remove(path)'
        ]}
    ]}
],

'服务端follower':[
    {'初始化时':[
        '封装一条处理器链,与leader不同'
    ]},
    {'请求依次经过如下处理器链':[
        'SyncRequestProcessor',
        'SendAckRequestProcessor',
        'CommitProcessor',
        'FinalRequestProcessor'
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 