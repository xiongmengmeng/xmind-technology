import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="分布式"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式事务")
r2=s2.getRootTopic()
r2.setTitle("分布式事务")


content={
'事务':[
    '1.建立连接:从DataSource获得数据库连接',
    '2.开启事务',
    '3.执行方法',
    '4.提交或回滚事务'
],
'分布式事务':[
    '上述1-4过程都在spring中进行管理，不能修改',
    '分布式事务的使用就需要考虑在1前，4后进行',
    {'原理':[
        '在DataSource外建立切面,切getConnection这个方法',
        '创建一个自定义Connection类,它对旧Connection上做封装'
    ]},
    {'1.自定义Connection类':[
        '实现Connection接囗,重写三个方法即可',
        {'事务对象':[
            '事务对象LbTransaction'
        ]},
        {'commit()':[
            '以下内容都为异步实现',
            '1.阻塞，等待别的事务都是可提交状态,继续',
            '2.判断事务对象LbTransaction的状态',
            '3.状态为commit：调用connection.commit()',
            '4.状态为rollback：调用connection.rollback()',
            '5.关闭连接connection.close()'
        ]},
        {'rollback()':[
            'connection.rollback()',
        ]},
        {'close()':[
            '空实现',
        ]},
    ]},
    {'2.定义一个分布式事务的注解':[
        '@LbTransactional'
    ]},
    {'3.事务对象LbTransaction':[
        {'String groupId':[
            '事务组id'
        ]},
        {'String transactionId':[
            '事务id'
        ]},
        {'TransactionType transactionType':[
            '事务状态'
        ]},
    ]}
    {'3.分布式事务的注解的切面':[
        {'通知方法invoke()':[
            '1.创建一个全局事务',
            '2.执行方法',
            {'3.执行结果成功':[
                '是：注册一个分支事务，状态为commit',
                '是：注册一个分支事务，状态为rollback'
            ]}
        ]}
    ]},
    {'4.自定义事务管理器':[
        {'4.1创建事务组，返回groupId':[
            ''
        ]}
        {'4.2注册事务':[
            '参数：注册的事务组ID：grougId，当前事务的状态transactionType',
            '创建一个事务对象LbTransaction',
            '把它放入到本地map中'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 