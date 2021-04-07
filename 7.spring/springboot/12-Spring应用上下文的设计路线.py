import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Spring应用上下文的设计路线")
r2=s2.getRootTopic()
r2.setTitle("Spring应用上下文的设计路线")


content={
'上下文对容器不仅是扩展关系，更重要是持有关系，上下文是以属性形式持有了容器':[],
'ApplicationContext ':[
    'MessageSource，支持不同的信息源。具备支持国际化的实现，为开发多语言版本的应用提供服务',
    'ResourcePatternResolver，访问数据源。具备了从不同地方得到Bean定义资源的能力，比如：xml，java config，注解等等',
    'ApplicationEventPublisher，发布事件。使应用上下文具备了事件机制。事件机制为Bean声明周期的管理提供了便利'
],
'ConfigurableApplicationContext':[
    'refresh()：IoC容器的初始化过程，标志着IoC容器的正式启动'
],
'AbstractApplicationContext':[
    {'实现refresh()方法':[
        'IoC容器的初始化过程:IoC容器中建立BeanDefinition数据映射',
        {'1.BeanDefinition的Resource定位':[
            '由ResourceLoader通过统一的Resource接口完成',
            {'对于SpringBoot':[
                '包扫描从主类所在的包开始扫描，在refresh容器之前（prepareContext()方法中），会先将主类解析成BeanDefinition',
                '然后在refresh方法中并且是扫描Bean之前，解析主类的BeanDefinition获取basePackage的路径',
                '这样就完成了定位的过程'
            ]}
        ]},
        {'2.BeanDefinition的载入':[
            '把用户定义好的Bean表示成IoC容器内部的数据结构BeanDefinition',
            {'对于SpringBoot':[
                '通过主类找到了basePackage，将该路径拼接成：classpath*:org/springframework/boot/demo/**/*.class的形式',
                '然后PathMatchingResourcePatternResolver的类会将该路径下所有的.class文件都加载进来',
                '遍历判断是不是有@Component注解，如果有，就是要装载的BeanDefinition',
                '注：@Configuration，@Controller，@Service等注解底层都是@Component注解，只不过包装了一层'
            ]}
        ]},
        {'3.注册BeanDefinition':[
            '在IoC容器中将BeanDefinition注入到一个ConcurrentHashMap中，IoC容器就是通过这个HashMap来持有这些BeanDefinition数据的',
            '通过BeanDefinitionRegister接口的实现来完成'
        ]}
    ]
    }
],
'GenericApplicationContext ':[
    '属性DefaultListableBeanFactory beanFactory'
],
'AnnotationConfigServletWebServerApplicationContext':[
    '属性beanFactory是IoC容器(DefaultListableBeanFactory)'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 