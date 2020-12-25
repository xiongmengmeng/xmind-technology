# import os,sys 
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
# sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("thread")
r2=s2.getRootTopic()
r2.setTitle("多线程")


content={
'Thread类':[
    '进程:受操作系统管理的基本运行单元,如一个正在操作系统中运行的exe程序'
    '线程：进程中独立运行的子任务，最大限度地利用CPU的空闲时间来处理任务',
    '多线程是异步的',
    {'实现多线程的两种方式':[
        '继承Thread类',
        '实现Runnable接口'
    ]},
    '使用多线程时，代码的运行结果与代码执行顺序或调用顺序无关'
    'start():通知“线程规划器”此线程已准备就绪，等待调用线程对象的run（）方法',
    '非线程安全:多个线程对同一个对象中的同一个实例变量进行操作时会出现值被更改、值不同步的情况，进而影响程序的执行流程',
    'currentThread（）方法可返回代码段正在被哪个线程调用的信息',
    'isAlive（）的功能是判断当前的线程是否处于活动状态,线程处于正在运行或准备开始运行的状态',
    '',
    '',
    ''
    '·线程的启动·如何使线程暂停·如何使线程停止·线程的优先级·线程安全相关的问题'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 