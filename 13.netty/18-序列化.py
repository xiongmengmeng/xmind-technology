import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("序列化")
r2=s2.getRootTopic()
r2.setTitle("序列化")


content={

'粘包和拆包':[
    {'原因':[
        '发送端Netty的应用层进程缓冲区，程序以ByteBuf为单位来发送数据，',
        '到了底层操作系统内核缓冲区，底层会按照协议的规范对数据包进行二次拼装，拼装成传输层TCP层的协议报文，再进行发送',
        '接收端收到传输层的二进制包后，首先保存在内核缓冲区，Netty读取ByteBuf时才复制到进程缓冲区'
    ]}
],
'分包':[
    {'定义':[
        '在接收端，Netty程序需要根据自定义协议',
        '将读取到的进程缓冲区ByteBuf，在应用层进行二次拼装，重新组装我们应用层的数据包',
    ]},
    {'方法':[
        '可以自定义解码器分包器：基于ByteToMessageDecoder或者ReplayingDecoder，定义自己的进程缓冲区分包器',
        '使用Netty内置的解码器。如使用Netty内置的LengthFieldBasedFrameDecoder自定义分隔符数据包解码器，对进程缓冲区ByteBuf进行正确的分包'
    ]}
],
'JSON':[
    'Java处理JSON数据有三个比较流行的开源类库有：阿里的FastJson、谷歌的Gson和开源社区的Jackson',
    {'JSON传输的编码器和解码器之原理':[
        '入站',
        '先使用LengthFieldBasedFrameDecoder（Netty内置的自定义长度数据包解码器）解码Head-Content二进制数据包，解码出Content字段的二进制内容',
        '然后，使用StringDecoder字符串解码器（Netty内置的解码器）将二进制内容解码成JSON字符串',
        '最后，使用JsonMsgDecoder解码器（一个自定义解码器）将JSON字符串解码成POJO对象'
    ]}
],
'Protobuf协议通信':[
    {'Protobuf的编码过程':[
        '使用预先定义的Message数据结构将实际的传输数据进行打包',
        '然后编码成二进制的码流进行传输或者存储'
    ]},
    {'优点':[
        'Protobuf数据包是一种二进制的格式，相对于文本格式的数据交换（JSON、XML）来说，速度要快很多',
        '优异的性能，使得它更加适用于分布式应用场景下的数据通信或者异构环境下的数据交换'
    ]},
    {'proto文件':[
        '一个消息的协议文件，这个协议文件的后缀文件名为“.proto”',
        'Protobuf使用proto文件来预先定义的消息格式。数据包是按照proto文件所定义的消息格式完成二进制码流的编码和解码',
        {'内容':[
            '头部声明',
            '消息结构体的定义'
        ]},
        'Maven插件生成POJO和Builder',
        {'序列化serialization & 反序列化Deserialization':[
            '通过字节数组',
            '通过流',
            '通过流+序列化的字节码之前添加了字节数组的长度，类似于前面介绍的Head-Content协议'
        ]}
    ]}
],
'Netty自带的ProtoBuf编/解码器':[
    'ProtobufDecoder解码器',
    'ProtobufEncoder编码器',
    'ProtobufVarint32FrameDecoder解码器',
    'ProtobufVarint32LengthFieldPrepender编码器'
],
'自定义Protobuf编/解码器':[
    '解析复杂的Head-Content协议,需要开发者自己去解决半包问题',
    {'继承netty提供的MessageToByteEncoder编码器':[
        '完成Head-Content协议的复杂数据包的编码',
        '将Protobuf POJO编码成Head-Content协议的二进制ByteBuf数据包'
    ]},
    {'继承netty提供的ByteToMessageDecoder解码器':[
        '完成Head-Content协议的复杂数据包的解码',
        '将二进制ByteBuf数据包最终解码出Protobuf POJO实例'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 