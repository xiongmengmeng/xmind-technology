import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程的上下文切换")
r2=s2.getRootTopic()
r2.setTitle("线程的上下文切换")


content={
'线程的上下文切换':[
    {'定义':[
        '一个CPU在一个时刻只能运行一个线程',
        '当其运行一个线程时，由于时间片耗尽或出现阻塞等情况，CPU会转去执行另外一个线程'
    ]},
    '因当前线程的任务可能并没有执行完毕，所以进行切换时需要保存线程的运行状态',
    '以便下次重新切换回来时，继续切换之前的状态运行，这个过程涉及用户态和内核态的切换',
],
'用户态和内核态':[
    {'用户态':[
        '当在执行用户自己的代码时，称其处于用户运行态（用户态）',
        '此时处理器特权级最低，是普通的用户进程运行的特权级，大部分用户直接面对的程序都是运行在用户态',
    ]},
    {'内核态':[
        '当因为系统调用陷入内核代码中执行时，处于内核运行态（内核态）',
        '此时处理器处于特权级最高',
    ]},
    {'切换':[
        '如要执行文件操作、网络数据发送等操作必须通过write、send等系统调用，这些系统调用会调用内核的代码',
        '会从用户态切换到内核态的内核地址空间去执行内核代码来完成相应的操作，在执行完后又会切换回用户态'
    ]}

]




}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 