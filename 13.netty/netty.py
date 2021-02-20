import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("netty")
r2=s2.getRootTopic()
r2.setTitle("netty")


content={

# '前言':[
#     {'netty':[
#         '一个提供异步的、事件驱动的网络应用程序框架，所有IO操作都是异步非阻塞的',
#         '通过Future-Listener机制，用户可以方便地主动获取或者通过通知机制获得IO操作结果'
#     ]},
#     {'redis':[
#         'Remote Dictionary Server（远程字典服务器）'
#     ]},
#     {'ZooKeeper':[
#         '分布式协调工具'
#     ]},
#     {'高并发IM':[
#         '一切高实时性通信、消息推送的应用场景',
#         '如：私信、聊天、大规模推送、视频会议、抽奖、互动游戏、基于位置的应用（Uber、滴滴司机位置）、在线教育' 
#     ]}
# ],
'高并发IO':[
    {'IO读写':[
        '会用到底层的read&write两大系统调用',
        {'read系统调用':[
            '把数据从内核缓冲区复制到进程缓冲区'
        ]},
        {'write系统调用':[
            '把数据从进程缓冲区复制到内核缓冲区'
        ]},
        {'同步IO':[
            '用户空间的线程是主动发起IO请求的一方，内核空间是被动接受方'
        ]},
        {'异步IO':[
            '系统内核是主动发起IO请求的一方，用户空间的线程是被动接受方'
        ]},
        {'内存缓冲区':[
            '目的是为了减少频繁地与设备之间的物理交换',
            '外部设备的直接读写，涉及cpu的中断',
            '发生系统中断时，需要保存之前在cpu中的进程数据和状态等信息，而结束中断之后，还需要恢复之前的进程数据和状态等信息'
        ]}
    ]},
    {'四种主要的IO模型':[
        {'同步阻塞IO（Blocking IO)':[
            {'内核进行IO执行的两个阶段':[
                '等待数据（操作系数将磁盘数据读取到内核）',
                '复制数据（将数据从内核缓冲区读取到用户缓冲区）'
            ]},
            '在内核进行IO执行的两个阶段,用户线程都被阻塞了',
            '特点：高并发场景下，需要大量的线程来维护大量的网络连接，内存、线程切换开销很大']},
        {'同步非阻塞IO（Non-blocking IO)':[
            {'两个步骤':[
                '1.在内核数据没有准备好的阶段，用户线程发起IO请求时，立即返回',
                '2.内核数据到达后，用户线程发起系统调用，用户线程阻塞'
            ]},
            '特点：应用程序的线程需要不断地进行IO系统调用,会占用大量的CPU时间，效率低下']},
        {'IO多路复用（IO Multiplexing）':[
            {'四个步骤':[
                {'1.选择器注册':[
                    '将需要read操作的目标socket网络连接，提前注册到select/epoll选择器中，Java中对应的选择器类是Selector类'
                ]},
                {'2.就绪状态的轮询':[
                    '通过选择器的查询方法，查询注册过的所有socket连接的就绪状态，内核会返回一个就绪的socket列表'
                ]},
                {'3.用户线程发起read系统调用':[
                    '用户线程获得了就绪状态的列表后，根据其中的socket连接，发起read系统调用，用户线程阻塞，内核开始复制数据，将数据从内核缓冲区复制到用户缓冲区'
                ]},
                '4.复制完成后，内核返回结果，用户线程解除阻塞的状态'
            ]},
            {'特点':[
                '涉及两种系统调用（System Call），一种是select/epoll（就绪查询），一种是IO操作',
                '通过select/epoll系统调用，一个进程可以监视多个文件描述符，一旦某个描述符就绪（一般是内核缓冲区可读/可写），内核能够将就绪的状态返回给应用程序',
                'Java语言的NIO（New IO）技术，使用的就是IO多路复用模型',
                '系统开销小，系统不必为每一个网络连接（文件描述符）创建进程/线程，从而大大减小了系统的开销。'
            ]}
        ]},
        {'异步IO（Asynchronous IO）':[
            {'四个步骤':[
                '1.用户线程通过系统调用，向内核注册某个IO操作,用户执行后续的业务操作',
                '2.内核进行整个IO操作（包括数据准备、数据复制）',
                '3.完成后，通知用户程序:内核会给用户线程发送一个信号（Signal），或者回调用户线程注册的回调接口',
                '4.用户线程读取用户缓冲区的数据' 
            ]},
            {'特点':[
                '非阻塞：在内核等待数据和复制数据的两个阶段，用户线程都不是阻塞的',
                '信号/事件驱动：用户线程需要接收内核的IO操作完成的事件，或者用户线程需要注册一个IO操作完成的回调函数',
                '内核支持：应用程序仅需要进行事件的注册与接收，其余的工作都留给了操作系统，因此需要底层内核提供支持'
            ]}
        ]},
    ]},
    {'操作系统对高并发的底层的支持':[
        '在Linux系统中，文件可分为：普通文件、目录文件、链接文件和设备文件',
        '文件句柄，文件描述符（File Descriptor）:内核为了高效管理已被打开的文件所创建的索引',
        '所有的IO系统调用，包括socket的读写调用，都是通过文件描述符完成的',
        'Linux操作系统中文件句柄数的限制，编辑/etc/rc.local开机启动文件:ulimit -SHn 1000000'
    ]}],
'Java NIO':[
    {'Java NIO组件':[
        '提供了统一的API，为大家屏蔽了底层的不同操作系统的差异'
    ]},
    {'三个核心组件':[
        'Channel（通道）',
        'Buffer（缓冲区）·',
        'Selector（选择器）'
    ]},
    {'NIO和OIO的对比':[
        'OIO是面向流（Stream Oriented）的，NIO是面向缓冲区（Buffer Oriented）的',
        'OIO的操作是阻塞的，NIO的操作是非阻塞的',
        'OIO没有选择器（Selector）概念，而NIO有选择器的概念'
    ]},
    {'缓冲区（Buffer）':[
        '定义：本质上是一个内存块，既可以写入数据，也可以从中读取数据',
        {'Buffer类':[
            '一个抽象类,非线程安全的，内部有一个byte[]数组内存块，作为内存缓冲区',
            {'4个重要的属性:记录读写的状态和位置':[
                {'capacity（容量）':[
                    '容量是指写入的数据对象的数量，缓冲区创建时设置,不能改变'
                ]},
                {'position属性':[
                    '位置，缓冲区中下一个要被读写的元素索引',
                    '使用（即调用）flip翻转方法，将缓冲区的写模式切换为读模式'
                ]},
                {'limit属性':[
                    '表示读写的最大上限'
                ]},
                {'mark（标记）':[
                    '一个暂存属性，暂时保存position的值，方便后面的重复使用position值'
                ]}
            ]},
            {'常用方法':[
                {'allocate()':[
                    '创建缓冲区:分配内存、返回了实例对象'
                ]},
                {'put()':[
                    '写入到缓冲区'
                ]},
                {'flip()':[
                    '翻转,将写模式变为读模式',
                    'limit变为写模式的position值',
                    'position重置为0',
                    '清除mark标记'
                ]},
                {'clear()/compact()':[
                    '将缓冲区转换为写模式'
                ]},
                {'get()':[
                    '从缓冲区读取'
                ]},               
                {'rewind()':[
                    '倒带,position重置为0,mark标记被清理'
                ]},
                {'mark( )&reset( )':[
                    '重复读取缓冲区'
                ]}
            ]},
            {'Java NIO Buffer类的使用步骤':[
                {'1.创建一个Buffer类的实例对象':[
                    '使用创建子类实例对象的allocate()方法'
                ]},
                {'2.将数据写入到缓冲区中':[
                    '调用put方法'
                ]},
                {'3.将缓冲区转换为读模式':[
                    '写入完成后，在开始读取数据前，调用Buffer.flip()方法'
                ]},
                {'4.从缓冲区中读取数据':[
                    '调用get方法'
                ]},
                {'5.将缓冲区转换为写入模式':[
                    '读取完成后，调用Buffer.clear() 或Buffer.compact()方法，将缓冲区转换为写入模式'
                ]}
            ]}
        ]}
    ]},
    {'通道（Channel）':[
        {'定义':[
            '一个连接就是用一个Channel（通道）',
            '一个通道可以表示一个底层的文件描述符，例如硬件设备、文件、网络连接',
            '涵盖了文件IO、TCP网络、UDP IO、基础IO'
        ]},
        {'分类':[
            {'FileChannel文件通道':[
                '阻塞模式,用于文件的数据读写',
                {'4个核心操作':[
                    {'获取FileChannel通道':[
                        'getChannel()'
                    ]},
                    {'读取FileChannel通道':[
                        'int read（ByteBufferbuf）',
                        '从通道读取到数据',
                        '然后写入到ByteBuffer缓冲区',
                        '并且返回读取到的数据量'
                    ]},
                    {'写入FileChannel通道':[
                        'int write（ByteBufferbuf）',
                        '从ByteBuffer缓冲区中读取数据',
                        '然后写入到通道自身',
                        '最后返回写入成功的字节数'
                    ]},
                    {'关闭通道':[
                        'close()'
                    ]},
                    {'强制刷新到磁盘':[
                        'force()方法'
                    ]}
                ]}
            ]},
            {'SocketChannel套接字通道':[
                {'定义':[
                    '用于Socket套接字TCP连接的数据读写,与OIO中的Socket类对应',
                    '支持阻塞和非阻塞两种模式',
                    'configureBlocking方法:true为阻塞模式',
                    '对应一个连接，两端都有一个负责传输的SocketChannel传输通道',
                    '在NIO中，2个涉及网络连接的通道：SocketChannel负责连接传输，ServerSocketChannel负责连接的监听',
                    'ServerSocketChannel应用于服务器端，而SocketChannel同时处于服务器端和客户端'
                ]},
                {'4个核心操作':[
                    {'获取SocketChannel传输通道':[
                        '客户端：先通过SocketChannel静态方法open()获得一个套接字传输通道',
                        '然后，将socket套接字设置为非阻塞模式',
                        '最后，通过connect()实例方法，对服务器的IP和端口发起连接',
                        '服务器：首先通过事件，获得服务器监听通道',
                        'accept()方法:获取新连接的套接字通道',
                        '将socket套接字设置为非阻塞模式'
                    ]},
                    '读取SocketChannel传输通道:同上',
                    '写入到SocketChannel传输通道:同上',       
                    {'关闭SocketChannel传输通道':[
                        'shutdownOutput()终止输出方法，向对方发送一个输出的结束标志（-1）',
                        '调用socketChannel.close()方法，关闭套接字连接'
                    ]}
                ]}
            ]},
            {'ServerSocketChannel服务器嵌套字通道（或服务器监听通道）':[
                '允许我们监听TCP连接请求，为每个监听到的请求，创建一个SocketChannel套接字通道',
                'NIO中的ServerSocketChannel监听通道，对应于OIO中的ServerSocket类'
            ]},
            {'DatagramChannel数据报通道':[
                {'定义':[
                    '用于UDP协议的数据读写'
                ]},
                {'4个核心操作':[
                    {'获取DatagramChannel数据报通道':[
                        '调用DatagramChannel类的open静态方法',
                        '调用configureBlocking（false）方法，设置成非阻塞模式',
                        '需要接收数据，还需要调用bind方法绑定一个数据报的监听端口'
                    ]},
                    {'读取DatagramChannel数据报通道数据':[
                        'receive（ByteBufferbuf）方法将数据从DatagramChannel读入，再写入到ByteBuffer缓冲区中',
                        '返回值，是SocketAddress类型，表示返回发送端的连接地址（包括IP和端口）'
                    ]},
                    {'写入DatagramChannel数据报通道':[
                        '调用send方法,需要指定接收方的地址（IP和端口）'
                    ]},
                    {'关闭DatagramChannel数据报通道':[
                        '调用close()方法'
                    ]}
                ]}
            ]}
        ]},
    ]},
    {'Selector选择器':[
        {'定义':[
            '通过选择器，一个线程可以查询多个通道的IO事件的就绪状态',
            '选择器和通道的关系，是监控和被监控的关系',
        ]},
        {'注册':[
            '通道和选择器之间的关系，通过Channel.register（Selector sel, int ops）方法完成注册',
            'register方法有两个参数：第一个参数，指定通道注册到的选择器实例；第二个参数，指定选择器要监控的IO事件类型'
        ]},
        {'SelectableChannel可选择通道':[
            '必须继承SelectableChannel类(提供了实现通道的可选择性所需要的公共方法)'
        ]},
        {'SelectionKey选择键':[
            '定义：那些被选择器选中的IO事件',
            {'作用':[
                '可以获得通道的IO事件类型，比方说SelectionKey.OP_READ',
                '获得发生IO事件所在的通道',
                '可以获得选出选择键的选择器实例'
            ]}
        ]},
        {'选择器使用流程':[
            {'1.获取选择器实例':[
                '选择器实例是通过调用静态工厂方法open()来获取的'
            ]},
            {'2.将通道注册到选择器中':[
                '调用通道的register()方法，将通道注册到了一个选择器上'
            ]},
            {'3.轮询感兴趣的IO就绪事件（选择键集合）':[
                '1.通过Selector选择器的select()方法，选出已经注册的、已经就绪的IO事件，保存到SelectionKey选择键集合中',
                '2.SelectionKey集合保存在选择器实例内部，是一个元素为SelectionKey类型的集合（Set）,调用选择器的selectedKeys()方法，可以取得选择键集合',
                '3.处理完成后，需要将选择键从这个SelectionKey集合中移除，防止下一次循环的时候，被重复的处理'
            ]}
        ]}
    ]}],
'Reactor反应器模式':[
    {'定义':[
        '高性能网络编程在设计和架构层面的基础模式',
        '反应器模式由Reactor反应器线程、Handlers处理器两大角色组成',
        {'Reactor反应器线程的职责':[
            '负责响应IO事件，并且分发到Handlers处理器'
        ]},
        {'Handlers处理器的职责':[
            '非阻塞的执行业务处理逻辑'
        ]}
    ]},
    {'常见的三种模式':[
        {'Connection Per Thread（一个线程处理一个连接）模式':[
            '对于每一个新的网络连接都分配给一个线程。每个线程都独自处理自己负责的输入和输出',
            '缺点是：对应于大量的连接，需要耗费大量的线程资源，对线程资源高'
        ]},
        {'单线程的Reactor反应器模式':[
            {'事件驱动模式':[
                '当有事件触发时，事件源会将事件dispatch分发到handler处理器进行事件处理'
            ]},
            {'定义':[
                'Reactor反应器和Handers处理器处于一个线程中执行'
            ]},
            {'2个重要的组件':[
                {'Reactor反应器':[
                    '负责查询IO事件，当检测到一个IO事件，将其发送给相应的Handler处理器去处理'
                ]},
                {'Handler处理器':[
                    '与IO事件（或者选择键）绑定，负责IO事件的处理',
                    '完成真正的连接建立、通道的读取、处理业务逻辑、负责将结果写出到通道等'
                ]}
            ]},
            {'两个重要的成员方法':[
                {'void attach(Object o)':[
                    '主要是将Handler处理器实例，作为附件添加到SelectionKey实例'
                ]},
                {'Object attachment()':[
                    '取出之前通过attach(Object o)添加到SelectionKey选择键实例的附件'
                ]}
            ]},
            {'IOHandler处理器的':[
                {'构造器':[
                    '1.将新的SocketChannel传输通道，注册到了反应器Reactor类的同一个选择器中。这样保证了Reactor类和Handler类在同一个线程中执行',
                    '2.Channel传输通道注册完成后，将IOHandler自身作为附件，attach到了选择键中。这样，在Reactor类分发事件（选择键）时，能执行到IOHandler的run方法'
                ]},
                {'两大职责':[
                    '接受新连接',
                    '为新连接创建一个输入输出的Handler处理器'
                ]}
            ]}
        ]},
        {'多线程的Reactor反应器模式':[
            {'改进的两方面':[
                '升级Reactor反应器:考虑引入多个Selector选择器，提升选择大量通道的能力',
                '升级Handler处理器:既要使用多线程，又要尽可能的高效率，考虑使用线程池'
            ]},
                        {'反应器':[
                '如果服务器为多核的CPU，可以将反应器线程拆分为多个子反应器（SubReactor）线程',
                '引入多个选择器，每一个SubReactor子线程负责一个选择器,提高反应器管理大量连接，选择大量通道的能力'
            ]},
            {'处理器':[
                '引入了一个线程池（ThreadPool），业务处理的代码执行在自己的线程池中，彻底地做到业务处理线程和反应器IO事件线程的完全隔离，避免服务器的连接监听受到阻塞'
            ]},

        ]}        
    ]},
    {'优点':[
        '响应快，虽然同一反应器线程本身是同步的，但不会被单个连接的同步IO所阻塞',
        '编程相对简单，最大程度避免了复杂的多线程同步，也避免了多线程的各个进程之间切换的开销',
        '可扩展，可以方便地通过增加反应器线程的个数来充分利用CPU资源'
    ]},
    {'缺点':[
        '反应器模式需要操作系统底层的IO多路复用的支持',
        '同一个Handler业务线程中，如果出现一个长时间的数据读写，会影响这个反应器中其他通道的IO处理。'
    ]}],
'并发基础中的Future异步回调模式':[
    {'join异步阻塞':[
        '应用场景：A线程调用B线程的join方法，等待B线程执行完成；在B线程没有完成前，A线程阻塞',
        '注意：join调用时，不是线程所指向的目标线程阻塞，而是当前线程阻塞，被合并的线程没有返回值'
    ]},
    {'FutureTask异步阻塞':[
        {'Callable接口':[
            '类似Runnable接口,更强大，有返回值'
        ]},
        {'Future接口':[
            {'定义':[
                '对并发任务的执行及获取其结果的一些操作'
            ]},
            {'3大功能':[
                '判断并发任务是否执行完成。',
                '获取并发的任务完成后的结果。',
                '取消并发执行中的任务'
            ]}
        ]},
        {'FutureTask类':[
            '实现了Future接口，提供了外部操作异步任务的能力',
            '内部封装一个Callable实例',
            '自身作为Thread线程的target',
            '一座搭在Callable实例与Thread线程实例之间的桥' 
        ]}
    ]},
    {'Guava的异步回调':[
        {'增强':[
            '1.引入接口ListenableFuture，继承了Java的Future接口，使得Java的Future异步任务在Guava中能被监控和获得非阻塞异步执行的结果',
            '2.引入接口FutureCallback，这是一个独立的新接口,目的是在异步任务执行完成后，根据异步结果，完成不同的回调处理，并且可以处理异步结果'
        ]},
        {'FutureCallback':[
            {'作用':[
                '用来填写异步任务执行完后的监听逻辑'
            ]},
            {'两个回调方法':[
                'onSuccess方法，在异步任务执行成功后被回调',
                'onFailure方法，在异步任务执行过程中，抛出异常时被回调'
            ]}
        ]},
        {'ListenableFuture':[
            'ListenableFuture异步任务实例获取：向Guava自己定制的线程池（ThreadPool）提交Callable任务的方式',
            {'Guava异步回调的流程':[
                '1.实现Java的Callable接口，创建异步执行逻辑',
                '2.创建Guava线程池(它是对Java线程池的一种装饰）',
                '3.将第1步创建的Callable/Runnable异步执行逻辑的实例，通过submit提交到Guava线程池，从而获取ListenableFuture异步任务实例',
                '4.创建FutureCallback回调实例，通过Futures.addCallback将回调实例绑定到ListenableFuture异步任务上'
            ]}
        ]},
        {'Futures工具类':[
            'addCallback静态方法:将FutureCallback的回调实例绑定到ListenableFuture异步任务'
        ]},
        {'与Java的FutureTask异步回调对比':[
            'Guava是非阻塞的异步回调，调用线程是不阻塞的，可以继续执行自己的业务逻辑',
            'FutureTask是阻塞的异步回调，调用线程是阻塞的，在获取异步结果的过程中，一直阻塞，等待异步线程返回结果'
        ]}
    ]},
    {'Netty的异步回调模式':[
        {'增强':[
            'Netty的Future接口,对Java的Future接口进行了增强',
            'GenericFutureListener接口，用于表示异步执行完成的监听器'
        ]},
        {'GenericFutureListener接口':[
            '回调方法：operationComplete,异步任务操作完成,Future异步任务执行完成后，将回调此方法'
        ]},
        {'Netty的Future接口':[
            'addListener():增加异步任务执行完成与否的监听器listener',
            '对执行的过程的进行监控，对异步回调完成事件进行监听（Listen）',
            'ChannelFuture的使用'
        ]}
    ]}],
'Netty原理与基础':[
    {'组件':[
        '服务器启动器',
        '缓冲区',
        '反应器',
        'Handler业务处理器',
        'Future异步任务监听',
        '数据传输通道'
    ]},
    {'Channel通道':[
        {'定义':[
            '反应器的查询和分发的IO事件的来源',
            '每一种通信连接协议，Netty都实现了自己的通道'
        ]},
        {'抽象类AbstractChannel':[
            {'构造器':[
                'parent属性:对于每一条传输通道（如NioSocketChannel实例），parent属性的值为接收到该连接的服务器连接监听通道',
                'pipeline属性:一条通过，一条流水线'
            ]},
            {'几个重要方法':[
                {'ChannelFuture connect(SocketAddress address)':[
                    '连接远程服务器,在客户端的传输通道使用'
                ]},
                {'ChannelFuture bind（SocketAddress address）':[
                    '绑定监听地址，开始监听新的客户端连接,在服务器的新连接监听和接收通道使用'
                ]},
                {'ChannelFuture close()':[
                    '关闭通道连接，返回连接关闭的ChannelFuture异步任务'
                ]},
                {'Channel read()':[
                    '读取通道数据，并且启动入站处理'
                ]},
                {'ChannelFuture write（Object o）':[
                    '启程出站流水处理'
                ]},
                {'Channel flush()':[
                    '将缓冲区中的数据立即写出到对端'
                ]}
            ]}
        ]},
        {'EmbeddedChannel（嵌入式通道）':[
            '模拟入站与出站的操作，底层不进行实际的传输，不需要启动Netty服务器和客户端,辅助测试使用'
        ]},
        {'NioSocketChannel类':[
            '继承自Java NIO的SelectableChannel',
            'TCP协议对应的传输通道类型',
            '对映服务器监听类NioServerSocketChannel'
        ]}
    ]},
    {'反应器':[
        {'定义':[
            '服务器通道新连接的IO事件的监听:一个反应器通过Selector选择器不断地查询注册过的IO事件（选择键）',
            '传输通道的IO事件:如果查询到IO事件，分发给Handler业务处理器',
            '为了及时接受（Accept）到新连接，在服务器端，一般有两个独立的反应器，一个反应器负责新连接的监听和接受，另一个反应器负责IO事件处理'
        ]},
        {'NioEventLoop':[
            '对应于NioSocketChannel通道',
            {'两个重要的成员属性':[
                'Thread线程类：负责一个Java NIO Selector选择器的IO事件轮询',
                'Java NIO选择器Selector类'
            ]}
        ]}
    ]},
    {'处理器':[
        {'涉及环节':[
            '数据包解码',
            '业务处理',
            '目标数据编码',
            '把数据包写到通道中'
        ]},
        {'分类':[
            '都继承了ChannelHandler处理器接口',
            {'ChannelInboundHandler通道入站处理器':[
                '默认实现为ChannelInboundHandlerAdapter(通道入站处理适配器)',
                'Handler业务处理器的各个方法的执行顺序和生命周期',
                {'主要操作':[
                    {'handlerAdded()':[
                        '当业务处理器被加入到流水线后，此方法被回调'
                    ]},
                    {'channelRegistered()':[
                        '当通道成功绑定一个NioEventLoop线程后，会通过流水线回调所有业务处理器的channelRegistered()方法'
                    ]},
                    {'channelActive()':[
                        '通道激活成功,所有的业务处理器添加、注册的异步任务完成，并且NioEventLoop线程绑定的异步任务完成'
                    ]},
                    {'channelRead()':[
                        '有数据包入站，通道可读'
                    ]},
                    {'channelReadComplete()':[
                        '流水线完成入站处理后'
                    ]},
                    {'channelInactive()':[
                        '当通道的底层连接已经不是ESTABLISH状态，或者底层连接已经关闭时'
                    ]},
                    {'channelUnregistered()':[
                        '通道和NioEventLoop线程解除绑定，移除掉对这条通道的事件处理之后'
                    ]},
                    {'handlerRemoved()':[
                        'Netty会移除掉通道上所有的业务处理器后'
                    ]} 
                ]}
            ]},
            {'ChannelOutboundHandler通道出站处理器':[
                '默认实现为ChanneloutBoundHandlerAdapter(通道出站处理适配器)',
                {'出站处理的方向':[
                    '通过上层Netty通道，去操作底层Java IO通道'
                ]},
                {'主要操作':[
                    {'bind()':[
                        '监听地址（IP+端口）绑定：完成底层Java IO通道的IP地址绑定,用于服务器端'
                    ]},
                    {'connect()':[
                        '连接服务端：完成底层Java IO通道的服务器端的连接操作,用于客户端'
                    ]},
                    {'write()':[
                        '写数据到底层：完成Netty通道向底层Java IO通道的数据写入操作'
                    ]},
                    {'flush()':[
                        '腾空缓冲区中的数据，把这些数据写到对端'
                    ]},
                    {'read()':[
                        '从底层读数据：完成Netty通道从Java IO通道的数据读取'
                    ]},
                    {'disConnect()':[
                        '断开服务器连接：断开底层Java IO通道的服务器端连接,主要用于客户端'
                    ]},
                    {'close()':[
                        '主动关闭通道：关闭底层的通道，例如服务器端的新连接监听通道'

                    ]}
                ]}
            ]},
            {'ChannelInitializer通道初始化处理器':[
                '属于入站处理器的类型,向流水线中装配业务处理器',
                {'initChannel()方法':[
                    '新连接通道作为参数，往它的流水线中装配Handler业务处理器'
                ]}
            ]}
        ]}
    ]},
    {'流水线（Pipeline）':[
        {'ChannelPipeline（通道流水线）':[
            '像一条管道，将绑定到一个通道的多个Handler处理器实例，串在一起，形成一条流水线',
            '基于责任链设计模式设计，内部是一个双向链表，支持动态地添加和删除Handler业务处理器'
        ]},
        {'ChannelHandlerContext上下文':[
            '在Handler业务处理器被添加到流水线中时创建，代表了ChannelHandler通道处理器和ChannelPipeline通道流水线之间的关联',
            {'作用':[
                '1.获取上下文所关联的Netty组件实例:如所关联的通道、所关联的流水线、上下文内部Handler业务处理器实例等',
                '2.入站和出站处理方法:只会从当前的节点开始执行Handler业务处理器，并传播到同类型处理器的下一站（节点）'
            ]}
        ]},
        {'Channel、Handler、ChannelHandlerContext三者的关系':[
            'Channel通道拥有一条ChannelPipeline通道流水线'
            '每一个流水线节点为一个ChannelHandlerContext通道处理器上下文对象'
            '每一个上下文中包裹了一个ChannelHandler通道处理器',
            '在ChannelHandler通道处理器的入站/出站处理方法中，Netty都会传递一个Context上下文实例作为实际参数',
            '通过Context实例的实参，在业务处理中，可以获取ChannelPipeline通道流水线的实例或者Channel通道的实例'
        ]},
        {'截断流水线':[
            {'入站':[
                '在channelRead方法中，不再调用父类的channelRead入站方法或不调用ctx.fireChannelXxx()'
            ]},
            {'出站':[
                '流程只要开始执行，就不能被截断。强行截断的话，Netty会抛出异常。如果业务条件不满足，可以不启动出站处理'
            ]}
        ]},
        {'Handler业务处理器的热拔插':[
            '动态地增加、删除流水线上的业务处理器Handler'
        ]}
    ]},
    {'Bootstrap启动器类':[
        {'作用':[
            '一个组装和集成器，将不同的Netty组件组装在一起',
            '为组件设置好对应的参数，最后实现Netty服务器的监听和启动'
        ]},
        {'分类':[
            'ServerBootstrap:server专用',
            'Bootstrap:client专用'
        ]},
        {'父子通道':[
            {'定义':[
                '有接收关系的NioServerSocketChannel和NioSocketChannel'
            ]},
            {'父通道（ParentChannel）':[
                'NioServerSocketChannel负责服务器连接监听和接收'
            ]},
            {'子通道（ChildChannel）':[
                '对应于每一个接收到的NioSocketChannel传输类通道'
            ]}
        ]},
        {'EventLoopGroup线程组':[
            '一个多线程版本的反应器'
        ]},
        {'服务器端启动器的使用':[
            '1.创建反应器线程组，并赋值给ServerBootstrap启动器实例',
            '2.设置通道的IO类型',
            '3.设置监听端口',
            '4.设置传输通道的配置选项',
            '5.装配子通道的Pipeline流水线',
            '6.开始绑定服务器新连接的监听端口',
            '7.自我阻塞，直到通道关闭',
            '8.关闭EventLoopGroup'
        ]},
        {'ChannelOption通道选项':[
            '1．SO_RCVBUF, SO_SNDBUF'
            '2.TCP_NODELAY:立即发送数据',
            '3．SO_KEEPALIVE:底层TCP协议的心跳机制',
            '4．SO_REUSEADDR:地址复用'
        ]}
    ]},
    {'ByteBuf缓冲区':[
        {'定义':[
            '一个字节容器，内部是一个字节数组'
        ]},
        {'逻辑分类':[
            '废弃',
            '可读',
            '可写',
            '可扩容'
        ]},
        {'AbstractByteBuf抽象类':[
            {'属性':[
                {'readerIndex（读指针）':[
                    '指示读取的起始位置,readerIndex与writerIndex相等，则表示ByteBuf不可读了'
                ]},
                {'writerIndex（写指针）':[
                    '写入的起始位置,writerIndex与capacity()容量相等，则表示ByteBuf已经不可写了'
                ]},
                'maxCapacity（最大容量'
            ]},
            {'方法':[
                {'容量系列':[
                    'capacity()：表示ByteBuf的容量',
                    'maxCapacity()：表示ByteBuf最大能够容纳的最大字节数'
                ]},
                {'写入系列':[
                    'isWritable() ：ByteBuf是否可写,false，并不代表不能再往ByteBuf中写数据了,ByteBuf是可以扩容的',
                    'writableBytes() ：取得可写入的字节',
                    'writeBytes(byte[] src) ：把src字节数组中的数据全部写到ByteBuf',
                    'markWriterIndex()与resetWriterIndex()：实现覆盖写'
                ]},
                {'读取系列':[
                    'isReadable( ) ：ByteBuf是否可读',
                    'readableBytes( ) ：ByteBuf当前可读取的字节数',
                    'readBytes(byte[] dst)：读取ByteBuf中的数据,将数据从ByteBuf读取到dst字节数组中，这里dst字节数组的大小，通常等于readableBytes()',
                    'markReaderIndex( )与resetReaderIndex( ) ：实现重复读'
                ]}
            ]}
        ]},
        {'ByteBufe的内存回收':[
            '通过引用计数的方式管理的(对Pooled ByteBuf的支持)'
        ]},
        {'ByteBufAllocato分配器':[
            {'定义':[
                '创建缓冲区和分配内存空间',
                '默认的分配器为ByteBufAllocator.DEFAULT,可以通过Java系统参数（SystemProperty）的选项io.netty.allocator.type进行配置'
            ]},
            {'两种实现':[
                'PoolByteBufAllocator:将ByteBuf实例放入池中,采用了jemalloc高效内存分配的策略',
                'UnpooledByteBufAllocator:通过Java的垃圾回收机制回收'
            ]},
            {'分配器分配ByteBuf的方法':[
                '初始容量为9，最大容量100的缓冲区:ByteBufAllocator.DEFAULT.buffer(9, 100)',
                '初始容量为256，最大容量Integer.MAX_VALUE的缓冲区:ByteBufAllocator.DEFAULT.buffer()'
            ]}
        ]},
        {'缓冲区的类型':[
                '堆缓存区',
                '直接缓存区:使用堆外内存',
                '组合缓存区'
        ]},
        {'ByteBuf的自动释放':[
            {'入站的ByteBuf':[
                {'TailHandler自动释放':[
                    'Netty默认会在ChannelPipline通道流水线的最后添加一个TailHandler末尾处理器',
                    '它实现了默认的处理方法，在这些方法中会帮助完成ByteBuf内存释放的工作'
                ]},
                {'SimpleChannelInboundHandler自动释放':[
                    '继承SimpleChannelInboundHandler,它会在调用完实际的channelRead()方法后，帮忙释放ByteBuf实例'
                ]},
                {'手动释放ByteBuf':[
                    '调用byteBuf.release()'
                ]}
            ]},
            {'出站的ByteBuf':[
                'HeadHandler自动释放'
            ]}
        ]},
        {'ByteBuf的浅层复制':[
            'slice切片浅层复制',
            'duplicate整体浅层复制'
        ]}
    ]}],
# 'Decoder与Encoder重要组件':[
#     {'解码器':[
#         {'定义':[
#             '将输入类型为ByteBuf缓冲区,或者Java POJO对象的数据进行解码，输出一个一个的Java POJO对象',
#             'Inbound入站处理器类型'
#         ]},
#         {'ByteToMessageDecoder类':[
#             'decode方法:由子类来实现，将解码后得到的Object，加入到父类传递过来的List<Object>实参中',
#             'decode方法处理完成后，基类会继续后面的传递处理：将List<Object>结果列表中所得到的Object，一个一个地传递到下一个Inbound入站处理器',
#             '会自动调用ReferenceCountUtil.release(in)方法释放ByteBuf缓冲区的内存'
#         ]},
#         {'ReplayingDecoder解码器':[
#             {'作用':[
#                 '内部定义了一个新的二进制缓冲区类，对ByteBuf缓冲区进行了装饰，名为ReplayingDecoderBuffer',
#                 '在读取ByteBuf缓冲区的数据之前，会检查缓冲区是否有足够的字节',
#                 '若ByteBuf中有足够的字节，则会正常读取；反之，如果没有足够的字节，则会停止解码',
#                 '适用于分包传输的应用场景'
#             ]},
#             {'state成员属性':[
#                 '保存当前解码器在解码过程中的当前阶段'
#             ]},
#             {'字符串的分包解码':[
#                 {'可以采用普通的Header-Content内容传输协议':[
#                     '1.在协议的Head部分放置字符串的字节长度。Head部分可以用一个整型int来描述',
#                     '2.在协议的Content部分，放置字符串的字节数组'
#                 ]},
#                 '在实际的传输过程中，一个Header-Content内容包，在发送端会被编码成为一个ByteBuf内容发送包'
#             ]},
#             {'缺点':[
#                 '数据解析逻辑复杂的应用场景，性能较差'
#             ]}
#         ]},
#         {'MessageToMessageDecoder<I>':[
#             '将一种POJO对象解码成另外一种POJO对象',
#             '泛型实参<I>,作用就是指定入站消息Java POJO类型'
#         ]},
#         {'Netty内置Decoder':[
#             '固定长度数据包解码器——FixedLengthFrameDecoder',
#             '行分割数据包解码器——LineBasedFrameDecoder',
#             '自定义分隔符数据包解码器——DelimiterBasedFrameDecoder',
#             {'自定义长度数据包解码器——LengthFieldBasedFrameDecoder':[
#                 '基于Header-Content协议的内容传输，尽量使用它',
#                 {'5个参数':[
#                     'maxFrameLength：发送的数据包的最大长度',
#                     'lengthFieldOffset：长度字段偏移量',
#                     'lengthFieldLength：长度字段所占的字节数',
#                     'lengthAdjustment：长度的矫正值',
#                     'initialBytesToStrip：丢弃的起始字节数'
#                 ]}
#             ]}
#         ]}
#     ]},
#     {'Encoder编码器':[
#         {'定义':[
#             '一个Outbound出站处理器，负责处理“出站”数据',
#             '负责将“出站”的某种Java POJO对象编码成二进制ByteBuf，或者编码成另一种Java POJO对象'
#         ]},
#         {'MessageToByteEncoder编码器':[
#             'encode方法:由子类来实现'
#         ]},
#         {'MessageToMessageEncoder<I>':[
#             '将一种POJO对象解码成另外一种POJO对象',
#             '泛型实参<I>。这个实参的作用就是指定入站消息Java POJO类型',
#             '现它的encode抽象方法'
#         ]},
#     ]},
#     {'解码器和编码器的结合':[
#         {'ByteToMessageCodec编解码器':[
#             '包含ByteToMessageDecoder解码器和MessageToByteEncoder编码器这两个基类',
#             '包含了编码encode和解码decode两个抽象方法'
#         ]},
#         {'MessageToMessageCodec（编解码器）':[
#             '包含MessageToMessageEncoder编码器和MessageToMessageDecoder解码器',
#             '包含了编码encode和解码decode两个抽象方法'
#         ]},
#         'CombinedChannelDuplexHandler组合器'
#     ]}],
# '序列化':[
#     {'粘包和拆包':[
#         {'原因':[
#             '发送端Netty的应用层进程缓冲区，程序以ByteBuf为单位来发送数据，',
#             '到了底层操作系统内核缓冲区，底层会按照协议的规范对数据包进行二次拼装，拼装成传输层TCP层的协议报文，再进行发送',
#             '接收端收到传输层的二进制包后，首先保存在内核缓冲区，Netty读取ByteBuf时才复制到进程缓冲区'
#         ]}
#     ]},
#     {'分包':[
#         {'定义':[
#             '在接收端，Netty程序需要根据自定义协议',
#             '将读取到的进程缓冲区ByteBuf，在应用层进行二次拼装，重新组装我们应用层的数据包',
#         ]},
#         {'方法':[
#             '可以自定义解码器分包器：基于ByteToMessageDecoder或者ReplayingDecoder，定义自己的进程缓冲区分包器',
#             '使用Netty内置的解码器。如使用Netty内置的LengthFieldBasedFrameDecoder自定义分隔符数据包解码器，对进程缓冲区ByteBuf进行正确的分包'
#         ]}
#     ]},
#     {'JSON':[
#         'Java处理JSON数据有三个比较流行的开源类库有：阿里的FastJson、谷歌的Gson和开源社区的Jackson',
#         {'JSON传输的编码器和解码器之原理':[
#             '入站',
#             '先使用LengthFieldBasedFrameDecoder（Netty内置的自定义长度数据包解码器）解码Head-Content二进制数据包，解码出Content字段的二进制内容',
#             '然后，使用StringDecoder字符串解码器（Netty内置的解码器）将二进制内容解码成JSON字符串',
#             '最后，使用JsonMsgDecoder解码器（一个自定义解码器）将JSON字符串解码成POJO对象'
#         ]}
#     ]},
#     {'Protobuf协议通信':[
#         {'Protobuf的编码过程':[
#             '使用预先定义的Message数据结构将实际的传输数据进行打包',
#             '然后编码成二进制的码流进行传输或者存储'
#         ]},
#         {'优点':[
#             'Protobuf数据包是一种二进制的格式，相对于文本格式的数据交换（JSON、XML）来说，速度要快很多',
#             '优异的性能，使得它更加适用于分布式应用场景下的数据通信或者异构环境下的数据交换'
#         ]},
#         {'proto文件':[
#             '一个消息的协议文件，这个协议文件的后缀文件名为“.proto”',
#             'Protobuf使用proto文件来预先定义的消息格式。数据包是按照proto文件所定义的消息格式完成二进制码流的编码和解码',
#             {'内容':[
#                 '头部声明',
#                 '消息结构体的定义'
#             ]},
#             'Maven插件生成POJO和Builder',
#             {'序列化serialization & 反序列化Deserialization':[
#                 '通过字节数组',
#                 '通过流',
#                 '通过流+序列化的字节码之前添加了字节数组的长度，类似于前面介绍的Head-Content协议'
#             ]}
#         ]}
#     ]},
#     {'Netty自带的ProtoBuf编/解码器':[
#         'ProtobufDecoder解码器',
#         'ProtobufEncoder编码器',
#         'ProtobufVarint32FrameDecoder解码器',
#         'ProtobufVarint32LengthFieldPrepender编码器'
#     ]},
#     {'解析复杂的Head-Content协议就需要自定义Protobuf编/解码器，需要开发者自己去解决半包问题':[
#         '继承netty提供的MessageToByteEncoder编码器，完成Head-Content协议的复杂数据包的编码，将Protobuf POJO编码成Head-Content协议的二进制ByteBuf数据包',
#         '继承netty提供的ByteToMessageDecoder解码器，完成Head-Content协议的复杂数据包的解码，将二进制ByteBuf数据包最终解码出Protobuf POJO实例'
#     ]}],
# '基于Netty的单体IM系统的开发实践':[
#     {'通信数据包':[
#         '魔数可以理解为通信的口令',
#         '版本号:如果在程序中有协议升级的需求，又需要同时兼顾新旧版本的协议，就会用这个版本号'
#     ]},
#     {'IM系统中Protobuf消息格式的设计':[
#         '消息类型使用enum定义',
#         '使用一个Protobufmessage结构定义一类消息',
#         '建议给应答消息加上成功标记和应答序号',
#         '编解码从顶层消息开始'
#     ]},
#     {'客户端会话ClientSession、服务端会话ServerSession':[
#         {'导航关系有两个方向':[
#             {'正向导航':[
#                 '通过会话导航到通道，主要用于出站处理的场景，通过会话将数据包写出到通道'
#             ]},
#             {'反向导航  ':[
#                 '通过通道导航到会话，主要用于入站处理的场景，通过通道获取会话，以便进一步进行业务处理'
#             ]}
#         ]},
#         {'通道的容器属性':[
#             {'Attribute':[
#                 'Attribute的设值:attr().set()',
#                 'Attribute的取值:attr().get()'
#             ]}
#         ]},
#         'ServerSession服务器端会话类:每个ServerSession实例都拥有一个唯一标识，为sessionId',
#         'SessionMap会话管理器'
#     ]},
#     {'心跳检测':[
#         {'网络连接的假死':[
#             '如果底层的TCP连接已经断开，但是服务器端并没有正常地关闭套接字，服务器端认为这条TCP连接仍然是存在的',
#             {'解决假死的有效手段':[
#                 '客户端定时进行心跳检测，服务器端定时进行空闲检测'
#             ]}
#         ]},
#         {'客户端的心跳报文':[
#             '客户端定期发送数据包到服务器端的数据包'
#         ]},
#         {'服务器端的空闲检测':[
#             '每隔一段时间，检测子通道是否有数据读写，如果有，则子通道是正常的；如果没有，则子通道被判定为假死，关掉子通道',
#             {'实现':[
#                 'Netty自带的IdleStateHandler空闲状态处理器'
#             ]}
#         ]}
#     ]}],
# 'ZooKeeper分布式协调':[
#     {'环境搭建':[
#         '1.创建数据目录和日志目录',
#         '2.创建myid文件:存放在数据目录下，内容只能是一个数字',
#         {'3.创建和修改配置文件“.cfg”':[
#             '前面准备的日志目录和数据目录',
#             '端口信息clientPort',
#             {'节点信息':[
#                 '配置集群中所有节点的（id）编号、IP地址和端口号',
#                 'server.id=host:port:port,前一个端口用于节点之间的通信，后一个端口用于选举主节点',
#                 {'ZooKeeper节点数要求':[
#                     'ZooKeeper集群节点数必须是奇数',
#                     'ZooKeeper集群至少是3个'
#                 ]}
#             ]},
#             {'时间相关选项':[
#                 {'tickTime':[
#                     '配置单元时间,默认值为3000，单位是毫秒（ms）'
#                 ]},
#                 {'initLimit':[
#                     '节点的初始化时间,用于Follower（从节点）的启动，并完成与Leader（主节点）进行数据同步的时间'
#                 ]},
#                 {'syncLimit':[
#                     '心跳最大延迟周期,用于配置Leader节点和Follower节点之间进行心跳检测的最大延时时间'
#                 ]}
#             ]}
#         ]},
#         {'4.启动':[
#             '为每一个节点制作一份启动命令".cmd"文件'
#         ]}
#     ]},
#     {'存储模型':[
#         {'定义':[
#             '一棵以 "/" 为根节点的树',
#             '每一个节点，叫作ZNode（ZooKeeper Node）节点',
#             '每个ZNode节点都用一个以 "/"（斜杠）分隔的完整路径来唯一标识',
#             '整个树形的目录结构全部都放在内存中',
#             '每个节点存放的有效负载数据（Payload）的上限仅为1MB'
#         ]},
#         {'zkCli客户端命令清单':[
#             'create:创建znode路径节点',
#             'ls:查看目录下的节点',
#             'get',
#             'set',
#             'delete'
#         ]},
#         'ZNode节点信息的主要属性',
#         {'ZooKeeper应用开发,通过Java客户端API去连接和操作ZooKeeper集群':[
#             'ZooKeeper官方的Java客户端API',
#             '第三方的Java客户端API:ZkClient',
#             '第三方的Java客户端API:Curator'
#         ]}
#     ]},
#     {'Curator':[
#         {'三个主要的模块':[
#             {'curator-framework':[
#                 '对ZooKeeper的底层API的一些封装'
#             ]},
#             {'curator-client':[
#                 '提供了一些客户端的操作，例如重试策略等'
#             ]},
#             {'curator-recipes':[
#                 '封装了一些高级特性，如：Cache事件监听、选举、分布式锁、分布式计数器、分布式Barrier等'
#             ]}
#         ]},
#         {'基本操作':[
#             {'Curator客户端实例的创建':[
#                 '1.使用工厂类CuratorFrameworkFactory的静态newClient()方法',
#                 '2.使用工厂类CuratorFrameworkFactory的静态builder构造者方法'
#             ]},
#             {'创建ZNode节点':[
#                 '一般使用链式调用来完成节点的创建',
#                 'client.create().creatingParentsIfNeeded().withMode(CreateMode.PERSISTENT).forPath("/test/CRUD/node-1", "hello".getBytes("UTF-8"))'
#             ]},
#             {'读取节点':[
#                 '首先是判断节点是否存在，调用checkExists方法',
#                 '其次是获取节点的数据，调用getData方法',
#                 '最后是获取子节点列表，调用getChildren方法'
#             ]},
#             {'更新节点':[
#                 'setData()方法进行同步更新',
#                 'inBackground(AsyncCallback callback)方法，设置一个AsyncCallback回调实例,将更新数据的行为从同步执行变成了异步执行'
#             ]},
#             {'删除节点':[
#                 'delete()'
#             ]}
#         ]},
#         {'对ZooKeeper服务器端的事件监听':[
#             {'事件监听有两种模式':[
#                 {'标准的观察者模式':[
#                     '通过Watcher监听器实现',
#                     '只能监听一次'
#                 ]},
#                 {'缓存监听模式':[
#                     '引入了一种本地缓存视图Cache机制去实现',
#                     '事件监听的种类有3种：Path Cache,Node Cache和Tree Cache'
#                 ]}
#             ]},
#             {'接口类型Watcher':[
#                 '一个标准的事件处理器，用来定义收到事件通知后相关的回调处理逻辑',
#                 '事件回调方法：process（WatchedEvent event）',
#                 {'Watcher监听器实例向服务器端注册':[
#                     '通过GetDataBuilder、GetChildrenBuilder和ExistsBuilder等这类实现了Watchable<T>接口的构造者',
#                     '使用构造者的usingWatcher(Watcher w)方法，为构造者设置Watcher监听器实例',
#                     '例子：client.getData().usingWatcher(w).forPath("/test/CRUD/node-1")'
#                 ]}, 
#                 {'WatchedEvent包含了三个基本属性':[
#                     '通知状态（keeperState）',
#                     '事件类型（EventType）',
#                     '节点路径（path）'
#                 ]}
#             ]},
#             {'NodeCache节点缓存的监听':[
#                 {'分类':[
#                     'Node Cache节点缓存可用于ZNode节点的监听',
#                     'Path Cache子节点缓存可用于ZNode的子节点的监听',
#                     'Tree Cache树缓存是Path Cache的增强，不光能监听子节点，还能监听ZNode节点自身'
#                 ]},
#                 {'步骤':[
#                     '1.构造一个NodeCache缓存实例',
#                     '2.构造一个NodeCacheListener监听器实例,回调方法nodeChanged()',
#                     '3.将NodeCacheListener的实例注册到NodeCache缓存实例，使用缓存实例的addListener方法',
#                     '4.使用缓存实例nodeCache的start方法来启动节点的事件监听'
#                 ]},
#                 {'原理':[
#                     'Node Cache用来观察ZNode自身，如果ZNode节点本身被创建，更新或者删除，那么Node Cache会更新缓存，并触发事件给注册的监听器',
#                     'Node Cache是通过NodeCache类来实现的，监听器对应的接口为NodeCacheListener'
#                 ]}

#             ]}
#         ]}
#     ]},
#     {'分布式命名服务':[
#         {'场景':[
#             '分布式API目录',
#             '分布式的ID生成器',
#             '分布式节点的命名'
#         ]},
#         {'ID生成器方案':[
#             {'Java的UUID':[
#                 '经由一定的算法机器生成的,是本地生成的ID，不需要进行远程调用，时延低，性能高',
#                 '缺点是过长，16字节共128位，通常以36字节长的字符串来表示，同时没有排序，无法保证趋势递增，因此用于数据库索引字段的效率就很低，添加记录存储入库时性能差'
#             ]},
#             {'分布式缓存Redis生成ID':[
#                 '利用Redis的原子操作INCR和INCRBY，生成全局唯一的ID'
#             ]},
#             {'Twitter的SnowFlake算法':[
#                 '生成的ID是一个64bit的长整型数字,可以使用ZK实现SnowFlakeID算法',
#                 '优点:在内存生成，高性能和高可用性,容量大,ID呈趋势递增，后续插入数据库的索引树时，性能较高',
#                 '缺点：依赖于系统时钟的一致性，如果某台机器的系统时钟回拨了，有可能造成ID冲突，或者ID乱序'
#             ]},
#             {'ZooKeeper生成ID':[
#                 '利用ZooKeeper的顺序节点，生成全局唯一的ID'
#             ]},
#             {'MongoDb的ObjectId':[
#                 'MongoDB是一个分布式的非结构化NoSQL数据库，每插入一条记录会自动生成全局唯一的一个“_id”字段值，它是一个12字节的字符串，可以作为分布式系统中全局唯一的ID'
#             ]}
#         ]}
#     ]},
#     {'分布式锁':[
#         '可重入的公平锁',
#         {'ZooKeeper分布式锁':[
#             {'原理':[
#                 '一个ZooKeeper分布式锁，首先需要创建一个父节点，尽量是持久节点（PERSISTENT类型）',
#                 '然后每个要获得锁的线程都在这个节点下创建个临时顺序节点',
#                 '由于Zk节点是按照创建的顺序依次递增的，为了确保公平，可以简单地规定，编号最小的那个节点表示获得了锁',
#                 '因此，每个线程在尝试占用锁之前，首先判断自己的排号是不是当前最小的，如果是，则获取锁'
#             ]},
#             {'优点':[
#                 'ZooKeeper的每一个节点都是一个天然的顺序发号器',
#                 'ZooKeeper节点的递增有序性可以确保锁的公平',
#                 'ZooKeeper的节点监听机制可以保障占有锁的传递有序而且高效',
#                 'ZooKeeper的临时顺序节点,能保证由于网络异常或者其他原因造成集群中占用锁的客户端失联时，锁能够被有效释放。',
#                 'ZooKeeper的节点监听机制能避免羊群效应:当一个节点挂掉，只有它后面的那一个节点才作出反应'
#             ]},
#             {'缺点':[
#                 '性能不太高:每次在创建锁和释放锁的过程中，都要动态创建、销毁暂时节点来实现锁功能',
#                 'Zk中创建和删除节点只能通过Leader（主）服务器来执行，然后Leader服务器还需要将数据同步到所有的Follower（从）服务器上，频繁的网络通信'
#             ]},
#             {'基于ZooKeeper实现一下分布式锁':[
#                 '1.一把锁，使用一个ZNode节点表示，如果锁对应的ZNode节点不存在，那么先创建ZNode节点',
#                 '2.抢占锁的所有客户端，使用锁的ZNode节点的子节点列表来表示；如果某个客户端需要占用锁，则在“/test/lock”下创建一个临时有序的子节点',
#                 '3.客户端创建子节点后,判断自己创建的子节点是否为当前子节点列表中序号最小的子节点。如果是，则认为加锁成功；如果不是，则监听前一个ZNode子节点的变更消息，等待前一个节点释放锁',
#                 '4.一旦队列中后面的节点获得前一个子节点的变更通知，进行判断自己是否为当前子节点列表中序号最小的子节点，如果是，则认为加锁成功；如果不是，则持续监听，一直到获得锁',
#                 '5.获取锁后，开始处理业务流程。在完成业务流程后，删除自己对应的子节点，完成释放锁的工作，以便后面的节点能捕获到节点的变更通知，获得分布式锁'
#             ]},
#             'Curator的InterProcessMutex可重入锁'
#         ]} 
#     ]}],
# '分布式缓存Redis':[
#     {'Jedis':[
#         '一个高性能的Java客户端，是Redis官方推荐的Java开发工具',
#         '一个Jedis对象代表一条和Redis服务进行连接的Socket通道'
#     ]},
#     {'JedisPool连接池':[
#         {'大连接数maxTotal':[
#             '业务QPS/单连接的QPS = 最大连接数',
#             '在实际的生产场景中，还要预留一些资源，通常来讲所配置的maxTotal要比理论值大一些',
#             '如果连接数确实太多，可以考虑Redis集群，那么单个Redis节点的最大连接数的公式为：maxTotal = 预估的连接数 / nodes节点数'
#         ]},
#         {'maxIdle实际上才是业务可用的最大连接数':[
#             '使得连接池达到最佳性能的设置是maxTotal = maxIdle',
#             '尽可能避免由于频繁地创建和销毁Jedis连接所带来的连接池性能的下降'
#         ]},
#         '刚创建好的连接池，以最小空闲数量为JedisPool进行预热',
#         '由于Jedis类实现了java.io.Closeable接口，故而在JDK 1.7或者以上版本中可以使用try-with-resources语句，在其隐藏的finally部分自动调用close方法'
#     ]},
#     {'spring-data-redis':[
#         '在Maven的pom文件中加上spring-data-redis库的依赖',
#         '配置spring-data-redis库的连接池实例和RedisTemplate模板实例',
#         'RedisTemplate模板API'
#     ]},
#     {'SpringEL':[
#         'Spring Expression Language,提供一种强大、简洁的Spring Bean的动态操作表达式',
#         'JSP页面的表达式使用${}进行声明。而SpringEL表达式使用#{}进行声明',
#         '一般来说，SpringEL表达式使用#{}进行声明。但是，不是所有注解中的SpringEL表达式都需要#{}进行声明'
#     ]}],
# '高并发IM架构的理论基础':[
#     {'技术选型':[
#         'Netty4.x + spring4.x + ZooKeeper 3.x + redis 3.x + rocketMQ 3.x+ mysql 5.x+ monggo3.x',
#         {'短连接spring cloud':[
#             '客户端向服务器发起连接，服务器接受客户端连接，在三次握手之后，双方建立连接',
#             '客户端与服务器完成一次读写，发送数据包并得到返回的结果之后，通过客户端和服务器的四次握手断开连接',
#             '短连接服务器也叫Web服务器，主要功能是实现用户的登录鉴权和拉取好友、群组、数据档案等相对低频的请求操',
#             '扩展：短连接Web网关（WebGate），代理大量的Web服务器，从而无感知地实现短连接的高并发，可以使用SpringCloud或者Dubbo等分布式Web技术'
#         ]},
#         {'长连接 Netty':[
#             '客户端向服务器发起连接，服务器接受客户端的连接，双方建立连接',
#             '客户端与服务器完成一次读写之后，它们之间的连接并不会主动关闭，后续的读写操作会继续使用这个连接',
#             'TCP协议的连接过程是比较烦琐的，建立连接是需要三次握手的，而释放则需要4次握手，所以说每个连接的建立都需要消耗资源和时间',
#             '长连接服务器也叫IM即时通信服务器，主要作用就是用来和客户端建立并维持长连接，实现消息的传递和即时的转发',
#             '扩展：基于ZooKeeper或者其他的分布式协调中间件，可以非常方便、轻松地实现一个IM服务器集群的管理'
#         ]},
#         '序列化协议选型:Protobuf'
#     ]},
#     {'集群的负载均衡之实践案例':[
#         '1. IM节点的POJO类ImNode,有属性id,balance(netty的服务联接数)',
#         '2. IM节点的ImWorker类：所有的工作节点都在ZooKeeper的同一个父节点下，创建顺序节点。然后从返回的临时路径上，取得属于自己的那个后缀的编号',
#         '3. ImLoadBalance负载均衡器：将计算最佳Netty服务器的算法，放在负载均衡器中',
#         '4. 与短连接网关WebGate整合'
#     ]},
#     {'即时通信消息的路由和转发的实践案例':[
#         '如果连接在不同的Netty Worker工作站点的客户端之间，需要相互进行消息的发送，那么就需要在不同的Worker节点之间进行路由和转发',
#         {'Worker节点的路由':[
#             '根据消息需要转发的目标用户，找到用户的连接所在的Worker节点',
#             '由于节点和节点之间都有可能需要相互转发，因此节点之间的连接是一种网状结构,每一个节点都需要具备路由的能力'
#         ]},
#         {'实现':[
#             {'1.IM路由器WorkerRouter:为每一个Worker节点增加一个IM路由器类':[
#                 '要订阅到集群中所有的在线Netty服务器，即监控所有子节点（netty节点）',
#                 '将远程节点信息封装在转发器中，并用一个map来维护'
#             ]},
#             {'2.IM转发器WorkerReSender':[
#                 '封装了远程节点的IP地址、端口号以及ID',
#                 '维持了一个到远程节点的长连接,可以想像IM转发器是一个Netty的客户端，通过Netty channel通道将消息发送到远程节点'
#             ]}
#         ]}
#     ]},
#     {'Feign短连接RESTful调用':[
#         '短连接的服务接口都是基于应用层HTTP协议的HTTP API或者RESTful API实现的，通过JSON文本格式返回数据',
#         {'四种方式':[
#             'JDK原生的URLConnection',
#             'Apache的HttpClient / HttpComponents',
#             'Netty的异步HttpClient',
#             'Spring的RestTemplate'
#         ]},
#         {'Feign':[
#             'Netflix开发的一个声明式、模板化的HTTP客户端，可以进行同接口多服务器的负载均衡'
#         ]}
#     ]},
#     {'分布式的在线用户统计的实践案例':[
#         {'Curator的分布式计数器':[
#             '用int类型来计数（SharedCount）',
#             '用long类型来计数（DistributedAtomicLong）'
#         ]}
#     ]}]  
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
                t11 = t1.addSubTopic()
                t11.setTopicHyperlink(t1.getID()) 
                t11.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTopicHyperlink(t11.getID()) 
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTopicHyperlink(t111.getID()) 
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t11111 = t1111.addSubTopic()
                                                    t11111.setTopicHyperlink(t1111.getID()) 
                                                    t11111.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t111111 = t11111.addSubTopic()
                                                                t111111.setTitle(u)
                                                                for y in p[u]:
                                                                    t1111111 = t111111.addSubTopic()
                                                                    t1111111.setTitle(y)
                                                        else:
                                                            t111111 = t11111.addSubTopic()
                                                            t111111.setTopicHyperlink(t11.getID()) 
                                                            t111111.setTitle(p)                                                        
                                            else:
                                                t11111 = t1111.addSubTopic()
                                                t11111.setTopicHyperlink(t111.getID()) 
                                                t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTopicHyperlink(t111.getID()) 
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTopicHyperlink(t11.getID()) 
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTopicHyperlink(t1.getID()) 
            t11.setTitle(i) 


topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\netty.xmind") 