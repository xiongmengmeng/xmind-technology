import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("")
r2=s2.getRootTopic()
r2.setTitle("")


content={
'CountDownLatch':[
    '使用AQS实现，使用AQS状态变量存放计数器的值',
    {'与join方法的区别':[
        '1.调用子线程的join()方法后，该线程会一直被阻塞直到子线程运行完毕',
        'CountDownLatch使用计数器允许子线程运行完毕或者在运行中递减计数',
        '2.使用线程池来管理线程时,更方便'
    ]},
    {'实现':[
        '在初始化CountDownLatch时设置状态值（计数器值）',
        '多个线程调用countdown方法时实际是原子性递减AQS的状态值',
        '当线程调用await方法后当前线程被放入AQS的阻塞队列',
        '其他线程调用countdown方法计数器值递减1',
        '当计数器值为0，当前线程调用AQS的doReleaseShared方法激活由调用await()方法被阻塞的线程'
    ]},
    {'await()':[
        '委托sync调用了AQS的acquireSharedInterruptibly方法',
        '1.首先判断当前线程是否已被中断，若是抛异常',
        '2.调用sync实现的tryAcquireShared查看计数器值是否为0',
        '是,直接返回',
        '否,调用AQS的doAcquireSharedInterruptibly方法让当前线程阻塞'
    ]},
    {'countDown() ':[
        '委托sync调用了AQS的releaseShared方法',
        '1.调用sync实现的AQS的tryReleaseShared方法:使用CAS将计数器值减1,返回state是否为0',
        '2.如state=0,调用AQS的doReleaseShared方法来激活阻塞的线程'
    ]} 
],
'CyclicBarrier':[
    '通过独占锁ReentrantLock(本质还是AQS)实现计数器原子性更新，并使用条件变量队列来实现线程同步',
    '适合分段任务有序执行的场景,可让一组线程全部达到一个状态后再全部同时执行',
    '回环:当所有等待线程执行完毕，并重置CyclicBarrier的状态后它可以被重用',
    '屏障:线程调用await方法后就会被阻塞，阻塞点称为屏障点，等所有线程都调用了await方法后，线程们就会冲破屏障，继续向下运行',
    {'类图':[
        'parties:记录线程个数，表示多少线程调用await后，所有线程才会冲破屏障继续往下运行',
        'count:一开始等于parties，每当有线程调用await方法就递减1，当count为0时就表示所有线程都到了屏障点',
        '使用两个变量：parties用来记录总的线程个数，当count计数器值变为0后，将parties赋给count，进行复用',
        'barrierCommand:任务'
    ]},
    {'await() ':[
        '1.获取独占锁lock，如parties=10，后面9个调用线程会调用await()方法阻塞',
        '2.第10个线程调用时，执行CyclicBarrier的任务，唤醒其他9个线程，重置CyclicBarrier'
    ]}
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 