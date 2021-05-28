import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Protocol")
r2=s2.getRootTopic()
r2.setTitle("Protocol")


content={
'Protocol':[
    '类注解 @SPI("dubbo")',
    {'int getDefaultPort()':[
        '当用户没有设置端口的时候，返回默认的端口'
    ]},
    {'<T> Exporter<T> export(Invoker<T> var1)':[
        '方法注解@Adaptive',
        '把一个服务暴露成远程invocation'
    ]},
    {'<T> Invoker<T> refer(Class<T> var1, URL var2)':[
        '方法注解@Adaptive',
        '引用一个远程服务'
    ]},
    {'void destroy()':[
        '销毁'
    ]}
],
'AbstractProtocol':[
    {'属性':[
        {'Map<String, Exporter<?>> exporterMap':[
            '服务暴露时存放exporter'
        ]}
    ]}
],



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 