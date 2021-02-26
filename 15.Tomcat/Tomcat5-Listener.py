import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("监听器")
r2=s2.getRootTopic()
r2.setTitle("监听器")


content={
'监听器6+2':[
    {'6个常规监听器':[
        '三类，对应JavaWeb三大域对：ServletContext、HttpSession、ServletRequest',
        '生命周期监听器，就是监听三大域对象的创建和销毁',
        '属性监听器则专门监听三大域对象get/setAttribute()',
        {'ServletContext--对应JavaWeb域对象ServletContext':[
            'ServletContextListener（生命周期监听）',
            'ServletContextAttributeListener（属性监听）'
        ]},
        {'HttpSession':[
            'HttpSessionListener（生命周期监听）',
            'HttpSessionAttributeListener（属性监听）'
        ]},
        {'ServletRequest':[
            'ServletRequestListener（生命周期监听）',
            'ServletRequestAttributeListener（属性监听）'
        ]},
    ]},
    {'2个感知监听':[
        'HttpSessionBindingListener',
        'HttpSessionActivationListener'
    ]},
],
'三大生命周期监听器，各自在何时创建、销毁，顺序是怎么样的':[
    '1.在项目启动时ServletContextListener监听到ServletContext对象创建',
    '2.每一次请求Tomcat都会创建一个Request，它的创建会被ServletRequestListener监听到',
    '3.如果Servlet中调用了request.getSession()，则Tomcat会创建Session（如果根据JSESSIONID找不到对应的），这会被HttpSessionListener监听到',
    '4.请求结束，Request销毁，被监听到',
    '5.用户30分钟未访问，Session过期销毁，被监听到',
    '6.项目关停，ServletContext销毁，被监听到'
],
'观察者模式':[
    '被监听对象',
    '监听器对象',
    '事件',
    {'过程':[
        '1.注册监听器，把自己与监听对象关联',
        '2.被监听对象发生特定行为，传入Event对象，触发监听器对象的doXX()方法'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 