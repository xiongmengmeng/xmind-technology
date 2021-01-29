import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TransactionInterceptor")
r2=s2.getRootTopic()
r2.setTitle("TransactionInterceptor")


content={
'继承自TransactionAspectSupport类（该类包含与Spring的底层事务API的集成），实现了MethodInterceptor接口':[],
'实现了MethodInterceptor接口,重写invoke()方法':[
    '调用了父类TransactionAspectSupport的invokeWithinTransaction()方法:',
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
],
'ReflectiveMethodInvocation':[
    '执行业务方法',
    '父类ProxyMethodInvocation->MethodInvocation->Invocation->Joinpoint',
    {'Joinpoint':[
        '连接点接口',
        '定义了执行接口：Object proceed() throws Throwable;',
        '执行当前连接点，并跳到拦截器链上的下一个拦截器'
    ]},
    {'Invocation':[
        '调用接口，继承自Joinpoint',
        '定义了获取参数接口： Object[] getArguments()',
        '是一个带参数的、可被拦截器拦截的连接点'
    ]},
    {'MethodInvocation':[
        '方法调用接口，继承自Invocation',
        '定义了获取方法接口：Method getMethod()',
        '是一个带参数的可被拦截的连接点方法'
    ]},
    {'ProxyMethodInvocation':[
        '代理方法调用接口，继承自MethodInvocation',
        '定义了获取代理对象接口：Object getProxy()',
        '一个由代理类执行的方法调用连接点方法'
    ]},
    {'ReflectiveMethodInvocation':[
        '实现了ProxyMethodInvocation接口，自然就实现了父类接口的的所有接口',
        '获取代理类，获取方法，获取参数，用代理类执行这个方法并且自动跳到下一个连接点'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 