import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConfigurationClassParser")
r2=s2.getRootTopic()
r2.setTitle("ConfigurationClassParser")


content={
'作用':[
    '解析配置类、扫描包、注册BeanDefinition'
],
'调用处':[
    {'ConfigurationClassPostProcessor':[
        'postProcessBeanDefinitionRegistry()->processConfigBeanDefinitions()',
        {'processConfigBeanDefinitions()':[
            {'1.创建ConfigurationClassParser':[
                'ConfigurationClassParser parser = new ConfigurationClassParser'
            ]},
            {'2.解析':[
                {'parser.parse(candidates)->processConfigurationClass()':[
                    '递归地处理配置类及其父类层次结构:',
                    'SourceClass sourceClass = asSourceClass(configClass, filter);',
                    '递归处理Bean，如果有父类，递归处理，直到顶层父类:',
                    'doProcessConfigurationClass(configClass, sourceClass, filter);'
                ]}
            ]}
        ]},
    ]}
],
'doProcessConfigurationClass()':[
    {'解析内部类':[
        '配置类上有@Configuration注解，该注解继承 @Component',
        'if 判断为true，调用processMemberClasses方法，递归解析配置类中的内部类'
    ]},
    {'解析@PropertySource':[
        '如果配置类上有@PropertySource注解，则解析加载properties文件，并将属性添加到Spring上下文中'
    ]},
    {'处理@ComponentScan注解':[
        '1.获取配置类上的@ComponentScan注解',
        {'2.循环所有的ComponentScan，立即执行扫描':[
            'this.componentScanParser.parse(componentScan, sourceClass.getMetadata().getClassName())'
        ]},
        {'3.检验获得的BeanDefinition中是否有配置类':[
            '有@Configuration、@Component、@ComponentScan、@Import、@ImportResource和@Bean中的其中一个注解',
            '递归调用parse方法，进行解析'
        ]}
    ]},
    {'解析@Import注解,并加载该注解指定的配置类':[
        'SpringBoot项目中经常用的各种@Enable*** 注解基本都是封装的@Import'
        'processImports(configClass, sourceClass, getImports(sourceClass), true)'
    ]},
    {'解析@ImportResource':[
        '以导入xml配置文件'
    ]},
    {'解析@Bean methods':[
        '将@Bean方法转化为BeanMethod对象，添加到ConfigurationClass#beanMethods集合中'
    ]},
    '@SpringBootApplication注解=@ComponentScan+@EnableAutoConfiguration+@Import+@Configuration+@Component'
],
'ComponentScanAnnotationParser#parse()':[
    {'1.创建一个ClassPathBeanDefinitionScanner对象':[
        'new ClassPathBeanDefinitionScanner()'
    ]},
    {'2.扫描并注册BeanDefinition':[
        'scanner.doScan(StringUtils.toStringArray(basePackages)):',
        {'1.从指定的包中扫描需要装载的Bean':[
            'Set<BeanDefinition> candidates = findCandidateComponents(basePackage)'
        ]},
        {'2.将该Bean注册进IoC容器（beanDefinitionMap）':[
            'registerBeanDefinition(definitionHolder, this.registry)'
        ]},
    ]},
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 