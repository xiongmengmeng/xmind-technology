import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Tomcat基础")
r2=s2.getRootTopic()
r2.setTitle("Tomcat基础")


content={
'JavaEE规范：JDBC，JNDI，EJB，RMI，JSP，Servlets，XML，JMS，Java IDL，JTS，JTA，JavaMail，JAF':[],
'Tomcat实现Servlet和JSP,所以它也叫Servlet/JSP容器':[],
'服务器最本质的作用':[
    '将资源对外暴露',
    '配合各种传输协议进行响应输出'
],
'基础概念':[
    'IP：电子设备（计算机）在网络中的唯一标识，一个IP对应一台实体电脑',
    '端口：应用程序在计算机中的唯一标识，一个端口只能被唯一程序占用',
    '传输协议：数据传输的规则',
    {'HTTP':[
        '一种协议规则',
        {'网络协议':[
            'http:超文本的传送规则（html超文本标记语言）',
            'pop3,pop,imap:邮箱数据的传送规则',
            'ftp,流媒体协议：视频数据的传送规则'
        ]},
        '格式：基于请求-响应模型'
    ]}
],
'概念联系':[
    'IP对映服务器，端囗对映软件',
    'IP可以精准定位一台电脑,但一台电脑可运行多个软件',
    '应用程序访问：IP+端囗'
],
'用浏览器访问百度':[
    '1.www.baidu.com',
    '2.去本机的hosts文件查www.baidu.com对映IP,查不到',
    {'3.去DNS服务器查www.baidu.com对映IP:115.239.210.27:443':[
        '443是HTTPS默认端囗',
        '80是HTTP默认端囗'
    ]},
    {'4.定位服务器，记得用IP+host域名':[
        '因为一台服务器，可能运行多台虚拟主机',
        '即域名!=IP,一个IP可以对应多个域名',
        'IP只是对应实体服务器，而域名对应具体的网站'
    ]}
],
'容易混淆的小概念':[
    'Tomcat服务器 = Web服务器 + Servlet/JSP容器（Web容器）',
    'Web服务器作用:接收客户端的请求，给客户端作出响应（只静态资源）',
    'JSP/Servlet容器作用：把动态资源转换成静态资源'
],
'Web服务器类似一个收发器':[],
'我们用Java开发的Web应用,是一个半成品，类似于一个插件':[]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 