import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Tomcat架构")
r2=s2.getRootTopic()
r2.setTitle("Tomcat架构")


content={
'Tomcat的目录结构':[
    'bin:存放启动和关闭Tomcat的脚本文件',
    {'conf:存放Tomcat服务器的各种配置文件':[
        'Server.xml',
        {'web.xml':[
            '请求路径找不到对映Servlet处理，使用文件里配置的DefaultServlet',
            '请求*.jsp的资源,使用JspServlet，将jsp翻译成Servlet'
        ]}
    ]},
    'lib:存放Tomcat服务器和所有web应用程序需要访问的jar文件',
    'logs:存放Tomcat的日志文件',
    'temp:存放Tomcat运行时产生的临时文件',
    'webapps:当发布web应用程序时，通常把web应用程序的目录及文件放到这个目录下',
    'work:Tomcat将JSP生成的Servlet源文件和字节码文件放到这个目录下'

],
'Tomcat的架构':[
    'Server.xml文件中的配置结构和Tomcat的架构是一一对应的',
    '<Server>，代表服务器，<Server>下面有且仅有1个<Service>，代表服务',
    '<Service>下有两个<Connector>，监听端口,代表连接（需要可以再加）',
    'Tomcat默认配置两个端口，一个是HTTP/1.1协议(专门处理HTTP请求)，一个是AJP/1.3协议',
    '<Engine>（Tomcat引擎），与Connector平级',
    '<Engine>下面有个Host，代表虚拟主机',
    'Context：我们开发的Web应用',
    {'举例':[
        '在浏览器输入"localhost:8080/myWeb/index.html"',
        '浏览器是以HTTP协议发送请求',
        '当请求到了服务器后，会被识别为HTTP类型',
        '服务器就找来专门处理HTTP的Connector',
        '它的默认端口正是Server.xml配置的8080',
        'Connector不处理实际业务，它会负责把请求带到Engine那，然后Engine会处理',
        'Engine根据myWeb找到对映context,即我们开发的web应用'
    ]},

],
'动手实现Tomcat':[
   '链接：https://pan.baidu.com/s/1gCWs7Jsr2qtABXQN7HHegw 密码：35se'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 