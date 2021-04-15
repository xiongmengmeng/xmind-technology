import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Java NIO-通道Channel")
r2=s2.getRootTopic()
r2.setTitle("Java NIO-通道Channel")


content={
'定义':[
    '一个网络连接使用一个通道表示,类似OIO中的两个流的结合体，既可以从通道读取，也可以向通道写入',
    '一个通道可以表示一个底层的文件描述符，例如硬件设备、文件、网络连接',
    '不同的网络传输协议类型，在Java中都有不同的NIO Channel（通道）实现,涵盖文件IO、TCP网络IO、UDP网络IO'
],
'分类':[
    {'FileChannel文件通道':[
        '阻塞模式,用于文件的数据读写',
        {'4个核心操作':[
            {'获取FileChannel通道':[
                'getChannel()',
                {'例':[
                    'FileInputStream fis=new FileInputStream("xxx")',
                    'FileChannel inChannel=fis.getChannel()',
                    'FileOutStream fos=new FileOutStream("xxx")',
                    'FileChannel outChannel=fos.getChannel()'
                ]}
            ]},
            {'读取FileChannel通道':[
                'int read（ByteBufferbuf）',
                '从通道读取到数据，写入到ByteBuffer缓冲区,并且返回读取到的数据量',
                {'例':[
                    'ByteBuffer buf=ByteBuffer.allocate(20)'
                    'int length=-1',
                    'while((length=inChannel.read(buf)!=-1){',
                    '   //处理读取到的数据',
                    '}'
                ]}
            ]},
            {'写入FileChannel通道':[
                'int write（ByteBufferbuf）',
                '从ByteBuffer缓冲区中读取数据，然后写入到通道自身,最后返回写入成功的字节数',
                {'例':[
                    'buf.flip()'
                    'int outlength=0',
                    'while((length=outChannel.write(buf)!=0){',
                    '   //写入字节数据',
                    '}'
                ]}
            ]},
            {'关闭通道':[
                'close()',
                {'例':[
                    'inChannel.close()'
                ]}
            ]},
            {'强制刷新到磁盘(保证写入通道的缓冲数据，都真正地写入磁盘)':[
                'force()',
                {'例':[
                    'inChannel.force()'
                ]}
            ]},
            '更高效的文件复制，可以调用文件通道的transferFrom方法'
        ]}
    ]},
    {'SocketChannel套接字通道':[
       
    ]},
    {'ServerSocketChannel服务器监听通道':[
        
    ]},
    {'DatagramChannel数据报通道':[
        '用于UDP协议的数据读写',
        {'4个核心操作':[
            {'获取DatagramChannel数据报通道':[
                '调用DatagramChannel类的open静态方法',
                '调用configureBlocking（false）方法，设置成非阻塞模式',
                '需要接收数据，还需调用bind方法绑定一个数据报的监听端口'
            ]},
            {'读取DatagramChannel数据报通道数据':[
                {'receive(ByteBufferbuf)':[
                    '将数据从DatagramChannel读入，再写入到ByteBuffer缓冲区中',
                    '返回值，是SocketAddress类型，表示返回发送端的连接地址（包括IP和端口）'
                ]}
            ]},
            {'写入DatagramChannel数据报通道':[
                {'send()':[
                    '需指定接收方的地址（IP和端口）'
                ]}
            ]},
            {'关闭DatagramChannel数据报通道':[
                'close()'
            ]}
        ]}
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 