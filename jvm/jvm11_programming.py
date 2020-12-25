import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_programming")
r2=s2.getRootTopic()
r2.setTitle("Javac编译器")


content={
'分类':[
    {'前端编译器':[
        '编译期的优化过程',
        '很多Java语法新特性，是靠编译器的“语法糖”来实现',
        '不依赖字节码或者Java虚拟机的底层改进'
    ]},
    {'后端编译器':[
        '即时编译器在运行期的优化过程'
    ]}
],
'由Java语言编写的程序':[],
'编译入口':[
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
'注解处理器':[
    '类似插件，可CRUD抽象语法树中的任意元素',
    '解析与填充符号表->注解处理器,是一个循环过程，直到注解处理器不再对语法树进行修改',
    {'应用':[
        'Lombok:通过注解来实现自动产生getter/setter/equals()/hashCode()方法等'
    ]},
    'com.sun.tools.javac.processing.JavacProcessingEnvironment类的doProcessing()方法',
    '生成一个新的JavaCompiler对象，对编译的后续步骤进行处理'
],
'语义分析与字节码生成':[
    {'作用':[
        '对结构上正确的源程序进行上下文相关检查'
    ]},
    {'标注检查':[
        '变量使用前是否已被声明',
        '变量与赋值之间的数据类型是否能够匹配',
        '实现类com.sun.tools.javac.comp.Attr',
        '实现类com.sun.tools.javac.comp.Check'
    ]},
    {'数据及控制流分析':[
        '程序局部变量在使用前是否有赋值',
        '方法的每条路径是否都有返回值',
        '是否所有的受查异常都被正确处理',
        '实现类com.sun.tools.javac.comp.Flow'
    ]},
    {'解语法糖':[
        {'语法糖定义':[
            '某种语法，对语言的编译结果和功能并没有实际影响，但可以方便程序员使用'
        ]},
        {'应用':[
            {'泛型':[
                '本质：参数化类型（Parameterized Type）',
                '能够用在类、接口和方法的创建中，分别构成泛型类、泛型接口和泛型方法',
                {'擦除法实现':[
                    '对方法的Code属性中的字节码进行擦除',
                    '元数据中会保留泛型信息，反射手段可以取得参数化类型',
                    '缺点是比较慢，会频繁构造包装类和装箱、拆箱'
                ]}
            ]},
            {'自动装箱、拆箱与遍历循环':[
                '包装类的“==”运算遇到算术运算自动拆箱',
                '包装类的equals()方法不处理数据转型'
            ]},
            '条件编译'
        ]},
        {'解语法糖定义':[
            '编译阶段被还原回原始的基础语法结构'
        ]},
        '实现类com.sun.tools.javac.comp.TransTypes',
        '实现类com.sun.tools.javac.comp.Lower'
    ]},
    {'字节码生成':[
        'com.sun.tools.javac.jvm.Gen类完成',
        '把前面各步骤所生成的信息（语法树、符号表）转化成字节码指令写到磁盘',
        {'进行了少量代码添加和转换':[
            '将实例构造器<init>()和类构造器<clinit>()方法添加到语法树中',
            '如把字符串的加操作替换为StringBuffer或StringBuilder'
        ]}
    ]} 
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 