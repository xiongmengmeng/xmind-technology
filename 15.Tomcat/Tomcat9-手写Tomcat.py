import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("手写tomcat")
r2=s2.getRootTopic()
r2.setTitle("手写tomcat")


content={
'客户端':[
    {'1.创建一个Socker对象，连接xxx域名的80端囗':[
        'Socket socket=new Socker("xxx",80)',
    ]},
    {'2.获取输出流对象':[
        'InputStream is=socker.getInputStream()',
    ]},
    {'3.获取输入流对象':[
        'OutputStream ops=socker.getOutputStream()',
    ]},
    {'4.将HTTP协议的请求部分发送到服务端':[
        'ops.write("GET  yyy.html HTTP/1.1\\n".getBytes())',
        'ops.write("请求头的内容".getBytes())',
        'ops.write("请求体的内容".getBytes())',
        'ops.write("\n".getBytes())'
    ]},
    {'5.将来自服务器的数据打印到控制台':[
        'int i=is.read()',
        'while(i!=-1){',
        '   System.out.print((char)i)',
        '   i=is.read()',
        '}'
    ]},
    {'6.释放资源':[
        '...'
    ]}
],
'服务端':[
    {'1.创建ServerSockt对象，监听本机80端囗':[
        'ServerSockt serverSockt=new ServerSockt(80)',
    ]},
    {'2.等待来自客户端的请求，获取客户端对应的Socket对象':[
        'Sockt sockt=serverSockt.accept()',
    ]},
    {'3.通过Sockt对象获取到输入流对象':[
        'InputStream is=socker.getInputStream()',
    ]},
    {'4.通过Sockt对象获取到输出流对象':[
        'OutputStream ops=socker.getOutputStream()',
    ]},
    {'5.通过输出流将获取到的资源内容发送给客户端':[
        'ops.write("HTTP/1.1 200 ok\\n".getBytes())',
        'ops.write("响应头的内容".getBytes())',
        'ops.write("\n".getBytes())'
    ]},
    {'6.通过输入流读取客户端的数据，并分析本次请求需要获取的资源':[
        {'要获取html数据':[
            '读取对映html数据到服务器内存',
            'ops.write("html文件内容".getBytes())',
            'ops.flush()'
        ]},
        {'运行一段代码':[
            '服务器启动时加载配置数据到map(放在静态代码块中)',
            '从map中拿到资源对映路径',
            '反射加载到内存创建对映对象',
            '调用对象方法',
            'ops.write("方法结果".getBytes())',
            'ops.flush()'
        ]},
    ]},
    {'5.释放资源':[
        '...'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 