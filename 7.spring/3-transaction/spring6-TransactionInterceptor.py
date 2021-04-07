import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TransactionInterceptor")
r2=s2.getRootTopic()
r2.setTitle("TransactionInterceptor")


content={
'Advice接囗':[
    '无方法，只是一个定义'
],
'Interceptor接囗':[
    '无方法，只是一个定义'
],
'MethodInterceptor接囗':[
    '方法：invoke(MethodInvocation invocation)'
],
'TransactionAspectSupport':[
    {'invokeWithinTransaction()方法':[
        '1.TransactionAttribute txAttr=getTransactionAttributeSource().getTransactionAttribute(method, targetClass):获取事务属性',
        '2.TransactionManager tm=determineTransactionManager(txAttr):获取事务管理器',
        {'声明式事务':[
            {'3.createTransactionIfNecessary()':[
                '创建一个事务TransactionInfo',
                'getTransaction()：根据事务属性获取TransactionStatus，调用PlatformTransactionManager.getTransaction()',
                'prepareTransactionInfo()：构造一个TransactionInfo对象，绑定当前线程：ThreadLocal<TransactionInfo>'
            ]},
            {'4.invocation.proceedWithInvocation()':[
                'InvocationCallback是父类的内部回调接口',
                '子类中实现该接口供父类调用',
                '子类TransactionInterceptor中invocation.proceed(),回调方法执行'
            ]},
            {'5.completeTransactionAfterThrowing(txInfo, ex)':[
                '如果遇到异常，事务回滚',
                '最终调用AbstractPlatformTransactionManager的rollback()'
            ]},
            {'6.commitTransactionAfterReturning(txInfo)':[
                '如果没有异常就提交事务',
                '最终调用AbstractPlatformTransactionManager的commit()'
            ]}
        ]}
    ]}
],
'TransactionInterceptor类':[
    {'重写invoke(MethodInvocation invocation)方法':[
        'invokeWithinTransaction():父类已经实现'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 