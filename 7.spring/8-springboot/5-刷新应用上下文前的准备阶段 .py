import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("刷新应用上下文前的准备阶段")
r2=s2.getRootTopic()
r2.setTitle("刷新应用上下文前的准备阶段")


content={
'prepareContext()':[
    {'1.拿到启动类':[
        'Set<Object> sources = getAllSources()'
    ]},
    {'2.将启动类加载到beanDefinitionMap':[
        'load(context, sources.toArray(new Object[0]))',
        {'过程':[
            {'1.创建BeanDefinitionLoader':[
                'createBeanDefinitionLoader(getBeanDefinitionRegistry(context), sources)',
                {'getBeanDefinitionRegistry()':[
                    '将上下文context强转为BeanDefinitionRegistry',
                ]},
            ]},
            {'2.将启动类加载到beanDefinitionMap':[
                'loader.load()',
                '主类按Class加载,封装成AnnotatedGenericBeanDefinition',
                '注册进beanDefinitionMap'
            ]}
        ]}
    ]}
],
'BeanDefinitionRegistry':[
    '方法registerBeanDefinition()：',
    '将BeanDefinition注册进DefaultListableBeanFactory容器的beanDefinitionMap中'
],
'BeanDefinitionLoader':[
    '属性AnnotatedBeanDefinitionReader annotatedReader',
    {'load()':[
        'this.annotatedReader.register(source)'
    ]},
    {'构造方法createBeanDefinitionLoader()':[
        {'注解形式的Bean定义读取器':[
            'this.annotatedReader =new AnnotatedBeanDefinitionReader(registry)'
        ]},
        {'XML形式的Bean定义读取器':[
            'this.xmlReader =new XmlBeanDefinitionReader(registry)'
        ]},
        {'类路径扫描器':[
            'this.scanner =new ClassPathBeanDefinitionScanner(registry)'
        ]}
    ]}
],
'AnnotatedBeanDefinitionReader':[
    {'register()':[
        '->registerBean(componentClass)->doRegisterBean():',
        {'1.将beanClass封装为BeanDefinition':[
            'new AnnotatedGenericBeanDefinition(beanClass)'
        ]},
        {'2.将BeanDefinition注册到beanDefinitionMap':[
            'BeanDefinitionReaderUtils.registerBeanDefinition(definitionHolder, this.registry)->',
            'registry.registerBeanDefinition(beanName, definitionHolder.getBeanDefinition())->',
            'DefaultListableBeanFactory.registerBeanDefinition()->',
            'this.beanDefinitionMap.put(beanName, beanDefinition)'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 