import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("thread")
r2=s2.getRootTopic()
r2.setTitle("Thread类")


content={
'Thread类':[
    {'方法':[
        'start():通知"线程规划器"此线程已准备就绪，等待调用线程对象的run()方法',
        'currentThread():代码段正在被哪个线程调用',
        'isAlive():当前线程是否处于活动状态(正在运行或准备开始运行)',
        'sleep():在指定毫秒数内让"正在执行的线程(this.currentThread())"休眠',
        'getId():线程唯一标识',
        'suspend():暂停线程,resume():恢复线程执行',
        'yield():放弃当前的CPU资源(放弃的时间不确定)',
        'setPriority():设置线程优先级,有继承性',
        {'线程停止':[
            '1.抛异常',
            '2.使用退出标志，线程正常退出:run方法完成后线程终止',
            '3.stop():强行终止(不推荐),可能产生不可预料结果',
            '4.interrupt+return:在当前线程中打了一个停止标记，并不是真的停止线程',
            'interrupted():判断当前线程是否中断，执行后将状态标志为清除',
            'isInterrupted():判断当前线程是否中断，不清除状态标志'
        ]}
    ]},
    {'分类':[
        '用户线程',
        '守护线程(Daemon):典型---垃圾回收线程'
    ]},
    {'线程的6种状态':[
        '状态枚举：Thread.State',
        {'NEW':[
            '尚未启动的线程，未执行start()'
        ]},
        {'RUNNABLE':[
            '正在java虚拟机中执行的线程'
        ]},
        {'BLOCKED':[
            '受阻塞，等待某个监视器锁的线程'
        ]},
        {'WAITING':[
            '无限期等待另一线程来执行某一特定操作'
        ]},
        {'TIMED_WAITING':[
            '有限期等待另一线程来执行某一特定操作'
        ]},
        {'TERMINATED':[
            '已退出'
        ]}
    ]},
    {'线程组':[
        '线程组中可以有线程对象，也可以有线程组',
        '作用:批量管理线程或线程组对象'
    ]},
    {'SimpleDateFormat非线程安全,解决方式':[
        '1.建了多个SimpleDateFormat类的实例',
        '2.ThreadLocal类能使线程绑定到指定的对象'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 