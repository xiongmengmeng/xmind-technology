import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TransactionTemplate")
r2=s2.getRootTopic()
r2.setTitle("TransactionTemplate")


content={
'TransactionDefinition':[
    '事务定义'
],
'DefaultTransactionDefinition':[
    '事务定义'
],
'InitializingBean':[
    'afterPropertiesSet()'
],
'TransactionOperations接囗':[
    '执行事务回调方法',
    'T execute(TransactionCallback<T> action)：不带返回值，需自己实现类',
    'void executeWithoutResult(Consumer<TransactionStatus> action)：不带返回值，有现成的实现类'
],
'TransactionTemplate':[
    '事务操作接囗：用来执行事务的回调方法',
    '继承DefaultTransactionDefinition',
    {'实现TransactionOperations接囗，重写execute(TransactionCallback<T> action)方法':[
        {'1.TransactionStatus status = this.transactionManager.getTransaction(this)':[
            '获取事务状态'
        ]},
        {'2.action.doInTransaction(status)':[
            '执行业务逻辑',
            'rollbackOnException(status, ex):应用运行时异常 -> 回滚'
        ]},
        {'3.this.transactionManager.commit(status)':[
            '事务提交'
        ]}
    ]},
    {'实现InitializingBean接囗,重写afterPropertiesSet()方法':[
        '只是校验了事务管理器不为空'
    ]},
],
'总结':[
    'TransactionTemplate还是通过TransactionManager事务管理器来操作事务的',
    '@Transactional是否生效, 取决于是否加载于接口方法, 并且是否通过接口方法调用(而不是本类调用)'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 