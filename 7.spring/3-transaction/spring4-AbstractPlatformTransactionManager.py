import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("AbstractPlatformTransactionManager")
r2=s2.getRootTopic()
r2.setTitle("AbstractPlatformTransactionManager")


content={
'getTransaction()方法':[
    '1.isExistingTransaction()判断是否存在事务',
    '2.当前已存在事务,根据不同传播机制不同处理',
    {'handleExistingTransaction()':[
        '1.NERVER：不支持当前事务;如当前事务存在，抛出异常',
        '2.NOT_SUPPORTED：不支持当前事务，现有同步将被挂起:suspend()',
        '3.REQUIRES_NEW挂起当前事务，创建新事务:',
        '   1)suspend()',
        '   2)doBegin()',
        '4.NESTED嵌套事务:',
        '   1）非JTA事务：createAndHoldSavepoint()创建JDBC3.0保存点，不需要同步',
        '   2) JTA事务：开启新事务，doBegin()+prepareSynchronization()需要同步'
    ]},
    '3.当前不存在事务: 不同传播机制不同处理',
    {'细节':[
        {'suspend()':[
            '1.存在同步,事务不为空，挂起事务doSuspend(transaction),解除绑定当前事务各种属性',
            '2.没有同步，事务不为空，挂起事务',
            '3.没有同步，事务为空，什么都不用做'
        ]},
        {'DataSourceTransactionManager':[
            {'doSuspend(transaction)':[
                '1.把当前事务的connectionHolder数据库连接持有者清空',
                '2.当前线程解绑datasource.其实就是ThreadLocal移除对应变量'
            ]},
            {'doBegin()':[
                '1.DataSourceTransactionObject“数据源事务对象”，设置ConnectionHolder，再给ConnectionHolder设置各种属性：自动提交、超时、事务开启、隔离级别',
                '2.给当前线程绑定一个线程本地变量，key=DataSource数据源  v=ConnectionHolder数据库连接'
            ]}

        ]}
    ]}
],
'commit(TransactionStatus status)':[
    '1.如果事务明确标记为本地回滚，-》执行回滚',
    '2.如果不需要全局回滚时提交 且 全局回滚-》执行回滚',
    '3.提交事务，核心方法processCommit()',
    {'processCommit()':[
        '有6个核心操作，分别是3个前置操作，3个后置操作',
        '1.prepareForCommit(status);源码是空的，没有拓展目前',
        '2.triggerBeforeCommit(status); 提交前触发操作',
        '遍历事务同步器，把每个事务同步器都执行“提交前”操作，如jdbc事务，SqlSessionUtils.beforeCommit()->this.holder.getSqlSession().commit(),提交会话',
        '3.triggerBeforeCompletion(status);完成前触发操作',
        '如果是jdbc事务，那么最终就是，SqlSessionUtils.beforeCompletion->',
        'TransactionSynchronizationManager.unbindResource(sessionFactory),解绑当前线程的会话工厂',
        'this.holder.getSqlSession().close();关闭会话',
        '4.triggerAfterCommit(status);提交事务后触发操作',
        '5. triggerAfterCompletion(status, TransactionSynchronization.STATUS_COMMITTED)',
        '对于JDBC事务来说',
        '1）如果会话任然活着，关闭会话',
        '2）重置各种属性',
        '6.cleanupAfterCompletion(status)',
        '1）设置事务状态为已完成',
        '2) 如果是新的事务同步，解绑当前线程绑定的数据库资源，重置数据库连接',
        '3）如果存在挂起的事务（嵌套事务），唤醒挂起的老事务的各种资源：数据库资源、同步器'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 