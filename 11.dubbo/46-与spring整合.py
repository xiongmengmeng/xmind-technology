import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("与Spring整合")
r2=s2.getRootTopic()
r2.setTitle("与Spring整合")


content={
'@EnableDubbo':[
    '扫描属性文件，将其封装为XXXConfig类',
    '扫描指定包下的类，扫描@Service与@Reference注解，并且进⾏处理',
    '@EnableDubboConfig',
    '@DubboComponentScan'
],
'@EnableDubboConfig':[
    '调⽤DubboConfigConfigurationRegistrar的registerBeanDefinitions⽅法',
    {'作用':[
        '解析properties⽂件内容,组装成BeanDefinition,类型为XXXConfig',
        '注册DubboConfigBindingBeanPostProcessor(⼀个BeanPostProcessor),给bean属性做赋值'
    ]},
    {'总结':[
        '对propties⽂件进⾏解析并根据不同的配置项⽣成对应类型的Bean对象'
    ]}
],
'@DubboComponentScan':[
    {'DubboComponentScanRegistrar':[
        {'向Spring容器中注册两个Bean':[
            'ServiceAnnotationBeanPostProcessor',
            'ReferenceAnnotationBeanPostProcessor'
        ]}
    ]},
],
'ServiceAnnotationBeanPostProcessor':[
    '⼀个BeanFactoryPostProcessor，⽤来注册BeanDefinition',
    {'作⽤':[
        '把被@Service注解的类当做⼀个Dubbo服务，进⾏服务导出',
        {'得到⼀个Spring的Bean':[
            '封装一个BeanDefinition,beanClass属性是具体的服务实现类',
        ]},
        {'得到一个Dubbo的服务':[
            '针对每个BeanDefinition,⽣成⼀个ServiceBean类型的BeanDefinition'
        ]}
    ]},
    {'ServiceBean':[
        {'参数':[
            {'ref':[
                '服务的具体实现类'
            ]},
            {'interface':[
                '服务的接⼝'
            ]},
            {'parameters':[
                '服务的参数（@Service注解中所配置的信息）'
            ]},
            {'application':[
                '服务所属应⽤'
            ]},
            {'protocols':[
                '服务所使⽤的协议'
            ]},
            {'registries':[
                '服务所要注册的注册中⼼'
            ]}
        ]},
        {'实现ApplicationListener接⼝':[
            '当Spring启动完成后会触发onApplicationEvent()⽅法的调⽤',
            '⽅法内会调⽤export()，这个⽅法是服务导出的⼊⼝⽅法'
        ]}
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 