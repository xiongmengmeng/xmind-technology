import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("监听器")
r2=s2.getRootTopic()
r2.setTitle("监听器")


content={
'EventMultiCaster':[
    {'功能':[
        '注册着所有的Listener',
        '发布者调用applicationEventPublisher.publishEvent(msg),将事件发送给EventMultiCaster',
        'EventMultiCaster根据事件类型决定转发给那个Listener'
    ]},
    {'1.事件广播器的初始化':[
        'refresh()->initApplicationEventMulticaster()',
        '配置了:反射的机制将其注册成容器的事件广播器',
        '未配置:new SimpleApplicationEventMulticaster(beanFactory);',
        '注册到beanFactory的一级缓存 中'
    ]},
    {'2.注册事件监听器':[
        'refresh()->registerListeners()',
        '将监听器，添加到广播器中，只加了监听器的名字(此处监听器还是BeanDefinition)'
    ]},
    {'3.发布事件':[
        'refresh()->finishRefresh()',
        'getApplicationEventMulticaster().multicastEvent(applicationEvent, eventType)',
        'Spring委托ApplicationEventMulticaster将事件通知给所有的事件监听器'
    ]}
],
'SimpleApplicationEventMulticaster':[
    {'multicastEvent()':[
        {'传参':[
            'final ApplicationEvent event',
            'ResolvableType eventType'
        ]},
        {'1.获得事件匹配的监听器':[
            'getApplicationListeners(event, type))'
        ]},
        {'2.执行监听器的逻辑':[
            {'同步(默认)':[
                'invokeListener(listener, event)'
            ]},
            {'异步':[
                'executor.execute(()->invokeListener(listener, event))',
                {'实现':[
                    '自定义类实现ApplicationEventMulticaster接口',
                    '重写setTaskExecutor(TaskExecutor taskExecutor)方法'
                ]}
            ]}
        ]}
    ]},
    {'invokeListener()':[
        {'传参':[
            'ApplicationListener listener, ApplicationEvent event'
        ]},
        'listener.onApplicationEvent(event)'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 