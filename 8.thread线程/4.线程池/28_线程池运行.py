import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程池-运行")
r2=s2.getRootTopic()
r2.setTitle("线程池-运行")


content={
'线程池状态':[
    {'RUNNING':[
        '接受新任务并且处理阻塞队列里的任务'
    ]},
    {'STOP':[
        '中断正在处理的任务,拒绝新任务并且抛弃阻塞队列里的任务'
    ]},
    {'TIDYING':[
        '所有任务都执行完（包含阻塞队列的）,线程池活动线程数为0，调用terminated方法'
    ]},
    {'TERMINATED':[
        '终止状态,terminated方法调用完成以后的状态'
    ]},
    {'转换':[
        'RUNNING -> SHUTDOWN:显式调用shutdown()，或隐式调用finalize()里的shutdown()',
        'RUNNING或SHUTDOWN-> STOP:显式调用shutdownNow()时',
        'SHUTDOWN -> TIDYING:当线程池和任务队列都为空时',
        'STOP -> TIDYING:当线程池为空时',
        'TIDYING -> TERMINATED:当terminated()执行完成时'
    ]}
],
'工作线程Worker-runWorker':[
    '1.task==null或者调用getTask从任务队列获取的任务返回null,跳3',
    {'2.执行任务':[
        '2.1获取工作线程内持有的独占锁',
        '2.2执行扩展接口代码',
        '2.3执行任务',
        '2.4任务执行完毕后做一些事情',
        '2.5统计当前Worker完成了多少个任务',
        '2.6释放锁'
    ]},
    {'3.执行清理任务':[
        {'统计信息':[
            '加全局锁',
            '统计线程池完成任务个数',
            '把当前工作线程中完成任务累加到全局计数器',
            '然后从工作集中删除当前Worker',
            '释放锁'
        ]},
        '尝试设置线程池状态为TERMINATED',
        '判断当前线程池里面线程个数<核心线程个数，如果是则新增一个线程',
    ]}
],
'用处':[
    '1.执行大量异步任务时提供更好的性能:线程的创建和销毁需要开销,线程池里线程可复用',
    '2.提供一种资源限制和管理的手段，如可限制线程的个数，动态新增线程等',
    'Executors:工具类，有很多静态方法，根据用户选择返回不同的线程池实例'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 