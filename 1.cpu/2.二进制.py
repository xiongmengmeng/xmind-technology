import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二进制")
r2=s2.getRootTopic()
r2.setTitle("二进制")


content={
'基础定义':[
    '二进制数表示计算机信息',
    {'为什么':[
        '计算机内部是由IC这种电子部件构成的',
        'IC的一个引脚，只能表示两个状态'
    ]},
    {'字节':[
        '信息的基本单位，8位二进制数被称为一个字节'
    ]},
    {'位权':[
        '数字的位数不同，位权也不同'
    ]}
],
'运算':[
    {'移位运算':[
        {'定义':[
            '将二进制数值的各数位进行左右移位的运算',
            '左侧是被移位的值，右侧表示要移位的位数',
            '可以代替乘法运算和除法运算',
            '溢出的位,计算机会直接忽略掉'
        ]},
        {'<<':[
            '左移',
            '在空出来的低位补0'
        ]},
        {'>><':[
            '右移',
            {'右移区分逻辑位移和算术位移':[
                '逻辑位移:在最高位补0',
                '算术位移:用移位前符号位的值补足'
            ]},
        ]},
        {'补数':[
            '用正数来表示负数',
            {'补数求解':[
                '取反+ 1'
            ]}
        ]},
        {'符号扩充':[
            '用符号位的值（0或者1）填充高位'
        ]}
    ]},
    {'逻辑运算':[
        '逻辑非（NOT运算）',
        '逻辑与（AND运算）',
        '逻辑或（OR运算）',
        '逻辑异或（XOR运算）'
    ]}

],
'缺点':[
    {'小数运算时出错':[
        '一些十进制数的小数无法转换成二进制数'
    ]},
    {'浮点数':[
        '定义：用符号、尾数、基数和指数这四部分来表示的小数',
        '双精度浮点数--64位',
        '单精度浮点数--32位来表示全体小数'
    ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 