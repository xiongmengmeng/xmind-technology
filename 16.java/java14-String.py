import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("String")
r2=s2.getRootTopic()
r2.setTitle("String")


content={
'简介':[
    '一个被 final修饰的类',
    {'本质':[
        '使用字符数组来存储的数据'
    ]},
    {'基本数据类型传递与引用传递区别':[
        '当传递方法参数类型为基本数据类型时，方法不会修改基本数据类型的参数------值拷贝',
        '当传递方法参数类型为引用数据类型时，方法会修改引用数据类型的参数所指向对象的值------堆的值'
    ]},
    {'不可变性优点':[
        {'安全':[
            'String对于方法中形参值更多的是像基本数据类型属于【值拷贝】'
        ]},
        {'效率/性能':[
            '在编译阶段就把所有的字符串文字放到一个常量池中,避免频繁的创建和销毁对象,提高了性能'
        ]}
    ]}
],
'使用方式':[
    {'String s1 = “first”':[
        '编译期就被确定,s1直接指向字符串常量池的”first”对象'
    ]},
    {'String s2=”se”+”cond”':[
        '当一个字符串由多个字符串常量连接而成时，它自己肯定也是字符串常量',
        's2也同样在编译期就被解析为一个字符串常量，并且s2是常量池中”second”的一个引用'
    ]},
    {'String s12=”first”+s2':[
        'JVM对于字符串引用,引用的值在程序编译期是无法确定的',
        '只有在程序运行期动态分配使用StringBuilder连接后的新String对象赋给s12'
    ]},
    {'String s3 = new String(“three”)':[
        '用new String() 创建的字符串不是常量，不能在编译期就确定'
    ]},
    {'String s4 = new String(“fo”)+”ur”':[
        '不能在编译期确定，但是”fo”和”ur”这两个字符串常量也会添加到字符串常量池中',
        '并且在堆中创建String对象。（字符串常量池并不会存放”four”这个字符串'
    ]},
    {'String s5 = new String(“fo”)+new String(“ur”)':[
        '同上'
    ]}
],
'String 的拼接':[
    'Java中，唯一被重载的运算符就是字符串的拼接相关的:+,+=',
    '创建一个StringBuilder对象，并调用append()方法，最后调用toString()创建新String对象'
],
'intern()方法':[
    '字符串常量池已经包含一个等于此String对象的字符串，则返回代表字符串常量池中这个字符串的String对象',
    '否则将此String对象的引用地址（堆中）添加到字符串常量池中'
],
'String的String Pool':[
    '一个固定大小的Hashtable，默认值大小长度是1009',
    '如放进String Pool的String非常多，就会造成Hash冲突严重，从而导致链表会很长，而链表长了后直接会造成的影响就是当调用String.intern时性能会大幅下降',
    '在jdk 1.7中，StringTable的长度可以通过一个参数指定：-XX:StringTableSize=99991'
],
'学习':[
    'https://blog.csdn.net/qian520ao/article/details/78966179'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 