import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("circulDependence(下)")
r2=s2.getRootTopic()
r2.setTitle("circulDependence(下)")


content={
'解决思路分析':[
    {'思路':[
        'A的Bean在创建过程中',
        '1.进行依赖注入前，把A的原始Bean放入缓存（提早暴露）',
        '2.进行依赖注入，此时A的Bean依赖了B的Bean',
        '3.如B的Bean不存在，创建B的Bean:先创建一个B的原始对象，然后把B的原始对象放入缓存',
        '4.如B的原始对象依赖注入A，从缓存中拿到A的原始对象（只是A的原始对象，不是最终Bean）',
        '5.B的原始对象依赖注入完，B的生命周期结束，A的生命周期也结束',
    ]},
    '除了简单Bean，还要考虑进行AOP，最终生成代理的Bean',
    {'AOP':[
        '实现类AnnotationAwareAspectJAutoProxyCreator，父类是AbstractAutoProxyCreator，实现BeanPostProcessor接囗',
        '本质：利用JDK动态代理或CGLib的动态代理',
        '如给一个类中的某个方法设置了切面，这个类最终会生成一个代理对象',
        '过程：A类--->生成一个普通对象-->属性注入-->基于切面生成一个代理对象-->把代理对象放入singletonObjects单例池'
    ]},
    {'实际':[
        {'1.A初始化':[
            '使用反射生成原始Bean',
            '将A的原始Bean放入singletonFactories中(一个map)，key为beanName,value类型为AbstractAutowireCapableBeanFactory',
            '开始依赖注入：populateBean()方法,内部调用getBean()获取B'
        ]},
        '2.B开始初始化,使用反射生成原始Bean',
        {'3.B依赖注入':[
            '1.发现B依赖A，getBean()获取A',
            '2.去singleton缓存中找实例,发现A的bean存在于singletonFactories中,根据beanName得到一个ObjectFactory',
            '3.把bean存放到earlyProxyReferences中(一个map),key为beanName，value为bean',
            '4.执行ObjectFactory.getEarlyBeanReference方法，得到一个A原始对象经过AOP之后的代理对象',
            '5.将bean生成的代理放入earlySingletonObjects中(一个map),key为beanName，value为bean'
        ]},
        '4.B初始化完成',
        {'5.A继续初始化：initializeBean()':[
            '执行AbstractAutoProxyCreator的postProcessAfterInitialization方法',
            '判断当前beanName是否在earlyProxyReferences',
            '如在:已经提前进行过AOP，无需再次进行AOP,从earlySingletonObjects中得到代理对象，然后入singletonObjects中',
            '如不在:进行BeanPostProcessor的执行之后，把A的代理对象放入singletonObjects中',
        ]},
        '6.A初始化完成'
    ]}
],
'https://www.cnblogs.com/lanqingzhou/p/13592190.html':[]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 