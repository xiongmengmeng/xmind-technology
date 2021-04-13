import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Bean基础内容")
r2=s2.getRootTopic()
r2.setTitle("Bean基础内容")


content={
'Bean生命周期(4部分)':[
    'Bean定义',
    'Bean的初始化',
    'Bean的生存期',
    'Bean的销毁'
],
'Bean定义':[
    'BeanDefinition：表示Bean，描述Bean的配置信息',
    {'BeanDefinitionRegistry接囗：':[
        '定义对BeanDefinition的各种增删改操作:',
        '注册（registerBeanDefinition）',
        '消除注册（removeBeanDefinition）',
        '获取注册（getBeanDefinition）',
        '查看是否有此注册（containsBeanDefinition）',
        '获取所有的名称（getBeanDefinitionNames）',
        '获取名片的个数（getBeanDefinitionCount）'
    ]},
    {'实现类SimpleBeanDefinitionRegistry':[
        '属性：Map<String, BeanDefinition> beanDefinitionMap',
        '方法registerBeanDefinition：将BeanDefinition>加到beanDefinitionMap中'
    ]}
],
'Bean作用域':[
    'Singleton:所有spring应用，默认值，Ioc容器只存在单例',
    'Prototype:所有spring应用，每当从Ioc容器中取出一个Bean，则创建一个新的Bean',
    'request:spring web应用，web工程单次这一次(request)',
    'session:spring web应用，HTTP会话',
    'application:spring web应用，web工程生命周期',
    'globalSession:spring web应用，不常用'
],
'Bean初始化流程':[
    '1.资源定位:通过@ComponentScan扫描路径找到带有@Component的类',
    '2.Bean定义:找到资源，开始解析，将信息保存到BeanDefinition实例中(此时没有初始化Bean，没有Bean实例)',
    '3.发布Bean定义：IoC容器加载Bean定义，此时，IoC容器只有Bean定义，Bean实例还未生成',
    '4.实例化:创建Bean的实例对象',
    '5.依赖注入：如@Autowired注入的各种资源',
    '注：ComponentScan中有配置项lazyInit，默认值false(不延迟实例化和依赖注入)'
],
'Bean初始化流程,详细':[
    '1.初始化',
    '2.依赖注入',
    '3.setBeanName方法：接囗BeanNameAware',
    '4.setBeanFactory方法：接囗BeanFactoryAware',
    '5.setApplicationContext方法：接囗ApplicationContextAware(需容器实现ApplicationContext接囗)',
    '6.postProcessBeforeInitialization方法：BeanPostProcessor的预初始化方法(注：针对全部Bean生效)',
    '7.自定义初始化方法：@PostConstruct标方法',
    '8.afterPropertiesSet方法：接囗InitializingBean',
    '9.postProcessAfterInitialization方法：BeanPostProcessor的后初始化方法(注：针对全部Bean生效)',
    '10.生存期',
    '11.自定义销毁方法：@PreDestroy标注方法',
    '12.destroy方法：接囗DisposableBean'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 