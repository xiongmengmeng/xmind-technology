import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ADSL接入网")
r2=s2.getRootTopic()
r2.setTitle("ADSL接入网")


content={


'互联网与家庭、公司网络不同点':[
    '距离的不同',
    '路由的维护方式'
],
'过程':[
    {'客户端生成的网络包':[
        '添加IP头部',
        '添加MAC头部并发送'
    ]},
    {'互联网接入路由器':[
        '接收包，取出IP包',
        '添加PPP,PPPoE,MAC头部',
        '头部：MAC-PPPoE-PPP-IP'
    ]},
    {'ADSL Modem':[
        '接收包',
        '拆分成ATM信元',
        '转换成电信号并发送'
    ]},
    '分离器',
    {'DSLAM':[
        '接收电信号',
        '还原为ATM信元并发送',
        '具有ATM接口，和后方路由器收发数据用的是ATM信元',
    ]},
    {'BAS(宽带接入服务器)':[
        '接收ATM信元',
        '还原网络包',
        '取出PPP包',
        '添加隧道头部并发送',
        '总结：负责将ATM信元还原成网络包并转发到互联网内部'
    ]},
    {'路由器（隧道专用）':[
        '接入隧道包',
        '取出IP包',
        '发送到互联网内部'
    ]}
],
'信元':[
    '一个非常小的数据块',
    '开头是有5个字节的头部，后面是48个字节的数据',
    '用于一种叫作ATM的通信技术'
    
],
'正交振幅调制（QAM）':[
    '=振幅调制（ASK）+相位调制（PSK）',
    '振幅调制（ASK）:振幅大小对应0和1,振幅小的信号为0，振幅大的信号为1',
    '相位调制（PSK）:信号相位对应0和1,0度开始的波为0，180度开始的波为1',
    'ADSL Modem:采用这种用圆滑波形（正弦波）对信号表示的方式',
    '以太网:采用方波信号表示0和1'
],
'ADSL Modem':[
    '将包拆分成信元，并转换成电信号发送给分离器',
    '会持续检查线路质量，动态判断使用的频段数量，以及每个频段分配到的比特数',
    '训练（握手）：Modem通电后，发送测试信号，根据信号接收情况判断使用的频段数量和每个频段的比特数(几秒到几十秒)'
],
'分离器':[
    '防止ADSL对电话干扰：信号从电话线传入,分离器需要将电话和ADSL的信号进行分离',
    '防止电话对ADSL干扰:防止拿起放下话筒导致的线路状态改变'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 