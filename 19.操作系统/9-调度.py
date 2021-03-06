import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="操作系统"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("调度")
r2=s2.getRootTopic()
r2.setTitle("调度")


content={
'调度':[
    '进程或线程来同时竞争CPU 时间片,【调度程序】使用【调度算法】，决定接下来哪个进程/线程可以运行'
],
'调度算法的分类':[
    '不同的环境下需要不同的调度算法',
    {'三种环境':[
        '批处理(Batch) : 商业领域',
        '交互式(Interactive)： 交互式用户环境',
        '实时(Real time)'
    ]},
    {'批处理中的调度':[
        {'先来先服务':[
            '当第一个任务从外部进入系统时，将会立即启动并允许运行任意长的时间(它不会因为运行时间太长而中断)',
            '当其他作业进入时，它们排到就绪队列尾部',
            '当正在运行的进程阻塞，处于等待队列的第一个进程就开始运行',
            '当一个阻塞的进程重新处于就绪态时，它会像一个新到达的任务，会排在队列的末尾，即排在所有进程最后。',
            '单链表可实现，易于理解'
        ]},
        {'最短作业优先':[
            '调度程序总是选择剩余运行时间最短的那个进程运行'
        ]},
    ]},
    {'交互式系统中的调度':[
        {'轮询调度':[
            '每个进程都会被分配一个时间段，称为时间片(quantum)，在这个时间片内允许进程运行',
            '如时间片结束时进程还在运行，则抢占一个CPU并将其分配给另一个进程',
            '如果进程在时间片结束前阻塞或结束，则CPU立即进行切换'
        ]},
        {'优先级调度':[
            '每个进程都被赋予一个优先级，优先级高的进程优先运行'
        ]},
        {'多级队列':[
            '先级类,属于最高优先级的进程运行一个时间片，次高优先级进程运行2个时间片，再下面一级运行4个时间片，以此类推',
            '当一个进程用完分配的时间片后，它被移到下一类'
        ]},
        {'最短进程优先':[
            '根据进程过去的行为进行推测，并执行估计运行时间最短的那一个'
        ]},
        {'保证调度':[
            '在一个有 n 个进程运行的单用户系统中，若所有的进程都等价，则每个进程将获得 1/n 的 CPU 时间'
        ]},
        {'彩票调度':[
            '为进程提供各种系统资源（例如 CPU 时间）的彩票。当做出一个调度决策的时候，就随机抽出一张彩票，拥有彩票的进程将获得该资源',
            '在应用到 CPU 调度时，系统可以每秒持有 50 次抽奖，每个中奖者将获得比如 20 毫秒的 CPU 时间作为奖励。'
        ]},
        {'公平分享调度':[
            '每个用户都会分配一些CPU 时间，而调度程序会选择进程并强制执行'
        ]}
    ]},
    {'实时系统中的调度':[
        {'硬实时(hard real time) ':[
            '必须要满足绝对的截止时间'
        ]},
        {'软实时(soft real time) ':[
            '虽然不希望偶尔错失截止时间，但是可以容忍'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 