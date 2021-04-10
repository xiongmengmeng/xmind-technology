import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程安全实现方法")
r2=s2.getRootTopic()
r2.setTitle("线程安全实现方法")


content={
'互斥同步':[
    {'同步':[
        '多线程并发访问，保证共享数据在同一时刻只被一条线程使用',
        {'互斥':[
            '实现同步的一种手段，如：临界区、互斥量和信号量'
        ]}
    ]},
    {'synchronized':[
        '块结构的同步语法',
    ]},
    {'java.util.concurrent.locks.Lock':[
        'ReentrantLock:重入锁',
        'RedissonLock:分布式锁'
    ]}
],
'非阻塞同步':[
    {'基于冲突检测的乐观并发策略':[
        '不需把线程阻塞挂起，直接操作',
        {'共享数据未被争用':[
            '操作直接成功'
        ]},
        {'共享数据被争用：':[
            '进行其他的补偿措施(不断重试)'
        ]},
        '操作和冲突检测两个步骤需要具备原子性'
    ]},
    {'处理器指令':[
        '测试并设置（Test-and-Set）',
        '获取并增加（Fetch-and-Increment）',
        '交换（Swap）',
        '比较并交换（Compare-and-Swap，CAS）',
        '加载链接/条件储存'
    ]}
],
'无同步方案':[
    '同步与线程安全没有必然联系',
    '方法不涉及共享数据,代码线程安全',
    {'可重入代码':[
        '方法返回结果可预测，输入相同数据，均返回相同结果'
    ]},
    {'线程本地存储':[
        '代码中所需数据须与其他代码共享，试下共享数据的代码维护在一个线程',
        {'消费队列':[
            '消息消费过程限制在一个线程中'
        ]},
        {'Web交互模型':[
            '一个请求对应一个服务器线程'
        ]},
        {'java.lang.ThreadLocal类':[
            '实现线程本地存储功能'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 