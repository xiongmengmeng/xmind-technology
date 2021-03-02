import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm3_class")
r2=s2.getRootTopic()
r2.setTitle("jvm3_类加载")


content={

# '类的生命周期':[
#     '加载（Loading）',
#     '连接:验证（Verification）--准备（Preparation）--解析（Resolution）',
#     '初始化（Initialization）->使用（Using）->卸载（Unloading）' 
# ],
'加载':[
    {'三阶段':[
        '1.通过类的全限定名来获取定义此类的二进制字节流',
        '2.将字节流所代表的静态存储结构转化为方法区的运行时数据结构',
        '3.生成代表此类的java.lang.Class对象，作为方法区类各种数据的访问入口'
    ]},
    {'类加载器':[
        {'定义':[
            '通过一个类的全限定名来获取描述该类的二进制字节流',
            '动作放在Java虚拟机外部实现，方便应用程序决定如何去获取所需的类',
            '任意一个类，由加载它的类加载器+类本身共同确立其在Java虚拟机中的唯一性',
            '每一个类加载器，都拥有一个独立的类名称空间'
        ]},
        {'分类':[
            '启动类加载器(BootstrapClassLoader):C++语言实现，虚拟机自身的一部分',
            '其他类加载器:Java语言实现,继承自抽象类java.lang.ClassLoader,独立存在于虚拟机外部'
        ]},
        '自定义：解密加密后的.class文件，防止代码被反编译'
    ]},

],
'加载--双亲委派模型':[
    'Java一直保持着三层类加载器、双亲委派的类加载架构',
    {'系统提供的类加载器(组合的关系,详情看类sun.misc.Launcher)':[
        '启动类加载器（Bootstrap Class Loader）',
        '扩展类加载器（Extension Class Loader)',
        '应用程序类加载器（Application Class Loader)'
    ]},
    {'要求':[
        '除了顶层的启动类加载器外，其余的类加载器都应有自己的父类加载器',
        '类加载器之间的父子关系不以继承，而是使用组合关系来复用父加载器的代码'
    ]},
    {'工作过程':[
        '如果一个类加载器收到了类加载的请求，不会尝试加载这个类，而是把请求委派给父类加载器',
        '每一个层次的类加载器都是如此,所有的加载请求最终都传送到最顶层的启动类加载器中',
        '当父加载器反馈自己无法完成这个加载请求时，子加载器会尝试自己去完成加载'
    ]},
    {'优点':[
        'Java中的类随着它的类加载器一起具备了一种带有优先级的层次关系'
    ]}

],
'加载--双亲委派模型--破坏':[
    {'破坏':[
        'JDBC4.0后，可用spi方式注册Driver',
        'DriverManager.getConnection("...")',
        'DriverManager:启动类加载器加载，Driver:应用类加载器加载',
        '解决：使用Thread.currentThread().getContextClassLoader()，获得上下文类加载器',
        '线程上下文类加载器让父级类加载器通过调用子级类加载器来加载类，打破了双亲委派模型原则'
    ]},
    {'热部署':[
        '销毁自定义classloader(被该加载器加载的class也会自动卸载)',
        '更新class',
        '使用新的ClassLoader去加载class'
    ]},
    {'自定义类加载器':[
        '符合双亲委派规范，重写findClass方法（用户自定义类加载逻辑）',
        '破坏:重写loadClass方法(双亲委派的具体逻辑实现)'
    ]},
    'https://blog.csdn.net/yusimiao/article/details/99301293'
],
'验证':[
    '目的：确保Class文件的字节流包含信息符合要求',
    {'四阶段':[
        {'文件格式验证':[
            '目的：保证输入的字节流能正确地解析并存储于方法区',
            '基于二进制字节流进行的，通过，字节流才被允许进入JVM内存的方法区中进行存储',
            '后面三个验证阶段全是基于方法区的存储结构，不会再直接读取、操作字节流'
        ]},
        {'元数据验证':[
            '对字节码描述的信息进行语义分析'
        ]},
        {'字节码验证':[
            '目的：通过数据流和控制流分析，确保程序语义合法、符合逻辑',
            '对类的方法体（Class文件中的Code属性）进行校验分析'
        ]},
        {'符号引用验证':[
            '目的：确保解析行为能正常执行',
            '解析阶段，会将符号引用转化为直接引用'
        ]}
    ]}
],
'准备':[
    '为类中定义的变量分配内存并设置初始值(jvm 默认的初值)',
    {'类中定义的变量':[
        '仅包括类变量，不包括实例变量',
        '实例变量将会在对象实例化时随着对象一起分配在Java堆中'
    ]},
    {'内存':[
        'JDK 8后变量的内存也是指Java堆，方法区只是一种逻辑概念'
    ]},
    {'初始值':[
        '通常情况下是数据类型的零值',
        '特殊：类字段的字段属性表中存在ConstantValue属性，变量值就会被初始化为属性所指定的初始值'
    ]}
],
'解析':[
    {'定义':[
        '将常量池内的符号引用替换为直接引用的过程',
        {'符号引用':[
            '以一组符号来描述所引用目标'
        ]},
        {'直接引用':[
            '直接指向目标的指针、相对偏移量或者是一个能间接定位到目标的句柄',
            '和内存布局相关,如果有了直接引用，那引用的目标必已在内存中存在'
        ]}
    ]},
    {'符号引用类型':[
            '类,接口,字段,类方法,接口方法,方法类型',
            '方法类型,方法句柄,调用点限定符'
    ]}
],
'初始化':[
    '执行类构造器<clinit>()方法的过程(编译生成class文件时产生，类的初始化方法)',
    {'<clinit>()内容':[
        '所有类变量的赋值动作',
        '静态语句块（static{}块）'
    ]},
    {'条件':[
        '1.遇到new、getstatic、putstatic或invokestatic这四条字节码指令时',
        '2.使用java.lang.reflect包的方法对类型进行反射调用时',
        {'3.初始化类的时，其父类还未初始化':[
            '类在初始化时，要求其父类全部要初始化',
            '接口在初始化时，不要求其父接口初始化,在使用到父接口的时候才会初始化'
        ]},
        '4.虚拟机启动时，用户指定的主类（包含main()方法的那个类）',
        {'5.java.lang.invoke.MethodHandle实例解析结果为下面四种类型的方法句柄时':[
            'REF_getStatic，REF_putStatic,REF_invokeStatic',
            'REF_newInvokeSpecial'
        ]},
        '6.一个接口中定义了JDK8新加的默认方法，如接口的实现类发生了初始化，接口要在其之前被初始化'
    ]}
],
'卸载':[
    '类所有实例已被回收，即java堆中不存在该类的任何实例',
    '加载该类的ClassLoader已被回收',
    '类对应的java.lang.Class对象没有任何地方引用，无法通过反射访问该类方法'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 