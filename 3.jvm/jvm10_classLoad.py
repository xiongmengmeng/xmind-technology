import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_classLoad")
r2=s2.getRootTopic()
r2.setTitle("类加载及执行子系统的案例")


content={



'Tomcat':[
    '正统的类加载器架构',
    {'目录结构':[
        '/common:类库可被Tomcat和Web应用程序共同使用;使用Common类加载器加载',
        '/server:类库可被Tomcat使用，对Web应用程序不可见;使用Catalina类加载器加载',
        '/shared:类库可被Web应用程序使用，对Tomcat不可见;使用Shared类加载器加载',
        '/WebApp/WEB-INF:类库仅可被该Web应用程序使用，对Tomcat和其他Web应用程序不可见;使用WebApp类加载器加载'
    ]},
    '为支持这套目录结构，并对目录里面的类库进行加载和隔离，Tomcat按照经典的双亲委派模型自定义了多个类加载器',
    {'JasperLoader类加载器':[
        '加载范围仅仅是这个JSP文件所编译出来的Class文件',
        '服务器检测到JSP文件被修改，会建立一个新的JSP类加载器替换掉目前的，实现JSP文件HotSwap功能'
    ]},
    'Tomcat 6及之后的版本:/common、/server和/shared这3个目录默认合并到一起变成1个/lib目录'
],
'OSGi：灵活的类加载器架构':[],
'字节码生成技术与动态代理的实现':[],
'Backport工具：Java的时光机器':[],
'实现远程执行功能':[
    {'思路':[
        {'如何编译提交到服务器的Java代码':[
            '客户端编译好，把字节码而不是Java代码传到服务端'
        ]},
        {'如何执行编译之后的Java代码':[
            '让类加载器加载这个类生成一个Class对象，然后反射调用方法'
        ]},
        {'如何收集Java代码的执行结果':[
            '在执行的类中把对System.out的符号引用替换为PrintStream的符号引用'
        ]}
    ]},
    {'实现':[
        'HotSwapClassLoader:实现“同一个类的代码可以被多次加载”',
        'ClassModifier:修改符合Class文件格式的byte[]数组中的常量池部分',
        '将常量池中指定内容的CONSTANT_Utf8_info常量替换为新的字符串',
        'HackSystem:代替java.lang.System',
        'JavaclassExecuter:提供给外部调用的入口，调用前面几个支持类组装逻辑，完成类加载工作'
    ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 