import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("栈帧")
r2=s2.getRootTopic()
r2.setTitle("栈帧")


content={
'背景':[
    'Java虚拟机以【方法】作为最基本的执行单元',
],
'目的':[
    '支持虚拟机进行【方法调用】和【方法执行】'
],
'栈帧':[
    '每一个方法从调用开始至执行完成的过程，对应着一个栈帧在虚拟机里面从入栈到出栈的过程',
    '在活动线程中，只有位于栈顶的栈帧才是有效的，称为【当前栈帧】，与这个栈帧相关联的方法称为【当前方法】',
],
'内容':[
    {'局部变量表':[
        '一组变量值的存储空间(单位：变量槽),存放【方法参数】和【方法内部定义的局部变量】',
        '在Java编译为Class文件时，就已经确定了该方法所需要分配的局部变量表的最大容量',
        {'方法被调用时':[
            '虚拟机会使用局部变量表来完成【实参】到【形参】的传递,即【参数值】到【参数变量列表】的传递过程'
        ]},
        {'实例方法被调用':[
            {'第0位变量槽':[
                '默认传递方法所属对象实例的引用',
                '方法中可通过this来访问这个隐含的参数'
            ]},
            '其余参数按照参数表顺序排列，占用从1开始的变量槽',
            '参数分配完，据方法体内部定义变量顺序和作用域分配其余变量槽'
        ]},
        {'注意':[
            '局部变量要赋初始值',
            '类变量不需要，它在<准备阶段>会赋默认值'
        ]} 
    ]},
    {'操作数栈':[
        '最大深度编译时确认(类局部变量表)，存在Code属性的max_stacks数据项',
        {'入栈/出栈操作':[
            '当一个方法刚刚开始执行的时候，方法的操作数栈是空的',
            '方法执行过程中，会有各种字节码指令往操作数栈中写入和提取内容'
        ]},
        {'栈帧间的数据共享':[
            '下面栈帧的部分操作数栈与上面栈帧的部分局部变量表重叠',
            '节约空间，方法调用时直接共用部分数据，无须进行额外的参数复制',
        ]},
    ]},
    {'动态连接':[
        '每个栈帧都包含一个指向运行时常量池中该栈帧所属方法的引用,这个引用是为->'
        '运行期间将符号引用->直接引用'
    ]},
    {'方法返回地址(2种方式)':[
        {'方法返回指令':[
            '调用完成,执行引擎遇到一个方法返回的字节码指令',
            '调用者的PC计数器的值可以作为返回地址，栈帧中会保存这个计数器值'
        ]},
        {'异常退出':[
            '方法执行过程遇异常，且异常没有在方法体内处理',
            '返回地址是要通过异常处理器表来确定的，栈帧中一般不会保存这部分信息'
        ]}
    ]}
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 