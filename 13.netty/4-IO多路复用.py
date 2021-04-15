import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IO多路复用")
r2=s2.getRootTopic()
r2.setTitle("IO多路复用")


content={
'四个步骤':[
    {'1.选择器注册':[
        '将需read操作的socket连接，提前注册到select/epoll选择器中（Java对应的选择器类是Selector类）'
    ]},
    {'2.就绪状态轮询':[
        '通过选择器的查询方法，查询注册过的所有socket连接的就绪状态，内核会返回一个就绪的socket列表'
    ]},
    {'3.用户线程发起read系统调用':[
        '用户线程获得了就绪状态的列表后，根据其中的socket连接，发起read系统调用',
        '用户线程阻塞，内核开始复制数据，将数据从【内核缓冲区】复制到【用户缓冲区】'
    ]},
    '4.复制完成后，内核返回结果，用户线程解除阻塞的状态'
],
'select函数':[
    '将一个文件描述符的数组发给操作系统，让操作系统去遍历，确定哪个文件描述符可以读写，然后告诉我们去处理',
    {'注意':[
        'select函数返回后，用户依然需遍历提交给操作系统的list',
        '只不过，操作系统会将准备就绪的文件描述符做上标识，用户层只会存在有意义的系统调用开销'
    ]},
],
'pollt函数':[
    '和select的主要区别:去掉了select只能监听1024个文件描述符的限制'
],
'优化':[
    {'1.select调用需传入fd数组，需拷贝一份到内核，高并发场景下拷贝消耗资源':[
        '优化为不复制'
    ]},
    {'2.select在内核层仍通过遍历方式检查文件描述符的就绪状态，是个同步过程，只不过无系统调用切换上下文的开销':[
        '内核层优化为异步事件通知'
    ]},
    {'3.select仅返回可读文件描述符的个数，具体哪个可读还要用户自己遍历':[
        '优化为只返回给用户就绪的文件描述符，无需用户做无效的遍历'
    ]}
],
'epollt函数':[
    '1.内核中保存一份文件描述符集合,无需用户每次都重新传入,只需告诉内核修改的部分即可------优化为不复制',
    '2.内核不再通过轮询方式找到就绪的文件描述符,而是通过异步IO事件唤醒--------------------内核层优化为异步事件通知',
    '3.内核仅将有IO事件的文件描述符返回给用户,用户无需遍历整个文件描述符集合--------------只返回给用户就绪的文件描述符',
    {'三个函数':[
        '1.创建一个epoll句柄：int epoll_create(int size);',
        '2.向内核添加、修改或删除要监控的文件描述符：int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);',
        '3.发起类似select()调用：int epoll_wait(int epfd, struct epoll_event *events, int max events, int timeout);'
    ]}
],
'结果':[
    '只一个阶段【复制数据】阻塞',
    '一个线程处理多个客户端连接（文件描述符），减少了系统调用开销（多个文件描述符只有一次select系统调用+n次就绪状态的文件描述符的read系统调用）',
    {'对比非阻塞IO':[
        '原来的while循环里多次系统调用，变成了一次系统调用+内核层遍历这些文件描述符',
        '类似代码里，while循环里调http接口进行批量查询，改成让对方提供一个批量查询的http接口，然后我们一次请求就完成了批量查询'
    ]}   
],
'特点':[
    {'涉及两种系统调用':[
        'select/epoll(就绪查询)',
        'read(IO操作)'
    ]},
    '通过select/epoll系统调用，一个进程可监视多个文件描述符，一旦某个描述符就绪（内核缓冲区可读/可写）,内核将就绪的状态返回给应用程序',
    {'系统开销小':[
        '系统不必为每一个网络连接（文件描述符）创建进程/线程，大大减小了系统开销'
    ]},
    'Java语言的NIO（New IO）技术，使用的就是IO多路复用模型',
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 