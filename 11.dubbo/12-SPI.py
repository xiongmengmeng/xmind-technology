import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SPI(上)")
r2=s2.getRootTopic()
r2.setTitle("SPI(上)")


content={
'作用：让整个框架的接口和具体实现解耦，增强扩展性':[],
'Java SPI':[
    'Service Provider Interface',
    '使用策略模式， 一个接口多种实现',
    '只声明接口，具体的实现不在程序中直接确定，由程序外的配置掌控',
    {'具体步骤':[
        '定义一个接口及对应的方法',
        '编写该接口的一个实现类',
        '在META-INF/services/目录下，创建一个以接口全路径命名的文件，如com.test.spi.PrintService',
        '文件内容为具体实现类的全路径名，如果有多个，则用分行符分隔',
        '在代码中通过java.util.ServiceLoader来加载具体的实现类'
    ]},
    {'使用方式':[
        'ServiceLoad<Driver> loads=ServiceLoad.load(Driver.class)'
    ]}
],
'Dubbo SPI':[
    '只加载配置文件中的类，分成不同的种类缓存在内存，不会立即初始化，性能更好',
    '增加对IoC和AOP支持， 一个扩展可以直接setter注入其他扩展',
    '支持包装扩展类，推荐把通用的抽象逻辑放到包装类中， 实现扩展点的AOP特性'
],
'分类':[
    'Class缓存:Dubbo SPI获取扩展类时，先从缓存读取，如缓存中不存在,加载配置文件，根据配置把Class缓存到内存中，不会直接全部初始化',
    '实例缓存:先从缓存中读取，如缓存中读不到，重新加载并缓存起来'
],
'扩展类的种类':[
    '普通扩展类:配置在SPI配置文件中',
    '包装扩展类（Wrapper类）:这种Wrapper类无具体的实现，只做了通用逻辑的抽象，需要在构造方法中传入一个具体的扩展接口的实现',
    '自适应扩展类（Adaptive类）:运行时，通过传入URL中的某些参数动态确定采用哪个扩展点实现类'
],
'扩展点的特性':[
    '自动包装:Wrapper--类继承Protocol接口，构造函数中注入了一个Protocol类型的参数(装饰器模式)',
    '自动加载：setter方法----某个扩展类是另外一个扩展点类的成员属性，拥有setter方法， 那么框架也会自动注入对应的扩展点实例',
    {'自适应':[
        '@Adaptive注解',
        '可动态通过URL中的参数来确定要使用哪个具体的实现类,从而解决自动加载中的实例注入问题',
        '注解在类上，dubbo不会为该类生成代理类',
        {'dubbo中仅有两个类被adaptive注解':[
            'AdaptiveCompiler',
            'AdaptiveExtensionFactory:表示拓展的加载逻辑由人工编码完成'
        ]},
        '注解在方法上,dubbo为该方法生成代理逻辑'
    ]},
    '自动激活：@Activate注解，可标记对应的扩展点默认被激活启用'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 