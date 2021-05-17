import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并发控制")
r2=s2.getRootTopic()
r2.setTitle("并发控制")


content={
'组件':[
    'Provider服务提供者',
    'Consumer服务消费者',
    'Registry注册中心',
    'Monitor监控中心'
],
'核心功能':[
    '接囗代理',
    '负载均衡',
    '容错机制',
    'Dubbo协议':[
        'Header(16字节数组)',
        '请求Body/响应Body'
    ]
],
'注册中心(4种)':[
    '注册中心(4种)',
    {'注册中心扩展':[
        'Registry接囗',
        'RegistryFactory接囗'
    ]}

],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 