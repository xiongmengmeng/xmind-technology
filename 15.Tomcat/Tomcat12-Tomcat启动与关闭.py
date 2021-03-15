import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Tomcat的启动与关闭")
r2=s2.getRootTopic()
r2.setTitle("Tomcat的启动与关闭")


content={
'Tomcat的批处理':[
    'startup.bat:启动批处理脚本，主要是找到catalina.bat并且执行',
    'shutdown.bat:找到catalina.bat并且执行',
    {'cataIina.bat':[
        'Tomcat服务器启动和关闭的核心脚本',
        '目的是组合出一个最终的执行命令',
        '第一部分:在按Ctrl+C组合键终止程序时自动确认',
        '第二部分:设置CATALINA_HOME、CATALINA_BASE两个变量',
        '第三部分:寻找setenv.bat和setclasspath.bat并执行它们',
        '然后将Tomcat的启动包bootstrap.jar和日志包tomcat-juli.jar添加到CLASSPATH环境变量下',
        '第四部分:对日志配置的设置',
        '第五部分:一些参数的初始化',
        '第六部分:根据不同的参数跳转到不同的位置执行不同的命令',
        '第七部分:命令真正执行的过程，将前面所有脚本运行后组成一个最终的命令开始执行'
    ]},
    'setcIasspath.bat:负责寻找、检查JAVA_HOME和JRE_HOME两个环境变量'
],
'Tomcat中的变量及属性':[
    {'Tomcat、JVM及操作系统之间相关的变量属性及操作':[
        '通过System.getenv(name)获取环境变量',
        '通过System.getProperty(name)获取JVM系统属性',
        '通过CatalinaProperties获取catalina. properties属性',
        '通过%变量名%直接获取环境变量',
        '执行JAVA时附带-Dparam=value'
    ],
    '环境变量':[
        '%JAVA_HOME%表示JDK的安装目录',
        '%CLASSPATH%JDK搜索class时优先搜索%CLASSPATH%指定的jar包',
        '%PATH%执行某命令时，如果在本地找不到此命令或文件，则会从%PATH%变量声明的目录中区查找'
    ],
    'JVM系统变量':[
        'user.dir：当前用户工作目录',
        'java.io.tmpdir：系统默认的临时文件目录,不同操作系统的目录不同',
        'java.home：Java安装目录',
        'user.home：用户目录',
        'catalina.home配置Tomcat的安装目录，在执行Tomcat启动的批处理脚本中会附带-Dcatalina.home="%CATALINA_HOME%"，即启动Tomcat程序时会把catalina.home作为JVM系统变量',
        'catalina.base配置Tomcat的工作目录',
        '工作目录与安装目录区别：运行多个Tomcat实例时，可以创建多个工作目录，而使用同一个安装目录，达到了多个Tomcat实例重用Tomcat程序的目的',
        '在执行Tomcat启动的批处理脚本中会附带-Dcatalina.base="%CATALINA_BASE%"，即启动Tomcat程序时会把catalina.base作为JVM系统变量',
        'catalina.config配置Tomcat配置文件catalina.properties的路径。'
    ],
    'Tomcat属性':[
        'package.access此属性与Java安全管理器的权限配置有关，用于配置包的访问权限',
        'package.definition此属性与Java安全管理器的权限配置相关，用于配置包的定义权限',
        'common.loader此属性用于配置Tomcat中用commonLoader类加载器加载的类库'
    ]
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 