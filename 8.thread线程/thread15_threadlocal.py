import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ThreadLocal")
r2=s2.getRootTopic()
r2.setTitle("ThreadLocal")


content={


'每个线程有自己的共享变量，解决变量在不同线程间的隔离性':[],
'通过覆盖initialValue()方法具有初始值':[],
'使用类InheritableThreadLocal可在子线路中取得父线程继承下来的值':[],
'应用场景':[
    '变量在线程间隔离而在方法或类间共享的场景',
    '进行事务操作，用于存储线程事务信息',
    '数据库连接，Session会话管理',
    '全链路追踪中的 traceId 或者流程引擎中上下文的传递一般采用ThreadLocal',
    'Spring 事务管理器采用了 ThreadLocal',
    'Spring MVC 的 RequestContextHolder 的实现使用了 ThreadLocal'
],
'源码':[
    '1.每个Thread维护着一个ThreadLocalMap的引用',
    '2.ThreadLocalMap是ThreadLocal的内部类，用Entry（继承的弱引用）来存储数据',
    '3.在Entry内部使用ThreadLocal作为key，我们设置的value作为value',
    '4.ThreadLocal创建的副本是存储在自己的threadLocals中的，也就是自己的ThreadLocalMap',
    '5.ThreadLocalMap的键值为ThreadLocal对象，可以有多个threadLocal变量',
    '6.进行get前，必须先set，否则报空指针异常，也可以初始化一个(重写initialValue()方法)',
    '7.ThreadLocal本身并不存储值，它作为一个key来让线程从ThreadLocalMap获取value',
    '8.通过threadLocalHashCode来标识每一个ThreadLocal的唯一性'
],
'ThreadLocalMap中key要用弱引用':[
    {'现象':[
        '业务代码中使用完ThreadLocal, ThreadLocal ref被回收',
        'threadLocalMap的Entry弱引用了threadLocal',
        '->threadLocal下次GC时被回收'
    ]},
    '弱引用:如对象只存在弱引用，下一次垃圾回收的时必被清理掉',
    '实际：key使用哪种类型引用都无法完全避免内存泄漏',
    '意义：set()、get()、remove()方法时，清理掉key为null的记录',
    {'建议':[
        '尽量在代理中使用try-finally块回收自定义的ThreadLocal变量',
        '尤其在线程池场景下，线程经常被复用，不清理会影响后续业务逻辑和造成内存泄露'
    ]}
]







}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 