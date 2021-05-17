import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Cluster")
r2=s2.getRootTopic()
r2.setTitle("Cluster")


content={
'Cluster':[
    '注解：@SPI("failover")',
    {'<T> Invoker<T> join(Directory<T> var1)':[
        '方法注解@Adaptive'
    ]}
],
'FailoverCluster':[
    {'join(Directory<T> directory)':[
        '通过字典伪装成一个invoker,字典中可能有多个提供者',
        'new FailoverClusterInvoker(directory)'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 