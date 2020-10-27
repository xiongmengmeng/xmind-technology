import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\tomcat.xmind") 
s2=w.createSheet()
s2.setTitle("tomcat")
r2=s2.getRootTopic()
r2.setTitle("tomcat")


content={
'Web服务器机制':[
    {'通信协议':[
        'HTTP/HTTPS',
        'HTTP请求/响应模型',
        '解析HTTP报文'
    ]},
    {'套接字通信':[
        '应用层与传输层TCP/IP协议族通信的中间抽象层，是一组接口',
        '一般由操作系统提供或者由JVM自己实现',
        'TCP/IP协议族中有两种套接字类型，流套接字和数据报套接字，对应TCP协议和UDP协议',
        '一个TCP/IP套接字由一个互联网地址、一个协议及一个端口号唯一确定',
        {'分类':[
            '单播通信',
            {'组播通信':[
                '能在公网内传播',
                '没有可靠传输协议，数据不可靠',
                '路由器',
                '实现类：java.net.MulticastSocket'
            ]},
            {'广播通信':[
                '只能在局域网内传播',
                '交换机',
                '实现类java.net.DatagramSocket'
            ]}
        ]}
    ]},
    {'服务器端对I/O的处理模型':[
        '单线程阻塞I/O模型',
        '多线程阻塞I/O模型',
        {'单线程非阻塞I/O模型':[
            {'连接的三种检测方式':[
                '应用程序遍历套接字的事件检测',
                {'内核遍历套接字':[
                    '套接字的遍历工作交由操作系统内核',
                    '对套接字遍历结果组织成一系列事件列表并返回应用层处理',
                    '遍历工作下移到内核层',
                    '列表从内核复制到应用层,开销大',
                    '活跃连接较少时，内核与应用层间存在很多无效的数据副本'
                ]},
                {'内核基于回调':[
                    '内核中的套接字都对应一个回调函数',
                    '当客户端往套接字发送数据时，内核从网卡接收数据后就会调用回调函数',
                    '在回调函数中维护事件列表，应用层获取此事件列表即可得到所有感兴趣的事件',
                    {'两种':[
                        '可读列表readList和可写列表writeList标记读写事件(同套接字的数量）',
                        '事件列表'
                    ]}
                ]}
            
            ]},
        ]},
        {'多线程非阻塞I/O模型:Reactor模式':[
            {'改进':[
                '在耗时的process处理器中引入多线程，如使用线程池',
                '直接使用多个Reactor实例，每个Reactor实例对应一个线程'
            ]},
            '充分利用CPU资源，适合于高并发场景'
        ]}
    ]}],
'Servlet规范':[
    {'定义':[
        '描述HTTP请求及响应处理过程相关的对象及其作用',
        'Java体系的Web服务器都会遵循Servlet规范',
        'Tomcat是一个Servlet容器，它也需要遵守Servlet规范',
        '在Servlet容器中，每个Servlet类只能对应一个Servlet对象，所有请求都由同一个Servlet对象处理',
        '对于Web容器来说，实现SingleThreadModel接口意味着一个Servlet对象对应着一个线程',
    ]},
    {'Servlet接口':[
        {'两个Servlet类':[
            'GenericServlet：通用的、协议无关的Servlet',
            {'HttpServlet':[
                'HTTP的Servlet',
                'service方法把HTTP协议的GET请求转发到doGet处理方法',
                'POST、PUT、DELETE、HEAD、OPTIONS、TRACE请求同上'
            ]}
        ]},
        {'核心方法:service方法':[
            '处理客户端请求的方法',
            '客户端发起的请求会被路由到对应的Servlet对象上',
        ]},
        {'Servlet的生命周期':[
            '加载实例化:由Web容器完成',
            {'初始化':[
                '对应Servlet的init方法(参数为ServletConfig)',
                'ServletConfig为web.xml文件中配置的初始化参数',
                '由Web容器完成web.xml配置读取并封装成ServletConfig对象'
            ]},
            {'处理客户端请求':[
                '对应Servlet的service方法',
                '请求被封装成ServletRequest类型的请求对象和ServletResponse类型的响应对象'
            ]},
            {'销毁':[
                '对应Servlet的destroy方法',
                '调用destroy方法前要保证所有正在执行service方法的线程都完成执行',
                '把Servlet从Web容器中移除'
            ]}
        ]},
        {'ServletRequest接口':[
            '实现类封装了客户端请求的所有信息',
            'HTTP对应HttpServletRequest类,包含请求行和请求头部'
        ]},
        {'ServletContext接口':[
            '定义了运行所有Servlet的Web应用的视图',
            '添加Servlet,Filter,Listener到ServletContext里的方法'
        ]},
        {'ServletResponse接口':[
            '封装了服务器要返回客户端的所有信息'
        ]},
        {'Filter接口':[
            '允许Web容器对请求和响应做统一处理'
        ]},
        {'会话':[
            'HTTP对应的会话接口：HttpSession',
            'Cookie：常用的会话跟踪机制，标准名字JSESSIONID，会话ID通过调用HttpSession.getId()获取',
            'HttpSession对象限定在ServletContext级别，会话里面的属性不能在不同ServletContext之间共享',
            '分布式环境中，会话的所有请求在同一时间必须仅被一个JVM处理',
            '分布式容器迁移会话时会通知实现了HttpSessionActivationListener接口的所有会话属性'
        ]},
        {'注解':[
            '@WebServlet,@WebFilter,@WebInitParam,@WebListener'
        ]},
        {'Web应用':[
            '与ServletContext接口对象1：1，ServletContext对象提供了一个Servlet和它的应用程序视图',
            {'Web应用部署到容器':[
                '实例化web.xml中<listener>元素标识的每个事件监听器的一个实例',
                '对于已实例化且实现了ServletContextListener接口的监听器实例，调用contextInitialized()方法',
                '实例化web.xml中<filter>元素标识的每个过滤器的一个实例，并调用每个过滤器实例的init()方法',
                '根据load-on-startup 元素值定义的顺序，包含<load-on-startup>元素的<servlet>元素为每个Servlet实例化一个实例，并调用每个Servlet实例的init()方法'
            ]},
            '对不包含Servlet、Filter或Listener的Web应用，或使用注解声明的Web应用，不需要web.xml部署描述符'
        ]},
        'Servlet映射'
    ]}],
'Tomcat的启动与关闭':[
    {'Tomcat的批处理':[
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
    ]},
    {'Tomcat中的变量及属性':[
        {'Tomcat、JVM及操作系统之间相关的变量属性及操作':[
            '通过System.getenv(name)获取环境变量',
            '通过System.getProperty(name)获取JVM系统属性',
            '通过CatalinaProperties获取catalina. properties属性',
            '通过%变量名%直接获取环境变量',
            '执行JAVA时附带-Dparam=value'
        ]},
        {'环境变量':[
            '%JAVA_HOME%表示JDK的安装目录',
            '%CLASSPATH%JDK搜索class时优先搜索%CLASSPATH%指定的jar包',
            '%PATH%执行某命令时，如果在本地找不到此命令或文件，则会从%PATH%变量声明的目录中区查找'
        ]},
        {'JVM系统变量':[
            'user.dir：当前用户工作目录',
            'java.io.tmpdir：系统默认的临时文件目录,不同操作系统的目录不同',
            'java.home：Java安装目录',
            'user.home：用户目录',
            'catalina.home配置Tomcat的安装目录，在执行Tomcat启动的批处理脚本中会附带-Dcatalina.home="%CATALINA_HOME%"，即启动Tomcat程序时会把catalina.home作为JVM系统变量',
            'catalina.base配置Tomcat的工作目录',
            '工作目录与安装目录区别：运行多个Tomcat实例时，可以创建多个工作目录，而使用同一个安装目录，达到了多个Tomcat实例重用Tomcat程序的目的',
            '在执行Tomcat启动的批处理脚本中会附带-Dcatalina.base="%CATALINA_BASE%"，即启动Tomcat程序时会把catalina.base作为JVM系统变量',
            'catalina.config配置Tomcat配置文件catalina.properties的路径。'
        ]},
        {'Tomcat属性':[
            'package.access此属性与Java安全管理器的权限配置有关，用于配置包的访问权限',
            'package.definition此属性与Java安全管理器的权限配置相关，用于配置包的定义权限',
            'common.loader此属性用于配置Tomcat中用commonLoader类加载器加载的类库。'
        ]}
    ]}],
'整体结构及组件介绍':[
    '将Tomcat内核高度抽象，则它可以看成由连接器（Connector）组件和容器（Container）组件组成',
    '其中Connector组件负责在服务器端处理客户端连接，包括接收客户端连接、接收客户端的消息报文以及消息报文的解析等工作',
    '而Container组件则负责对客户端的请求进行逻辑处理，并把结果返回给客户端',
    {'Server组件':[
        '最顶级的组件，它代表Tomcat的运行实例',
        '一个JVM中只会包含一个Server'
    ]},
    {'Service组件':[
        '服务的抽象，它代表请求从接收到处理的所有组件的集合',
        'Server组件可以包含多个Service组件',
        '每个Service组件都包含了若干用于接收客户端消息的Connector组件和处理请求的Engine组件',
        '包含了若干Executor组件，每个Executor都是一个线程池，它可以为Service内所有组件提供线程池执行任务'
    ]},
    {'Connector组件':[
        '主要的职责就是接收客户端连接并接收消息报文，消息报文经由它解析后送往容器中处理',
        'HTTP、AJP等协议每种对应一个Connector组件，目前Tomcat包含HTTP和AJP两种协议的Connector',
        {'3部分':[
            {'Http11Protocol组件':[
                '包含接收客户端连接、接收客户端消息报文、报文解析处理、对客户端响应整个过程',
                '主要包含JIoEndpoint组件和Http11Processor组件',
                '启动时，JIoEndpoint组件内部的Acceptor组件将启动某个端口的监听',
                '请求到来后将被放入线程池Executor，线程池进行任务处理',
                '过程中将通过Http11Processor组件对HTTP协议解析并传递到Engine容器继续处理'
            ]},
            'Mapper组件：客户端请求的路由导航组件，它能通过请求地址找到对应的Servlet',
            'CoyoteAdaptor组件：将Connector和Container适配起来的适配器'
        ]}
    ]},
    {'Engine组件':[
        'Tomcat内部有4个级别的容器，分别是Engine、Host、Context和Wrapper',
        'Engine代表全局Servlet引擎，每个Service组件只能包含一个Engine容器组件',
        'Engine组件可以包含若干Host容器组件'
    ]},
    {'Host组件':[
        'Tomcat中Host组件代表虚拟主机，这些虚拟主机可以存放若干Web应用的抽象（Context容器）'
    ]},
    {'Context组件':[
        '是Web应用的抽象，的Web应用部署到Tomcat后运行时就会转化成Context对象',
        '包含了各种静态资源、若干Servlet（Wrapper容器）以及各种其他动态资源'
    ]},
    {'Wrapper组件':[
        'Wrapper容器是Tomcat中4个级别的容器中最小的，与之相对应的是Servlet，一个Wrapper对应一个Servlet'
    ]}
],
'Server组件与Service组件':[
    {'Server组件':[
        'Server组件是代表整个Tomcat的Servlet容器',
        'Tomcat的运行实例的抽象',
        {'3部分':[
            {'GlobalNamingResources组件':[
                '通过JNDI提供统一的命名对象访问接口，它的使用范围是整个Server'
            ]},
            {'ServerSocket组件':[
                '监听某个端口是否有SHUTDOWN命令，一旦接收到则关闭Server，即关闭Tomcat'
            ]},
            {'6个监听器组件':[
                'AprLifecycleListener监听',
                ' JasperListener监听',
                ' JreMemoryLeakPreventionListener监听',
                'GlobalResourcesLifecycleListener监听',
                ' ThreadLocalLeakPreventionListener监听',
                'NamingContextListener监听'
                
            ]}
        ]},
        {'作用':[
            '提供了监听器机制，用于在Tomcat整个生命周期中对不同事件进行处理',
            '提供了Tomcat容器全局的命名资源实现',
            '监听某个端口以接收SHUTDOWN命令'
        ]},
    ]},
    {'Service组件':[
        'Tomcat内的不同服务的抽象',
        '若干Connector组件和Executor组件组合而成',
        {'2部分':[
            {'Connector组件':[
                '负责监听某端口的客户端请求，不同的端口对应不同的Connector'
            ]},
            {'Executor组件':[
                '在Service抽象层面提供了线程池，让Service下的组件可以共用线程池',
                'JDK的JUC工具包'
            ]}
        ]}
    ]}],
'Connector组件':[
    '端口监听+请求报文解析(生成Request对象)+响应报文组装(Response对象)',
    'SSL安全通道支持:配置server.xml的<Connector>节点SSLEnabled属性开启',
    '想像成门',
    {'3部分':[
        {'Protocol组件':[
            '对不同通信协议（HTTP和AJP）处理进行了封装，有：Http11Protocol、Http11NioProtocol',
            {'Endpoint':[
                '不同的I/O模式(server.xml的<Connector>节点配置),不同Endpoint',
                'BIO模式的JIoEndpoint',
                'NIO模式的NioEndpoint和本地库I/O模式的AprEndpoint',
                {'2部分':[
                    'Acceptor：接收客户端连接的接收器组件',
                    'Executor：处理客户端请求的线程池'
                ]}
            ]},
            {'Processor组件':[
                '处理客户端请求的处理器，不同的协议和I/O模式有不同的Processor'
            ]}
        ]},
        {'Mapper组件':[
            '路由器，对客户端请求URL进行映射',
            '通过它将请求转发到对应的Host组件、Context组件、Wrapper组件以进行处理并响应客户端',
            '将某客户端请求发送到某虚拟主机上的某个Web应用的某个Servlet'
        ]},
        {'CoyoteAdaptor组件':[
            '适配器，将Connector组件和Engine容器适配连接',
            '把请求报文解析生成的请求对象和响应对象Response传递到Engine容器，交由容器处理'
        ]}
    ]},
    {'HTTP阻塞模式协议——Http11Protocol':[
        {'套接字接收终端——JIoEndpoint':[
            '端口监听客户端请求，接收套接字连接，提供一个线程池处理接收到的套接字连接，负责对连接数的控制，负责安全与非安全套接字连接的实现等',
            {'LimitLatch（连接数控制器)':[
                '控制套接字连接个数->控制流',
                'BIO模式,连接数:线程数=1:1',
                '默认情况，Tomcat处理连接池的线程数为200->BIO流量控制阀门大小也默认为200'
            ]},
            {'Acceptor（套接字接收器）':[
                '监听是否有客户端套接字连接并接收套接字',
                '将套接字交由Executor执行'
            ]},
            {'ServerSocketFactory套接字工厂':[
                '接收终端安全配置不同，套接字不同，引入了工厂模'
            ]},
            {'Executor任务执行器':[
                '使用JUC工具包的ThreadPoolExecutor类'
            ]},
            {'SocketProcessor（任务定义器':[
                '处理套接字并响应客户端',
                '连接数计数器减1',
                '关闭套接字'
            ]}
        ]},
        {'HTTP阻塞处理器——Http11Processor':[
            '套接字的读写和过滤，请求报文解析,生成Request对象，响应内容解析，生成Response对象',
            '套接字输入缓冲装置——InternalInputBuffer',
            '4个过滤器：IdentityInputFilter、VoidInputFilter、BufferedInputFilter、ChunkedInputFilter',
            {'套接字输出缓冲装置——InternalOutputBuffer':[
                'OutputStream：套接字的输出通道，通过其将字节写入到操作系统底层',
                'OutputStreamOutputBuffer：提供字节流输出的通道,与OutputFilter组合实现过滤效果',
                'OutputFilter：过滤器组件',
                'ByteChunk：为某个流添加缓冲功能'
            ]}
        ]}
    ]},
    {'HTTP非阻塞模式协议——Http11NioProtocol':[
        {'非阻塞接收终端——NioEndpoint':[
            'LimitLatch（连接数控制器)：对于NIO模式，Tomcat默认流量阀门为10 000',
            'Acceptor（套接字接收器）:负责接收套接字连接并注册到通道队列里面',
            'Poller（轮询器）:负责轮询检查事件列表',
            {'Poller（轮询器）':[
                '负责轮询检查事件列表',
                '内部依赖JDK的Selector对象进行轮询，选择出待处理的事件，每轮询一次就选出若干需要处理的通道'
            ]}
            'Poller池:包含了若干Poller组件',
            {'SocketProcessor（任务定义器）':[
                '用NIO方式读取套接字并进行处理，输出响应报文',
                '连接数计数器减一腾出通道',
                '关闭套接字'  
            ]}
            'Executor（任务执行器）'
        ]},
        {'HTTP非阻塞处理器——Http11NioProcessor':[
            '提供了对HTTP协议非阻塞模式的处理，作用同Http11Processor'
        ]}
    ]}],
'Engine容器':[
    '虚拟主机——Host:Engine容器的子容器，它表示一个虚拟主机',
    '访问日志——AccessLog:负责客户端请求访问日志的记录',
    '管道——Pipeline:搭配阀门（Valve）才能工作',
    'Engine集群——Cluster',
    'Engine域——Realm',
    '生命周期监听器——LifeCycleListener',
    '日志——Log'
],
'Context容器':[
    '一个Context对应一个Web应用程序',
    {'':[
        'Context容器的配置文件',
        '包装器——Wrapper',
        'Context域——Realm',
        '访问日志——AccessLog',
        '访问日志——AccessLog',
        '会话管理器——Manager',
        '目录上下文——DirContext',
        '安全认证',
        'Jar扫描器——JarScanner',
        '过滤器',
        '命名资源——NamingResource',
        'Servlet映射器——Mapper',
        '管道——Pipeline',
        'Web应用载入器——WebappLoader',
        'ServletContext的实现——ApplicationContext',
        '实例管理器——InstanceManager:实现对Context容器中监听器、过滤器以及Servlet等实例的管理',
        '',
        ''
    ]}
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\tomcat.xmind") 