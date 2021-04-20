import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm总结2-虚拟机执行子系统")
r2=s2.getRootTopic()
r2.setTitle("jvm总结2-虚拟机执行子系统")


content={

'类文件结构':[
    '一组以8个字节为基础单位的二进制流',
    {'两种数据类型':[
        '无符号数',
        '表'
    ]},
    {'组成':[
        '魔数与Class文件版本',
        '常量池cp_info',
        '访问标志',
        '类索引、父类索引与接口索引集合',
        '字段表集合',
        '方法表集合',
        '属性表集合'
    ]},
    {'字节码指令':[
        '操作码+参数'
    ]}
],
'类文件加载':[
    {'类加载过程':[
        '加载（Loading）',
        {'连接':[
            '验证（Verification）',
            '准备（Preparation）',
            '解析（Resolution）'
        ]},
        '初始化（Initialization）',
    ]},
    {'类加载器':[
        {'三种':[
            'BootstrapClassLoader---启动类类加载器',
            'ExtClassLoader---拓展类类加载器',
            'AppClassLoader---应用程序类类加载器'
        ]},
        '双亲委派模型',
        {'破坏模型':[
            '1.SPI方式加载类/接囗的实现，如JNDI,JDBC',
            '2.热部署',
            '3.自定义类加载器'
        ]}
    ]},
],
'字节码执行引擎':[
    {'栈帧':[
        '局部变量表',
        '操作数栈',
        '动态连接',
        '方法返回地址'
    ]},
    {'方法调用':[
        {'静态分派':[
            '依赖【静态类型】决定【方法执行版本】',
            '重载'
        ]},
        {'动态分派':[
            '运行期根据【实际类型】确定【方法执行版】本的分派动作',
            '重写'
        ]}
    ]},
    {'字节码执行引擎':[
        '解释执行',
        {'编译执行':[
            {'编译器优化':[
                '方法内联',
                '逃逸分析',
                '公共子表达式消除'
            ]}
        ]}
    ]},
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 