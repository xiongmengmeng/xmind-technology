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

'作用':[
    '数据隔离',
    '每个线程有自己的共享变量，解决变量在不同线程间的隔离性'
],
'代码':[
    '通过覆盖initialValue()方法具有初始值',
    '使用类InheritableThreadLocal可在子线路中取得父线程继承下来的值'
],
'应用场景':[
    '2.SimpleDateFormat()的使用，它是线程不安全的，需要做数据隔离',
    '2.shiro中的subject中，存储在Threadlocal，方便随时获取'
    '3.切换数据源',
    '4.全链路追踪中的traceId',
    '5.Spring采用Threadlocal的方式，保证单个线程中的数据库操作使用的是同一个数据库连接',
    '6.Spring MVC的 equestContextHolder的实现使用了ThreadLocal'
],
'源码':[
    '1.每个Thread维护着一个threadLocals变量,指向ThreadLocalMap',
    '2.ThreadLocalMap是ThreadLocal的内部类，用Entry（继承弱引用）来存储数据',
    '3.在Entry内部使用ThreadLocal作为key，我们设置的值作为value',
    '4.进行get前，必须先set，否则报空指针异常，也可以初始化一个(重写initialValue()方法)',
    '5.ThreadLocal本身并不存储值，它作为一个key来让线程从ThreadLocalMap获取value',
    '6.通过threadLocalHashCode来标识每一个ThreadLocal的唯一性',
    {'本质':[
        '每个线程创建ThreadLocal时，实际是存在自己线程的threadLocals变量里'
    ]}
],
'ThreadLocalMap底层结构':[
    '用Entry（继承弱引用）来存储数据(数组结构)',
    {'不用链表怎么解决Hash冲突,set()':[
        '1.计算hash值，判断位置为i',
        '2.如位置是空的，初始化一个Entry对象放在位置i上',
        '3.如位置i不为空，如Entry对象的key正好是即将设置的key，刷新Entry中的value',
        '4.如位置i不为空，而key不等于entry，找下一个空位置，直到为空为止'
    ]},
    {'get()':[
        '根据ThreadLocal对象的hash值，定位到table中的位置',
        '判断该位置Entry对象中的key是否和get的key一致，如不一致，就判断下一个位置'
    ]}
],
'ThreadLocalMap中key为什么要用弱引用':[
    {'弱引用':[
        '如对象只存在弱引用，下一次垃圾回收的时必被清理掉',
        '实际：key使用哪种类型引用都无法完全避免内存泄漏'
    ]},
    'ThreadLocal的不足，可以通过看看netty的fastThreadLocal来弥补',
    {'现象':[
        '业务代码中使用完ThreadLocal, ThreadLocal ref被回收',
        'threadLocalMap的Entry弱引用了threadLocal,threadLocal下次GC时被回收',
    ]},
    {'代码优化':[
        'set()、get()、remove()方法时，清理掉key为null的记录'
    ]},
    {'建议':[
        '尽量在代码中使用try-finally块回收自定义的ThreadLocal变量',
        '尤其在线程池场景下，线程经常被复用，不清理会影响后续业务逻辑和造成内存泄露'
    ]}
]







}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 