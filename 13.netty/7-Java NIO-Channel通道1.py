import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("FileChannel文件通道")
r2=s2.getRootTopic()
r2.setTitle("FileChannel文件通道")


content={
'定义':[
    '表示一个网络连接,类似OIO中的两个流的结合体，既可以从通道读取，也可以向通道写入',
    '表示一个底层的文件描述符，例如硬件设备、文件、网络连接',
    '不同的网络传输协议类型，在Java中都有不同的NIO Channel（通道）实现,涵盖文件IO、TCP网络IO、UDP网络IO'
],
'分类':[
    'FileChannel文件通道',
    'SocketChannel套接字通道',
    'ServerSocketChannel服务器监听通道',
    'DatagramChannel数据报通道'
],
'FileChannel文件通道':[
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
            'int read（ByteBuffer buf）',
            '从通道读取到数据，写入到ByteBuffer缓冲区,返回读取到的字节数',
            {'例':[
                'ByteBuffer buf=ByteBuffer.allocate(20)',
                'inChannel.read(buf)',
                'System.out.print(new String(buf.array()))',
            ]}
        ]},
        {'写入FileChannel通道':[
            'int write（ByteBuffer buf）',
            '从ByteBuffer缓冲区中读取数据，然后写入到通道,返回写入成功的字节数',
            {'例':[
                'buf.flip()',
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
        {'强制刷新到磁盘(保证写入通道的缓冲数据，都真写入磁盘)':[
            'force()',
            {'例':[
                'inChannel.force()'
            ]}
        ]},
        {'更高效的文件复制':[
            'transferFrom(ReadableByteChannel target,long position,long count)',
            '数据从目标通道复制给当前通道',
            'transferTo(long position,long count,WritableByteChannel target)',
            '数据从当前通道复制给目标通道'
        ]}

    ]}
],



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 