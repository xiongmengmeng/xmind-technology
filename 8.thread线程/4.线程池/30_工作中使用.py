import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("工作中使用")
r2=s2.getRootTopic()
r2.setTitle("工作中使用")


content={
'使用场景':[
    '消费消息时',
    '计算时效时',
],
'使用':[
    'new ThreadPoolExecutor(4,4,2, TimeUnit.MINUTES,new LinkedBlockingDeque<Runnable>())',
],
'CompletableFuture使用':[
    {'1.异步执行任务':[
        'CompletableFuture.supplyAsync(() -> task(start, o), executor)'
    ]},
    {'2.将任务放在流中，得集合List<CompletableFuture<T>>':[
        'List<CompletableFuture<Long>> completableFutureList = taskList.stream()',
        '       .map(o -> CompletableFuture.supplyAsync(() -> task(start, o), executor))',
        '        .collect(Collectors.toList());',
    ]},
    {'3.将2中集合放在一个CompletableFuture中':[
        'CompletableFuture<Void> allOf = CompletableFuture.allOf(completableFutureList.toArray(new CompletableFuture[0]));'
    ]},
    {'4.阻塞':[
        'allOf.join();'
    ]},
    {'5.遍历2中集合,处理实际的业务逻辑':[

    ]}
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 