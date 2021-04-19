import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("动态分派")
r2=s2.getRootTopic()
r2.setTitle("动态分派")


content={
'动态分派':[
    {'定义':[
        '运行期根据【实际类型】确定【方法执行版】本的分派动作',
        {'典型表现':[
            '方法重写（Override）'
        ]}
    ]},
    {'invokevirtual指令运行时解析过程':[
        '1.找到操作数栈顶的第一个元素所指向的对象实际类型，记作C',
        {'2.在类型C中找到与常量中的描述符和简单名称都相符的方法':[
            {'2.1找得到，进行访问权限校验':[
                '通过:返回方法的直接引用，查找过程结束',
                '不通过:返回java.lang.IllegalAccessError异常'
            ]},
            {'2.2找不到，按照继承关系从下往上对C的各个父类进行搜索和验证':[

            ]}
        ]},
        '3.如始终没有找到合适的方法，抛出java.lang.AbstractMethodError'
    ]},
    {'方法重写本质':[
        'invokevirtual指令执行的第一步：在运行期确定接收者的实际类型',
        '根据【方法接收者】的【实际类型】来选择【方法版本】',
        '把常量池中方法的符号引用解析到直接引用上'
    ]},
    {'动态分派实现':[
        '方法版本选择过程需在【接收者类型的方法元数据】中搜索目标方法',
        {'优化手段':[
            '为类型在方法区中建【虚方法表】,使用虚方法表索引来代替元数据查找'
        ]},
        '虚方法表在【类加载】【连接阶段】进行初始化，类的变量初始值后，把类的虚方法表一同初始化'
    ]}
],
'单分派与多分派':[
    {'方法的宗量':[
        '方法的接收者与参数'
    ]},
    {'单分派':[
        '根据一个宗量对目标方法进行选择'
    ]},
    {'多分派':[
        '根据多个宗量对目标方法进行选择'
    ]},
    {'静态分派,选择目标方法的依据':[
        '静态类型',
        '方法参数',
        '属于多分派类型,根据两个宗量进行选择'
    ]},
    {'动态分派,选择目标方法的依据':[
        '方法接受者的实际类型'
    ]}
],
'总结':[
    {'静态分派':[
        '方法（括号内）参数的类型有关（只关注有几个参数类型）'
    ]},
    {'动态分派':[
        '和方法的调用者有关'
    ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 