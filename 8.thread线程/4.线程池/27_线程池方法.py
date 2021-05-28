import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程池_方法")
r2=s2.getRootTopic()
r2.setTitle("线程池_方法")


content={
'execute(Runnable command)':[
    {'1.线程总个数<corePoolSize，向workers里新增一个核心线程执行任务':[
        'c = ctl.get()'
        '如workerCountOf(c) < corePoolSize',
        '执行addWorker(command, true)'
    ]},
    {'2.线程池线程个数>=corePoolSize,向队列中添加任务':[
        {'判断线程池状态':[
            {'线程池状态为RUNNING，添加当前任务到任务队列':[
                'isRunning(c)&&workQueue.offer(command)'
            ]},
            {'二次检查线程池状态':[
                'RUNNING:当前线程池里是否有线程，没有则新增一个',
                '不是RUNNING:把任务从队列移除，执行拒绝策略'
            ]},
            {'非RUNNING:抛弃新任务':[
                'remove(command)+reject(command)'
            ]}
        ]},
    ]},
    {'3.尝试开启线程执行该任务':[
        '如线程池线程个数>maximumPoolSize,开启线程执行该任务',
        'if (!addWorker(command, false))'
    ]},
    {'4.执行拒绝策略(3尝试失败)':[
        'reject(command)'
    ]},
    '注:一个任务只可能有1-4中的一种情况'
], 
'addWorker(Runnable firstTask, boolean core)':[
    '新增线程',
    {'1.创建工作线程':[
        'Worker w = new Worker(firstTask)'
    ]},
    {'2.加全局锁':[
        'mainLock.lock()'
    ]},
    {'3.将工作线程添加到工作线程集合中':[
        'workers.add(w)'
    ]},
    {'4.释放锁':[
        'mainLock.unlock()'
    ]}
],
'processWorkerExit(Worker w, boolean completedAbruptly)':[
    {'1.加全局锁':[
        'ReentrantLock mainLock = this.mainLock',
        'mainLock.lock()'
    ]},
    {'2.统计线程池完成任务个数':[
        'completedTaskCount += w.completedTasks'
    ]},
    {'3.从工作集中删除当前Worker':[
        'workers.remove(w)'
    ]},
    {'4.释放锁':[
        'mainLock.unlock()'
    ]},
    {'5.尝试设置线程池状态为TERMINATED':[
        'tryTerminate()'
    ]},
    {'6.判断当前线程池里面线程个数<核心线程个数，如果是则新增一个线程':[
        'addWorker(null, false)'
    ]}
],
'shutdown()':[
    '检查权限',
    {'设置当前线程池状态为STOP':[
        '如当前线程池状态>=SHUTDOWN直接返回',
        '否则设置为SHUTDOWN状态'
    ]},
    {'设置所有空闲线程的中断标志':[
        '加全局锁，同时只有一个线程可调用shutdown方法设置中断标志',
        '尝试获取Worker自己的锁，获取成功则设置中断标志',
        '由于正在执行的任务已经获取了锁，所以正在执行的任务没有被中断',
        '中断的是阻塞到getTask()方法并企图从队列里面获取任务的线程，也就是空闲线程'
    ]}
],
'shutdownNow()':[
    '检查权限',
    '设置当前线程池状态为STOP',
    '中断所有的工作线程(包含空闲线程和正在执行任务的线程)',
    '返回值为这时候队列里面被丢弃的任务列表'
],
'awaitTermination()':[
    '获取独占锁，然后在无限循环内判断当前线程池状态是否至少是TERMINATED状态',
    '是,直接返回',
    '否,说明线程池里还有线程在执行，看超时时间nanos是否小于0，是说明不需要等待，直接返回',
    '大于0调用条件变量termination的awaitNanos方法等待nanos时间'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 