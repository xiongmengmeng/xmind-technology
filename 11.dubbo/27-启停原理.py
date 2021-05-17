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
        {'DubboNamespaceHandler':[
            '把不同的标签关联至解析实现类中'
        ]},
        {'DubboBeanDefinitionParser':[
            '把标签解析成对应的Bean定义并注册到Spring上下文中',
            '同时保证Spring容器中相同id的Bean不会被覆盖'
        ]},
        'Dubbo只做属性提取的事,运行时属性注入和转换都是Spring处理的'
    ]},
    {'注解@EnableDubbo':[
        {'@EnableDubboConfig':[
            "其注解@Import(DubboConfigConfigurationRegistrar.class)",
            {'DubboConfigConfigurationRegistrar':[
                '解析XML文件，加载XXXConfig类'
            ]}
        ]},
        {'@DubboComponentScan':[
            '其注解@Import(DubboComponentScanRegistrar.class)',
            {'DubboComponentScanRegistrar':[
                '注入ServiceAnnotationBeanPostProcessor，ReferenceAnnotationBeanPostProcessor类'
            ]},
            {'ServiceAnnotationBeanPostProcessor':[
                '实现BeanDefinitionRegistryPostProcessor接口',
                '所有Bean注册之后回调postProcessBeanDefinitionRegistry()扫描Service注解并注入容器'
            ]},
            {'ReferenceAnnotationBeanPostProcessor':[
                '实现InstantiationAwareBeanPostProcessor接口',
                'Spring的Bean中初始化前会触发postProcessPropertyValues方法:'
                '1.获取类中标注的Reference注解的字段和方法',
                '2.反射设置字段或方法对应的引用',
                '注：inject方法注入ReferenceBean类(继承自ReferenceConfig,增加了Spring初始化等生命周期方法)',
                '比触发afterPropertiesSet从容器中获取一些配置(protocol)等',
                '当设置字段值的时候仅调用referenceBean.getObject()获取远程代理即可'
            ]}
        ]}
    ]}
],
'优雅停机':[
    '1.收到kill 9进程退出信号，spring容器会触发容器销毁事件',
    '2.provider端会取消注册服务元数据信息',
    '3.consumer端会收到最新地址列表（不包含准备停机的地址）',
    {'4.Dubbo协议会发送readonly事件报文通知consumer服务不可用':[
        '考虑到注册中心推送服务有网络延迟，以及客户端计算服务列表可能占用一些时间',
        'Dubbo协议发送readonly时间报文时，consumer端会设置响应的provider为不可用状态，下次负载均衡就不会调用下线的机器'
    ]},
    '5.服务端等待已经执行的任务结束并拒绝新任务执行'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 