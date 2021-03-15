import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("servlet")
r2=s2.getRootTopic()
r2.setTitle("servlet")


content={
'servlet':[
    '一个Java接口,定义一套处理网络请求规范',
    {'5个方法':[
        '1.void init(ServletConfig config)',
        '2.ServletConfig getServletConfig()',
        '3.service(ServletRequest req, ServletResponse res):处理请求',
        '4.String getServletInfo()',
        '5.void destroy()'
    ]},

    '网络请求与响应都是tomcat来负责的',
    'Servlet用于编码业务代码，所谓的Request和Response是Tomcat传给它，用来处理请求和响应的工具，但它本身不处理这些'
],
'Tomcat':[
    '与客户端直接打交道',
    'Web服务器和Servlet容器的结合体',
    'Web服务器:将某个主机上的资源映射为一个URL供外界访问',
    'Servlet容器:处理请求',
    {'通过Web服务器映射的URL访问资源过程':[
        '接收请求',
        '处理请求',
        '响应请求'
    ]},
    {'详细过程':[
        '1.监听端口',
        '2.请求过来后，解析HTTP请求，封装成request',
        '3.调用那个servlet的service方法',
        '4.service方法返回一个response对象',
        '5.tomcat再把这个response,把结果转成HTTP响应返回给客户端'
    ]},
    '接收请求和响应请求是共性功能，且没有差异性,由Web服务器实现',
    '处理请求的逻辑不同，抽取出来做成Servlet，交给程序员自己编写',
    {'Tomcat传入Servlet的三个对象':[
        {'ServletConfig':[
            'Servlet配置,来自web.xml',
            '封装了servlet的一些参数信息，如需要，我们可从它获取'
        ]},
        {'ServletRequest':[
            'HTTP请求到了Tomcat后,Tomcat通过字符串解析,把请求头Header，请求地址Url，请求参数QueryString都封装进了Request对象中',
        ]},
        {'ServletResponse':[
            'Tomcat传给Servlet时，它是空的对象',
            'Servlet逻辑处理后得到结果，最终通过response.write()方法，将结果写入response内部的缓冲区',
            'Tomcat会在servlet处理结束后，拿到response，遍历里面的信息，组装成HTTP响应发给客户端'
        ]}
    ]}
],
'GenericServlet':[
    '抽象类',
    '改进:提升了init方法中原本是形参的servletConfig对象的作用域（成员变量）,方便其他方法使用'
],
'HttpServlet':[
    '改进:service方法中根据请求方式，调用不同的处理方法doGet,doPost'
],
'学习':[
    'https://www.zhihu.com/question/21416727',
    'https://zhuanlan.zhihu.com/p/54121733'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 