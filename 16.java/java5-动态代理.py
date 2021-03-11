import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("动态代理")
r2=s2.getRootTopic()
r2.setTitle("动态代理")


content={

'动态代理':[
    '代理类实例在程序运行时，由JVM根据反射机制动态的生成',
    {'过程如下':[
        '代理Class对象',
        '->反射创建代理对象',
        '->调用代理对象的方法'
    ]},
    '思考：Class对象包含了一个类的所有信息，如构造器、方法、字段等,如不写代理类，这些信息从哪获取?接口',
    {'代理类和目标类实现同一组接口':[
        '尽可能保证代理对象的内部结构和目标对象一致',
        '这样对代理对象的操作最终都可以转移到目标对象身上，代理对象只需专注于增强代码的编写'
    ]},
    '优点：代理类可作用于多个目标对象，代理对象和目标对象松耦合',
    {'缺点':[
        '实现比静态代理(代理对象直接持有目标对象的引用)更加复杂',
        '存在一定限制，如要求需代理的对象必须实现某个接口',
        '不够灵活，会为接口中声明的所有方法添加上相同的代理逻辑'
    ]}
],
'java两种代理方式':[
    'JDK动态代理：借助Proxy,InvocationHandler',
    'CGLIB动态代理：借助Enhancer,MethodInterceptor'
],
'学习':[
    'https://www.zhihu.com/question/20794107/answer/658139129',
    'https://baijiahao.baidu.com/s?id=1693196110185594031',
    'https://www.cnblogs.com/liuyun1995/p/8144628.html'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 