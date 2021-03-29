import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("事务")
r2=s2.getRootTopic()
r2.setTitle("事务")


content={
'Spring 的事务传播行为有哪些':[
    '1.REQUIRED：Spring 默认的事务传播级别，如果上下文中已经存在事务，就加入到事务中执行，如果当前上下文中不存在事务，新建事务执行',
    '2.REQUIRES_NEW：每次都会新建一个事务，如果上下文中有事务，则将上下文的事务挂起，当新建事务执行完成以后，上下文事务再恢复执行',
    '3.SUPPORTS：如果上下文存在事务，则加入到事务执行，如果没有事务，则使用非事务的方式执行',
    '4.MANDATORY：上下文中必须要存在事务，否则会抛出异常',
    '5.NOT_SUPPORTED ：如果上下文中存在事务，则挂起事务，执行当前逻辑，结束后恢复上下文的事务',
    '6.NEVER：上下文中不能存在事务，否则就会抛出异常',
    '7.NESTED：嵌套事务。如果上下文中存在事务，则嵌套事务执行，如果不存在事务，则新建事务'
],
'Spring 的事务隔离级别':[
    'Spring 的事务隔离级别底层其实是基于数据库的，Spring 并没有自己的一套隔离级别',
    'DEFAULT：使用数据库的默认隔离级别',
    'READ_UNCOMMITTED：读未提交，最低的隔离级别，会读取到其他事务还未提交的内容，存在脏读',
    'READ_COMMITTED：读已提交，读取到的内容都是已经提交的，可以解决脏读，但是存在不可重复读',
    'REPEATABLE_READ：可重复读，在一个事务中多次读取时看到相同的内容，可以解决不可重复读，但是存在幻读',
    'SERIALIZABLE：串行化，最高的隔离级别，对于同一行记录，写会加写锁，读会加读锁'
],
'Spring 的事务隔离级别是如何做到和数据库不一致的':[
    'Spring 的事务隔离级别本质上还是通过数据库来控制的，具体是在执行事务前先执行命令修改数据库隔离级别',
],
'Spring 事务的实现原理':[
    '使用的技术：AOP（动态代理） + ThreadLocal + try/catch',
    '动态代理：基本所有要进行逻辑增强的地方都会用到动态代理，AOP 底层也是通过动态代理实现',
    'ThreadLocal：主要用于线程间的资源隔离，以此实现不同线程可以使用不同的数据源、隔离级别等等',
    'try/catch：最终是执行 commit 还是 rollback，是根据业务逻辑处理是否抛出异常来决定'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 