import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("反射")
r2=s2.getRootTopic()
r2.setTitle("反射")


content={
'ClassLoader':[
    {'Class<?> loadClass(String name, boolean resolve)':[
        '1.Class<?> c = findLoadedClass(name):检查是否已经加载该类',
        '2.c = parent.loadClass(name, false):如果尚未加载，遵循父优先加载机制，加载.class文件',
        '3.c = findClass(name):模板方法模式：如果还是没有加载成功，调用findClass()'
    ]}
],
'Class类':[
    'class文件已经被类加载器加载到内存中，并且JVM根据其字节数组创建了对应的Class对象',
    {'构造器':[
        '私有的，我们无法手动new一个Class对象，只能由JVM创建',
        'JVM在构造Class对象时，需要传入一个类加载器，然后才有我们上面分析的一连串加载、创建过程'
    ]},
    {'static Class<?> forName(String className)':[
        'ClassLoader.getClassLoader(caller):交给类加载器',
    ]},
    {'newInstance()':[
        '1.Constructor<T> c = getConstructor0(empty, Member.DECLARED):获取空参构造器',
        '2.没有空参构造器抛异常',
        '3.tmpConstructor.newInstance((Object[])null):调用空参构造器对象的newInstance()创建实例',
        '本质：newInstance()底层就是调用无参构造对象的newInstance()'
    ]},
    {'ReflectionData':[
        ' volatile Field[] declaredFields',
        'volatile Field[] publicFields',
        'volatile Method[] declaredMethods',
        'volatile Method[] publicMethods',
        'volatile Constructor<T>[] declaredConstructors',
        'volatile Constructor<T>[] publicConstructors',
        'volatile Field[] declaredPublicFields',
        'volatile Method[] declaredPublicMethods',
        'volatile Class<?>[] interfaces'
    ]},
    '字段、方法、构造器对象,因信息量太大，JDK还单独写了三个类：Field、Method、Constructor',
],
'反射API':[
    {'创建实例':[
        'clazz.newInstance()底层调用Contructor对象的newInstance()',
        '要想调用clazz.newInstance()，必须保证编写类的时候有个无参构造'
    ]},
    {'反射调用方法':[
        'Class对象获取Method时，需要传入方法名+参数的Class类型',
        'method.invoke(obj, args);要传入一个目标对象,java实例方法会隐式传递一个对象引用'
    ]}

]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 