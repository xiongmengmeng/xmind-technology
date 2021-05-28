import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Directory")
r2=s2.getRootTopic()
r2.setTitle("Directory")


content={
'Node接口':[
    'URL getUrl()',
    'boolean isAvailable()',
    'void destroy()'
],
'Directory<T>接口':[
    'Class<T> getInterface()',
    'List<Invoker<T>> list(Invocation var1)'
],
'AbstractDirectory<T>':[
    '封装了通用逻辑',
    '主要实现四个方法:检测Invoker是否可用,销毁所有Invoker,list方法,doList模版方法',
    {'属性':[
        {'List<Router> routers':[
            '路由'
        ]},
    ]},
    {'list(Invocation invocation)':[
        {'1.获取所有Invoker列表':[
            'List<Invoker<T>> invokers = this.doList(invocation)'
        ]},
        {'2.调用router进行路由，获得符合路由规则的invoker':[
            'invokers=router.route(invokers, this.getConsumerUrl(), invocation)'
        ]}
    ]},
    {'doList(Invocation var1)':[
        '模版方法,返回所有的Invoker列表'
    ]}
],
'NotifyListener':[
    'notify(List<URL> var1)'
],
'StaticDirectory':[
    'Directory的静态列表实现',
    '传入的Invoker列表封装成静态的Directory对象，里面的列表不会改变'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 