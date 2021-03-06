import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SPI(下)")
r2=s2.getRootTopic()
r2.setTitle("SPI(下)")


content={
'扩展点注解':[
    {'@SPI':[
        '用在类、 接口和枚举类上， Dubbo框架中使用在接口上',
        '作用：标记接口是一个Dubbo SPI接口(一个扩展点)，运行时需要通过配置找到具体实现类',
        'Dubbo中很多地方通过get Extension (Class<T> type. String name)来获取扩展点接口的具体实现'
    ]},
    {'©Adaptive':[
        '标记在类、 接口、 枚举类和方法上',
        '方法级别注解在第一次getExtension时，自动生成和编译一个动态的Adaptive类，达到动态实现类的效果'
    ]},
    {'©Activate':[
        '扩展点自动激活注解',
        '标记在类、 接口、 枚举类和方法上',
        '使用在有多个扩展点实现、需根据不同条件被激活的场景中，如Filter需要多个同时激活， 因为每个Filter实现的是不同的功能'
    ]}
],
'ExtensionLoader':[
    '扩展机制的主要逻辑类，卖现了配置的加载、 扩展类缓存、 自适应对象生成等工作',
    '入口getExtension、 getAdaptiveExtension、getActivateExtension三个，分别是获取普通扩展类、获取自适应扩展类、获取自动激活的扩展类',
    {'get Extension (String name)':[
        '类似spring ioc，通过指定名称获得动态代理对象',
        '1.框架读取SPI对应路径下的配置文件，根据配置加载所有扩展类并缓存(不初始化)',
        '2.根据传入的名称初始化对应的扩展类',
        '3.尝试查找符合条件的包装类：包含扩展点的setter方法，包含与扩展点类型相同的构造函数',
        '4.返回对应的扩展类实例'
    ]},
    {'getAdaptiveExtension':[
        '自适应获得动态代理对象',
        '在运行时根据参数决定使用哪个动态代理对象',
        '1.和getExtension一样先加载配置文件',
        '2.生成自适应类的代码字符串',
        '3.获取类加载器和编译器， 并用编译器编译刚才生成的代码字符串',
        '4.返回对应的自适应类实例'
    ]}
],
'ExtensionFactory':[
    '创建ExtensionLoader类',
    {'三个实现':[
        'AdaptiveExtensionFactory:持有所有的具体工厂，getExtension方法遍历它持有的所有工厂，最终还是调用SPI或Spring工厂实现的getExtension方法',
        'SpiExtensionFactory:获取扩展点接口对应的Adaptive实现类',
        'SpringExtensionFactory:把Spring上下文保存到Set集合,遍历集合,根据名字从Spring容器中匹配，如没匹配到，根据类型匹配，如还没匹配到返回null'
    ]}
],
'扩展点动态编译的实现':[
    'Dubbo SPI的自适应特性让整个框架非常灵活，动态编译是自适应特性的基础，因动态生成的自适应类只是字符串，需通过编译才能得到真正的Class',
    '使用反射来动态代理一个类， 但是在性能上和直接编译好的Class有一定的差距',
    'Dubbo SPI通过代码的动态生成， 并配合动态编译器，灵活地在原始类基础上创建新的自适应类',
    {'三种代码编译器':[
        {'Abstractcompiler':[
            {'封装了通用的模板逻辑':[
                '1.通过正则匹配出包路径、类名，再根据包路径、类名拼接出全路径类名',
                '2.尝试通过Class.forName加载该类并返回，防止重复编译。如果类加载器中没有这个类，则进入第3步',
                '3.调用doCompile方法进行编译。这个抽象方法由子类实现',  
            ]}
        ]},
        'JDKCompiler',
        'JavassistCompiler:默认,不断通过正则表达式匹配不同部位的代码， 然后调用Javassist库中的API生成不同部位的代码， 最后得到一个完整的Class对象',
        'AdaptiveCompiler编译器:管理其他Compile,抽象类，无法实例化，在里面封装了通用的模板逻辑'
    ]}
],
'get Extension (Class<T> type,String name)来获取扩展点接口的具体实现':[
    '对传入的Class做校验，判断是否是接口',
    '是否有@SPI注解'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 