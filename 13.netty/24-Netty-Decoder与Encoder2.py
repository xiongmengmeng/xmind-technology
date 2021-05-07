import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("netty:Decoder与Encoder")
r2=s2.getRootTopic()
r2.setTitle("netty:Decoder与Encoder")


content={
'粘包和拆包':[
    {'原因':[
        '发送端Netty的【应用层进程缓冲区】，程序以【ByteBuf】为单位来发送数据',
        '到了底层【操作系统内核缓冲区】，按照协议的规范对数据包进行二次拼装，拼装成【传输层TCP层的协议报文】，再进行发送',
        '接收端收到传输层的二进制包后，首先保存在内核缓冲区，Netty读取ByteBuf时才复制到进程缓冲区'
    ]},
    {'解决方案--分包':[
        '自定义协议+编解码器',
        '关键解决：服务器每次读出数据长度问题',
    ]},
    {'分包':[
        {'定义':[
            '在接收端，Netty程序根据自定义协议',
            '将读取到的进程缓冲区ByteBuf，在应用层进行二次拼装，重新组装我们应用层的数据包',
        ]},
        {'方法':[
            {'自定义解码器分包器':[
                '基于ByteToMessageDecoder或者ReplayingDecoder，定义自己的进程缓冲区分包器'
            ]},
            {'Netty内置的解码器':[
                '使用Netty内置自定义分隔符数据包解码器LengthFieldBasedFrameDecoder，对进程缓冲区ByteBuf进行正确分包'
            ]}
        ]}
    ]}
],
'http+json':[
    'Java处理JSON数据使用类库：阿里的FastJson、谷歌的Gson和开源社区的Jackson',
    {'处理JSON数据的编解码器':[
        '1.用LengthFieldBasedFrameDecoder（Netty的自定义长度数据包解码器）解码Head-Content二进制数据包，解码出Content字段的二进制内容',
        '2.用StringDecoder字符串解码器（Netty内置的解码器）将二进制内容解码成JSON字符串',
        '3.用JsonMsgDecoder解码器（自定义解码器）将JSON字符串解码成POJO对象'
    ]}
],
'tcp+Protobuf':[
    {'Protobuf编码过程':[
        '使用预先定义的Message数据结构将实际的传输数据进行打包',
        '编码成二进制的码流进行传输或者存储'
    ]},
    {'优点':[
        {'速度快':[
            'Protobuf数据包是【二进制】格式，JSON、XML数据包是【文本】格式'
        ]},
        {'跨语言':[
            '更加适用于分布式应用场景下的数据通信或者异构环境下的数据交换'
        ]}
    ]},
    {'proto文件':[
        '一个消息的协议文件，文件名后缀为“.proto”',
        'Protobuf使用proto文件来预先定义的消息格式',
        '数据包是按照proto文件所定义的消息格式完成二进制码流的编码和解码',
        {'内容':[
            '头部声明',
            '消息结构体的定义'
        ]},
        {'序列化&反序列化':[
            '通过字节数组',
            '通过流',
            '通过【流+序列化的字节码】前加字节数组的长度，类似于前面介绍的Head-Content协议'
        ]}
    ]},
    {'Netty自带的ProtoBuf编/解码器':[
        'ProtobufDecoder解码器',
        'ProtobufEncoder编码器',
        'ProtobufVarint32FrameDecoder解码器',
        'ProtobufVarint32LengthFieldPrepender编码器'
    ]},
    {'自定义Protobuf编/解码器':[
        '解析复杂的Head-Content协议,需开发者自己解决半包问题',
        {'继承netty提供的MessageToByteEncoder编码器':[
            '完成Head-Content协议的复杂数据包的编码',
            '将Protobuf POJO编码成Head-Content协议的二进制ByteBuf数据包'
        ]},
        {'继承netty提供的ByteToMessageDecoder解码器':[
            '完成Head-Content协议的复杂数据包的解码',
            '将二进制ByteBuf数据包最终解码出Protobuf POJO实例'
        ]}
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 