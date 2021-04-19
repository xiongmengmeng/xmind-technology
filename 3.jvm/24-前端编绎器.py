import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("前端编译器")
r2=s2.getRootTopic()
r2.setTitle("前端编译器")


content={
'编译器分类':[
    {'前端编译器':[
        '将源代码编译成字节码',
        {'编译期的优化过程':[
            '很多Java语法新特性，是靠编译器的“语法糖”来实现',
            '不依赖字节码或者Java虚拟机的底层改进'
        ]},
    ]},
    {'后端编译器---及时编译器':[
        '执行引擎的编译',
        '即时编译器在运行期的优化过程'
    ]}
],
'编译入口(由Java语言编写的程序)':[
    'Java源码编译器',
    'com.sun.tools.javac.main.JavaCompiler类的compile()方法'
],
'编译过程':[
    {'准备过程':[
        '初始化插入式注解处理器'
    ]},
    {'解析与填充符号表':[
        '词法、语法分析',
        '将源代码的字符流转变为标记集合，构造出抽象语法树',
        '填充符号表，产生符号地址和符号信息'
    ]},
    '注解处理',
    {'分析与字节码生成':[
        '标注检查:对语法的静态信息进行检查',
        '数据流及控制流分析:对程序动态运行过程进行检查',
        '解语法糖:将简化代码编写的语法糖还原为原有的形式',
        '字节码生成:将前面各个步骤所生成的信息转化成字节码'
    ]}
],
'解析与填充符号表':[
    {'词法分析':[
        '字符流->标记集合',
        '单个字符:程序编写时的最小元素',
        '标记:编译时的最小元素',
        'com.sun.tools.javac.parser.Scanner类实现'
    ]},
    {'语法分析':[
        '标记序列->抽象语法树',
        'com.sun.tools.javac.parser.Parser类实现',
        {'抽象语法树':[
            '用来描述程序代码语法结构',
            '每一个节点都代表着程序代码中的一个语法结构',
            '如包、类型、修饰符、运算符、接口、返回值、代码注释等'
        ]},
        '抽象语法树以com.sun.tools.javac.tree.JCTree类表示'
    ]},
    {'填充符号表':[
        {'符号表':[
            '符号地址+符号信息'
        ]},
        {'作用':[
            '语义分析阶段: 语义检查和产生中间代码',
            '目标代码生成阶段: 根据符号表进行地址分配'
        ]},
        '   com.sun.tools.javac.comp.Enter类实现'
    ]}
],

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 