import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("位运算")
r2=s2.getRootTopic()
r2.setTitle("位运算")


content={
'java运算符':[
    '与（&）',
    '非（~）',
    '或（|）',
    '异或（）'
],
'位与运算符（&）':[
    {'运算规则':[
        '两个数都转为二进制，然后从高位开始比较，如果两个数都为1则为1，否则为0。'
    ]},
    {'例':[
        '129&128',
        '129转换成二进制就是10000001',
        '128转换成二进制就是10000000',
        '从高位开始比较得到，得到10000000，即128'
    ]},
],
'位或运算符（|）':[
    {'运算规则':[
        '两个数都转为二进制，然后从高位开始比较，两个数只要有一个为1则为1，否则就为0',
    ]},
    {'例':[
        '129|128',
        '129转换成二进制就是10000001',
        '128转换成二进制就是10000000',
        '从高位开始比较得到，得到10000001，即129'
    ]}
],
'位异或运算（^）':[
    {'运算规则':[
        '两个数转为二进制，然后从高位开始比较，如果相同则为0，不相同则为1'
    ]},
    {'例':[
        '8^11',
        '8转为二进制是1000，11转为二进制是1011',
        '从高位开始比较得到的是：0011',
        '然后二进制转为十进制，Integer.parseInt("0011",2)=3',
        '6^3=110&11=101=5',
    ]}

],
'位非运算符（~）':[
    {'运算规则':[
        '如果位为0，结果是1，如果位为1，结果是0.'
    ]}
],
'向右移动(>>)':[
    {'运算规则':[
        '运算符前为要做操作的数字，运算符后为要移动的位数，数字向右移动'
    ]},
    {'例':[
        '6>>2',
        '6转为二进制是110',
        '向右移动两位得到的是：1'
        '然后二进制转为十进制，也是1',
    ]}

],
'向左移动(<<)':[
    {'运算规则':[
        '运算符前为要做操作的数字，运算符后为要移动的位数，数字向左移动'
    ]},
    {'例':[
        '6<<3',
        '6转为二进制是110',
        '向右移动两位得到的是：110000'
        '然后二进制转为十进制，也是48',
    ]}
],
'右移位运算符(>>>)':[
    '6>>>2=1',
    '无论正负，都在高位插入0'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 