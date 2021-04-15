import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="操作系统"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程")
r2=s2.getRootTopic()
r2.setTitle("线程")


content={
'线程':[
    {'多线程':[
        '共享同一块地址空间和所有可用数据',
        '这是进程所不具备的'
    ]},
    {'比进程更轻量级':[
        '比进程更容易创建和撤销,在许多系统中，创建一个线程要比创建一个进程快10-100倍'
    ]},
    {'性能':[
        '如多个线程都是CPU密集型的，并不能获得性能上的增强',
        '但如存在着大量的计算和大量的I/O处理，会加快应用程序的执行速度'
    ]}
],
'线程系统调用':[
    '从当前的某个单线程开始，线程通过调用一个库函数(如thread_create)创建新的线程',
    '当一个线程完成工作后，通过调用一个函数(如thread_exit)来退出,紧接着线程消失，状态变为终止，不能再进行调度'
],
'线程实现(三种)':[
    {'在用户空间中实现线程':[
        '把整个线程包放在用户空间中，内核不知道线程的存在',
        {'通用结构':[
            '线程在【运行时系统】之上运行，运行时系统是管理线程过程的集合',
            {'四个过程':[
                'pthread_create',
                'pthread_exit',
                'pthread_join',
                'pthread_yield'
            ]}
        ]}
    ]},
    {'在内核空间中实现线程':[
        '当某个线程希望创建一个新线程或撤销一个已有线程时，会进行一个系统调用',
        '这个系统调用通过对【线程表】的更新来完成线程创建或销毁工作',
        {'内核中的线程表':[
            '有每个线程的寄存器、状态和其他信息'
        ]}
    ]},
    {'在用户和内核空间中混合实现线程':[
        '编程人员可以自由控制用户线程和内核线程的数量，具有很大的灵活度',
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 