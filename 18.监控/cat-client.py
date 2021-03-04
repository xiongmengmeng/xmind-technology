import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="cat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("cat-client")
r2=s2.getRootTopic()
r2.setTitle("cat-client")


content={
'与srpingBoot整合':[
    '1.pom.xml引入相映jar',
    '2.src/main/resources/META-INF/文件夹下添加app.properties，加上domain配置，如：app.name=tms-service'
    '3.引入CatFilter,springBoot通过FilterRegistrationBean引入',
    '4.日志文件logback.xml引入cat',
    {'5.使用':[
        'Transaction transaction = Cat.newTransaction("DAO", proxyMethodId);',
        '业务代码',
        'transaction.setStatus(Transaction.SUCCESS);',
        'transaction.complete();'
    ]}
],
'Transaction t=Cat.newTransaction("logTransaction", "logTransaction");':[
    '客户端plexusIOC容器的初始化，cat-client的加载初始化、启动了四个daemon线程，并返回了Transaction对象',
    '内部调用Cat.getProducer().newTransaction(type, name)',
    {'1.getProducer()->checkAndInitialize()':[
        '检查客户端配置是否加载完毕,没有做初始化加载',
        '加载文件plexus.xml，完成IOC容器的初始化',
        {'启动这四个daemon线程':[
            'cat-StatusUpdateTask 用来每秒钟上报客户端基本信息（JVM等信息）',
            'cat-merge-atomic-task(消息合并检查)',
            'cat-TcpSocketSender-ChannelManager（NIO 连接服务端检查）',
            'cat-TcpSocketSender（消息发送服务端）'
        ]}
    ]},
    {'2.MessageProducer.newTransaction()':[
        '实现类DefaultMessageProducer',
        '2.1构造一个Context对象，并将其放入ThreadLocal中,用来构造消息',
        {'Context类':[
            'DefaultMessageManager包私有的内部类',
            'MessageTree m_tree:线程的消息体，构造成树',
            'Stack<Transaction> m_stack,多个嵌套消息体填充的栈',
            '每个线程通过使用ThreadLocal构造一个Context对象并存储'
        ]},
        {'2.2.m_manager.start(transaction, false)':[
            'MessageManager.start(),实现类DefaultMessageManager',
            '把消息(transaction)放在tree上，如果有嵌套结构，后边继续在tree上添枝加叶',
            '如果context还没有过消息,将消息放入m_stack中'
        ]}
    ]}
],
'transaction.complete()':[
    '将消息放入一个队列中，从而保证异步上报',
    {'DefaultMessageManager.flush()':[
        'MessageSender sender = m_transportManager.getSender();',
        'sender.send(tree):消息体放入了阻塞队列中等待上传',
        'reset():ThreadLocal中存储的Context清理'
    ]}
],
'TcpSocketSender':[
    'MessageQueue m_atomicTrees = new DefaultMessageQueue(SIZE)',
    '通信上报服务端使用了Netty-Client，并且自定义了消息协议',
    '监听消费队列，并消费（上传服务端）'
],
'总结':[
    '收集进来按照时间以及类型构造为Tree结构->',
    '在compele()方法中将这个构造的消息放入一个内存队列中->',
    '等待TcpSockekSender这个Daemon线程异步上报给服务端'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 