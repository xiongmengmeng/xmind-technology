import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TransactionTemplate")
r2=s2.getRootTopic()
r2.setTitle("TransactionTemplate")


content={
'介绍':[
    '继承DefaultTransactionDefinition',
    '实现TransactionOperations',
    '实现InitializingBean'
],
'TransactionOperations':[
    '事务操作接囗：用来执行事务的回调方法',
    {'使用模版模式':[
        'T execute(TransactionCallback<T> action)：不带返回值，需自己实现类',
        'void executeWithoutResult(Consumer<TransactionStatus> action)：不带返回值，有现成的实现类'
    ]},
    {'TransactionTemplate重写execute(TransactionCallback<T> action)方法':[
        '1.TransactionStatus status = this.transactionManager.getTransaction(this):获取事务状态',
        '2.action.doInTransaction(status):执行业务逻辑',
        'rollbackOnException(status, ex):应用运行时异常 -> 回滚',
        '3.this.transactionManager.commit(status):事务提交'
    ]},
],
'InitializingBean':[
    {'TransactionTemplate重写afterPropertiesSet()方法':[
        '只是校验了事务管理器不为空'
    ]},
],
'DefaultTransactionDefinition':[
    '事务定义',
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 