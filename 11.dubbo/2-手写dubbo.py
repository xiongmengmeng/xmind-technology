import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("手写dubbo")
r2=s2.getRootTopic()
r2.setTitle("手写dubbo")


content={
'Provider模块':[
    {'配置':[
        'application--应用名',
        'registry--注册中心',
        'potocol--协议',
        'provider--配置负载均衡策略，过滤器'
        'service--要提供的接囗服务'
    ]},
    {'提供API，实现API':[
        '略'
    ]},
    {'将接囗注册到本地和远程的注册中心':[
        '调用RemoteMapRegister类的registry()方法',
        '调用LocalMapRegister类的registry()方法',
    ]},
    {'暴露':[
        {'使用tomcat':[
            '1.使用内嵌tomcat包',
            '2.创建tomcat对象，并启动tomcat.start()',
            {'3.创建Servlet，加入tomcat':[
                '继承HttpServlet类，重写service()方法(处理请求)',
                {'service()方法':[
                    '1.拿到invocation对象',
                    '2.根据接囗名从LocalMapRegister类，拿到实现类的Class',
                    '3.从实现类的Class中，根据方法名，得到Method对象',
                    '4.执行方法，method.invoke(实例，参数)'
                ]}
            ]}
        ]},
        {'使用netty':[
            '略'
        ]}
    ]}

],
'Consumer模块':[
    {'配置':[
        'application--应用名',
        'registry--注册中心',
        'potocol--协议',
        'consumer--配置负载均衡策略，过滤器'
        'reference--要提供的接囗服务',  
    ]},
    {'拿接囗从注册中心获取服务地址':[
        '调用RemoteMapRegister类的get()方法，拿到所有URL',
        '使用负载均衡算法到出一个URL'
    ]},
    {'调用服务':[
        {'1.封装一个Invocation类':[
            'String interfaceName',
            'String methodName',
            'Class[] paramType',
            'Object[] params',
        ]},
        {'2.发送请求':[
            '2.1.有传参Invocation对象',
            '2.2.有地址URL',
            {'2.3.使用网络API发送请求，并获取返回结果':[
                'URL url=new URL(...)',
                'HttpURLConnection h=url.openConnection()',
                'OutputStream() ops=h.getOutputStream()',
                'ObjectOutputStream oos=new ObjectOutputStream(ops)'
                'oos.writeObject(invocation)',
                'oos.flush()',
                'oos.close()',
                'InputStream() is=h.getInputStream()',
                'String result=IOUtils.toString(is)'
            ]}
        ]},
        {'3.封装一个代理类':[
            '实现网络调用',
            '将发送请求的内容放入invoke()方法内'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 