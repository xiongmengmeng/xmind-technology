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
'三个组件':[
    '事件',
    '事件监听器',
    '事件广播器'
],
'Spring内置事件':[
    {'ContextRefreshedEvent':[
        '当容器被实例化或refreshed时发布'
    ]},
    {'ContextStartedEvent':[
        '当容器启动时发布,即调用start()方法'
    ]},
    {'ContextStoppedEvent':[
        '当容器停止时发布,即调用stop()方法'
    ]},
    {'ContextClosedEvent':[
        '当容器关闭时发布,即调用close方法'
    ]},
    {'RequestHandledEvent':[
        '在使用spring的DispatcherServlet时有效,当一个请求被处理完成时发布'
    ]},
],
'实现':[
    {'自定义事件':[
        '继承ApplicationEvent',
        '构造方法需要super'
    ]},
    {'2.自定义事件监听器':[
        {'基于接口':[
            '实现ApplicationListener接口，这是个泛型接口，泛型类类型就是事件类型',
            'spring容器托管的bean，所以这里加了@component',
            '重写onApplicationEvent()方法'
        ]},
        {'基于注解':[
            '@EventListener(XXXEvent.class),加在方法上',
            '方法onApplicationEvent(XXXEvent event)'
        ]}
    ]},
    {'3.事件发布操作':[
        'applicationContext.publishEvent(new HelloEvent(this,"lgb"))',
    ]}
],
'注意':[
    '1. 同样的事件能有多个监听器',
    '2. 事件监听器不一定要写一个类去实现，注解@EventListener，修饰在方法上也可以',
    '3. 事件监听操作和发布事件的操作是同步的，如果有事务，监听操作也在事务内',
    '4. 事件监听操作和发布事件的操作可以异步'
],
'事件原理':[
    '观察者模式',
    {'三部分':[
        {'事件（ApplicationEvent)':[
            '负责对应相应监听器',
            '事件源发生某事件是特定事件监听器被触发的原因'
        ]},
        {'监听器(ApplicationListener)':[
            '对应于观察者模式中的观察者',
            '监听器监听特定事件,并在内部定义了事件发生后的响应逻辑'
        ]},
        {'事件发布器（ApplicationEventMulticaster）':[
            '对应于观察者模式中的被观察者/主题,负责通知观察者',
            {'作用':[
                '1.对外提供发布事件和增删事件监听器的接口',
                '2.维护事件和事件监听器之间的映射关系',
                '3.在事件发生时负责通知相关监听器'
            ]}
        ]},
    ]},
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 