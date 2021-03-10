import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("启停原理")
r2=s2.getRootTopic()
r2.setTitle("启停原理")


content={
'配置解析':[
    {'基于XML配置原理解析':[
        'DubboNamespaceHandler主要把不同的标签关联至解析实现类中',
        'DubboBeanDefinitionParser实现:把标签解析成对应的Bean定义并注册到Spring ±下文中， 同时保证了 Spring容器中相同id的Bean不会被覆盖',
        'Dubbo只做了属性提取的事情， 运行时属性注入和转换都是Spring处理的'
    ]}
    {'注解->@EnableDubbo':[
        '@EnableDubboConfig->DubboConfigConfigurationSelector',
        {'@DubboComponentScan':[
            '->DubboComponentScanRegistrar:',
            {'ServiceAnnotationBeanPostProcessor':[
                '实现了 BeanDefinitionRegistryPostProcessor接口',
                'Spring容器中所有Bean注册之后回调postProcessBeanDefinitionRegistry方法开始扫描旧Service注解并注入容器'
            ]},
            {'ReferenceAnnotationBeanPostProcessor':[
                '1.获取类中标注的^Reference注解的字段和方法',
                '2.反射设置字段或方法对应的引用'
            ]}
        ]}
    ]}
],
'服务暴露实现原理':[
    '1.基于dubbo.jar内的Meta-inf/spring.handlers配置，spring在遇到dubbo名称空间时，会回调DubboNamespaceHandler类',
    '2.所有的dubbo标签，都统一用DubboBeanDefinitionParser进行解析，基于一对一属性映射，将XML标签解析为Bean对象',
    '服务暴露的入口点在ServiceConfig#export',
    '3.将Bean对象转会为url格式，将所以Bean属性转成url的参数,',
    '4.将URL传给Protocol扩展点，基于扩展点的Adaptive机制，根据URL的协议头，进行不同协议的服务暴露和引用',
    {'向注册中心暴露服务':[
        'RegistryProtocol#export',
        '将export参数中的提供者URL先注册到注册中心，再重新传给Protocol扩展点进行暴露',
        '1.委托具体协议(Dubbo)进行服务暴露， 创建NettyServer监听端口和保存服务实例',
        '2.创建注册中心对象， 与注册中心创建TCP连接',
        '3.注册服务元数据到注册中心',
        '4.订阅configurators节点， 监听服务动态属性变更事件',
        '5.服务销毁收尾工作， 比如关闭端口、 反注册服务信息等'
    ]}
],
'服务消费':[
    {'实现原理':[
        '',
        '服务引用的入口点在ReferenceBean#getObject'
    ]}
    '',
    ''
],
'优雅停机':[
    '1.pring容器会触发容器销毁事件',
    '2.provider端会取消注册服务元数据信息',
    '3.consumer端会收到最新地址列表（不包含准备停机的地址）',
    '4.Dubbo协议会发送readonly事件报文通知consumer服务不可用',
    '5.服务端等待已经执行的任务结束并拒绝新任务执行'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 