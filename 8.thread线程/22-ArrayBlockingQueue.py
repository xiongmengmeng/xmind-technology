import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ArrayBlockingQueue")
r2=s2.getRootTopic()
r2.setTitle("ArrayBlockingQueue")


content={
'logback中异步日志模型:多生产者-单消费者模型,使用ArrayBlockingQueue实现':[],
'原理':[
    '使用队列把同步日志打印转换为了异步',
    '业务线程: 调用异步appender将日志任务放入队列',
    '日志线程：使用同步appender进行具体日志打印'
],
'AsyncAppender:实现异步日志的关键':[],
'AsyncAppender':[
    '继承AsyncAppenderBase',
    'ArrayBlockingQueue:有界阻塞队列',
    'queueSize:有界队列元素个数，默认256个',
    'worker:线程，消费者线程',
    'aai:一个appender的装饰器，里面存放同步日志的appender',
    'appenderCount:记录aai里附加的同步appender个数',
    'neverBlock:当队列满时是否阻塞业务线程',
    'discardingThreshold:日志队列空闲元素小于该值，新的某些级别的日志会被丢弃'
],
'start()':[
    '1.使用有界队列ArrayBlockingQueue',
    '2.设置discardingThreshold为队列的1/5'
    '3.消费日志队列的worker线程设置为守护线程，设置线程名称',
    '4.启动线程'
],
'append()':[
    '1.日志级别<=INFO_INT&&队列剩余容量<discardingThreshold,丢弃日志任务',
    '2.neverBlock为false(默认):是调用阻塞队列put方法,否则调用不阻塞的offer方法'
],
'worker的run()':[
    '1.take方法从队列获取一个日志任务，如队列为空线程被阻塞直到队列不为空返回',
    '2.调用AppenderAttachableImpl的aai.appendLoopOnAppenders方法：',
    '循环调用通过addAppender注入的同步日志，appener具体实现把日志打印到磁盘'
],
'注意':[
    'ArrayBlockingQueue需合理队列大小免造成OOM',
    '队列将满或满时，根据具体场景制定抛弃策略以免队满时业务线程被阻塞'
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 