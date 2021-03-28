import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="操作系统"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("写时复制")
r2=s2.getRootTopic()
r2.setTitle("写时复制")


content={
'fork()函数 ':[
    '创建进程：产生一个和父进程完全相同的子进程(除了pid)',
    'fork创建出的子进程，与父进程共享内存空间(不用复制，直接引用父进程的物理空间)',
    '当父子进程中有更改相应段的行为发生时，再为子进程相应的段分配物理空间',
    ''
],
'exec()函数':[
    '一组函数的统称, 它包括了execl()、execlp()、execv()、execle()、execve()、execvp()',
    '作用：装载一个新的程序（可执行映像）覆盖当前进程内存空间中的映像，从而执行不同的任务',
    '注：exec系列函数在执行时会直接替换掉当前进程的地址空间(清空原有的数据)'
],
'Copy On Write':[
    {'技术实现原理':[
        'fork()之后，父进程中所有的内存页的权限都被设为read-only，然后子进程的地址空间指向父进程',
        '当父子进程都只读内存时，相安无事',
        '当其中某个进程写内存时，CPU硬件检测到内存页是read-only的，于是触发页异常中断（page-fault），陷入一个中断例程',
        '中断例程中，会把触发异常的页复制一份，于是父子进程各自持有独立的一份'
    ]},
    {'好处':[
        '减少分配和复制大量资源时带来的瞬间延时',
        '减少不必要的资源分配。如fork进程时，并不是所有的页面都需复制，父进程的代码段和只读数据段都不被允许修改，所以无需复制'
    ]},
    {'缺点':[
        '如fork()后，父子进程继续进行写操作，会产生大量的分页错误(页异常中断page-fault)'
    ]},
    {'总结':[
        '总结',
        'fork出的子进程共享父进程的物理空间，当父子进程有内存写入操作，read-only内存页发生中断，触发异常的内存页复制一份(其余的页还是共享父进程的)',
        'fork出的子进程功能实现和父进程一样,如有需要，用exec()把当前进程映像替换成新的进程文件，完成想要实现的功能'
    ]}
],
'Redis的COW':[
    'Redis在持久化时，如果是采用BGSAVE命令或者BGREWRITEAOF的方式，那Redis会fork出一个子进程来读取数据，从而写到磁盘中',
    '总体Redis读操作较多，如子进程存在期间，发生了大量写操作，会出现很多的分页错误(页异常中断page-fault)，耗费不少性能在复制上',
    'rehash阶段，写操作无法避免,所以Redis在fork出子进程后，将负载因子阈值提高，尽量减少写操作，避免不必要的内存写入操作'
],
'Java':[
    {'CopyOnWriteArrayList':[
        '定义了一个可重入锁:ReentrantLock ',
        '对修改集合的方法 (add, remove 等) 进行同步',
        '在进行实际修改操作时, 会先复制原来的数组, 再进行修改, 最后替换原来的',
        '缺点：弱一致性'
    ]},
    {'CopyOnWriteArraySet':[
        '基于CopyOnWriteArrayList的, 其内部维护了一个CopyOnWriteArrayList实例al ',
        '操作都被委托给 al,典型的【组合模式】应用'
    ]},
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 