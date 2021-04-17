import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器的初始化过程")
r2=s2.getRootTopic()
r2.setTitle("IoC容器的初始化过程")


content={
'IoC容器中建立BeanDefinition数据映射':[],
 '1.BeanDefinition的Resource定位':[
    '由ResourceLoader通过统一的Resource接口完成',
    {'对于SpringBoot':[
        '包扫描从主类所在的包开始扫描，在refresh容器之前（prepareContext()方法中），会先将主类解析成BeanDefinition',
        '然后在refresh方法中并且是扫描Bean之前，解析主类的BeanDefinition获取basePackage的路径',
        '这样就完成了定位的过程'
    ]},
    {'SpringBoot三种常规定位方式':[
        {'1.主类所在包':[
            {'@Component和@ComponentScan':[
                '@Component标明哪个类被扫描进入Spring IoC容器',
                '@ComponentScan标明采用何种策略去扫描装配Bean',
                '配置项basePackages定义扫描的包名，没有定义的情况下，它只扫描当前包和其子包下的路径'
            ]},
        ]},
        '2.SPI扩展机制实现的自动装配（比如各种starter）',
        '3.@Import注解指定的类',
        {'备ssm的定位方式':[
            '引入XML配置Bean:xml文件+@ImportResource，通过它可以引入对应的XML文件'
        ]}
    ]}
],
'2.BeanDefinition的载入':[
    '把用户定义好的Bean表示成IoC容器内部的数据结构BeanDefinition',
    {'对于SpringBoot':[
        '通过主类找到了basePackage，将该路径拼接成：classpath*:org/springframework/boot/demo/**/*.class的形式',
        '然后PathMatchingResourcePatternResolver的类会将该路径下所有的.class文件都加载进来',
        '遍历判断是不是有@Component注解，如果有，就是要装载的BeanDefinition',
        '注：@Configuration，@Controller，@Service等注解底层都是@Component注解，只不过包装了一层'
    ]}
],
'3.注册BeanDefinition':[
    '通过BeanDefinitionRegister接口的实现来完成',
    '比如DefaultListableBeanFactory 中的beanDefinitionMap属性',
    
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 