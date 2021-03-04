import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("other")
r2=s2.getRootTopic()
r2.setTitle("other")


content={
'DelegatingFilterProxy':[
    '存在与spring-web包中',
    '通过spring容器来管理filter的生命周期',
    '继承GenericFilterBean，间接实现了Filter这个接口，故而该类属于一个过滤器',
    {'init()--GenericFilterBean类实现':[
        '将该类封装成spring特有形式的类，方便spring维护',
        {'调用initFilterBean方法(模版方法)':[
            '1.找到被代理类在spring中配置的id并赋值给targetBeanName',
            '2.使用找到的id从spring容器中找到具体被代理的类，并赋值给delegate'
        ]}
    ]},
    {'doFilter':[
        '1.得到被代理的filter',
        '2.invokeDelegate():执行被代理filter--shiroFilter的doFilter方法'
    ]}
],
'':[
   ''
],
'':[
    ''
],
'学习':[
    'https://zhuanlan.zhihu.com/p/29161098'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 