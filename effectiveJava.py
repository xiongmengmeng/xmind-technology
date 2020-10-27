import xmind
from xmind.core.markerref import MarkerId

w = xmind.load("c:\\Users\\btr\\Desktop\\tcp.xmind") 
s2=w.createSheet()
s2.setTitle("tcp")
r2=s2.getRootTopic()
r2.setTitle("tcp")


# content={

# '前言':[
#     {'网卡':[
#         '网络适配器（Network Adapter），是连接计算机和传输介质的接口',
#         '主要用来将计算机数据转换为能够通过传输介质传输的信号'
#     ]},
#     {'网络电缆':[
#         '用来连接网络中的各个设备，供设备之间进行数据通信,常见的网络电缆有双绞线、光纤、电话线'
#     ]},
#     {'网络协议':[
#         '为计算机网络中进行数据交换而建立的规则、标准或约定的集合'
#     ]},
#     {'网络互联的7层框架':[
#         '应用层：为应用程序提供服务并规定应用程序中相关的通信细节',
#         '表示层：主要负责数据格式的转换,确保一个系统的应用层信息可被另一个系统应用层读取' ,
#         '会话层：负责建立和断开通信连接（数据流动的逻辑通路），以及记忆数据的分隔等数据传输相关的管理',
#         '传输层：只在通信双方的节点上（比如计算机终端）进行处理，无须在路由器上处理',
#         '网络层：将数据传输到目标地址，主要负责寻找地址和路由选择，网络层还可以实现拥塞控制、网际互联等功能',
#         '数据链路层：负责物理层面上互连的节点间的通信传输',
#         '物理层：利用传输介质为数据链路层提供物理连接，实现比特流的透明传输'
#     ]},
#     {'':[
#         '应用层：为应用程序提供服务并规定应用程序中相关的通信细节',
#         '传输层：为两台主机上的应用程序提供端到端的通信，提供流量控制、错误控制和确认服务',
#         '网际层：提供独立于硬件的逻辑寻址，从而让数据能够在具有不同的物理结构的子网之间传递,负责寻找地址和路由选择的同时，网络层还可以实现拥塞控制、网际互联等功能',
#         '网络访问层：提供了与物理网络连接的接口。针对传输介质设置数据格式，根据硬件的物理地址实现数据的寻址，对数据在物理网络中的传递提供错误控制。'
#     ]},
#     '网络工具集工具netwox:可以创造任意的TCP、UDP和IP数据报文，以实现网络欺骗',
#     '网络分析工具Wireshark:一个网络包分析工具。该工具主要是用来捕获网络数据包，并自动解析数据包，为用户显示数据包的详细信息，供用户对数据包进行分析'
# ],
# '网络访问层':[
#     '对应OSI七层网络模型的物理层和数据链路层',

#     {'物理层':[
#         '提供传送数据的通路和可靠的环境。对于计算机来说，物理层对应的就是网络适配器'
#     ]},
#     {'数据链路层':[
#         '为网络层提供数据传送服务',
#         '定义了数据传输的起始位置，并且通过一些规则来控制这些数据的传输，以保证数据传输的正确性',
#         {'介质访问控制（Media Access Control, MAC）':[
#             '：提供与网络适配器连接的接口。实际上，网络适配器驱动程序通常被称为MAC驱动，而网卡在工厂固化的硬件地址通常被称为MAC地址'
#         ]},
#         {'逻辑链路控制（Logical Link Control, LLC）':[
#             '这个子层对经过子网传递的帧进行错误检查，并且管理子网上通信设备之间的链路'
#         ]}
#     ]},
#     {'网络体系':[
#         {'构成':[
#             '访问方法：定义了计算机使用传输介质的规则',
#             '数据帧格式：定义了数据传输的格式',
#             '布线类型：定义了网络适配器和其他网络设备的连接方式',
#             '布线规则：定义网络适配器和网络设备连接规范'

#         ]}
#     ]}
# ]

# }

content={
'创建和销毁对象':[
    {'用静态工厂方法代替构造器':[
        '有名称',
        '不用每次调用都创建一个新的对象',
        '可以返回原返回类型的子类型对象',
        '通过静态方法的参数值，返回不同类的对象'
    ]},
    {'多构造器参数考虑使用Builder模式':[
        '可读性好'
    ]},
    '用私有构造器或枚举类型强化singleton属性',

    {'通过私有构造器强化不可实例化的能力':[
        '私有构造器内部抛AssertionError,防止类内部或反射调用',
        '构造器加注释说明 '
    ]},
    {'优先考虑依赖注入来引用资源':[
        '常见依赖注入框架：spring,dagger',
        '变体：将工厂传递给构造器，java8中增加的接囗Supplier<T>,最适合用于表示工厂'
    ]},
    {'避免创建不必要的对象':[
        '对于提供了静态工厂方法和构造器的不可变类：优先使用静态工厂方法',
        'Boolean.valueOf(String)优于Boolean(String)',
        '构造器每次调用都创建新的实例，而静态方法可以重用不可变的对象，也可以重用已知不会被修改的可变对象',
        '对于常量可以设置成static final的类型，让它成为类初始化的一部分，避免重复创建',
        '大量计算时优先使用基本数据类型，当心无意识的自动装箱'
    ]},
    {'消除过期的对象引用':[
        '如果类自己管理内存，应警惕内存泄漏问题：一旦元素被释放掉，元素中的任何对象引用都该被清空',
        '缓存，对弱引用WeakHashMap来引用缓存，可以保证缓存过期后被自动删除',
        '监听器和其它回调，也可以用WeakHashMap来引用回调'
    ]},
    '避免使用终结方法和清除方法',
    {'try-with-resources优先于try-finally':[
        '条件：当一个外部资源的句柄对象实现了AutoCloseable接口',
        '实现：将外部资源的句柄对象的创建放在try关键字后面的括号中',
        '结果：如果对外部资源的处理和对外部资源的关闭均遭遇了异常，“关闭异常”将被抑制，“处理异常”将被抛出',
        '“关闭异常”并没有丢失，而是存放在“处理异常”的被抑制的异常列表中'
    ]}
],
'对于所有对象都通用的方法':[
    {'覆盖equals时请遵守通用约定':[
        {'实现高质量equals方法的诀窍':[
            '使用==操作符楂“参数是否为这个对象的引用”',
            '使用instanceof操作符检查“参数是否为正确的类型”',
            '把参数转换成正确的类型',
            '对于该类中的每个“关键”域，检查参数中的域是否与该对象中对应的域相匹配'
        ]},
        {'注意':[
            '覆盖equals时总要覆盖hashCode',
            '不要将equals声明中的Object对象替换为其他类型'
        ]},
        {'自动生成':[
            '使用google开源的AutoValue框架',
            'IDE生成equals和hashCode方法',
            'lombok包中@Data'
        ]}
    ]},
    {'覆盖equals时总要覆盖hashCode':[
        '计算对象所有关键域的散列码，然后相加'
    ]},
    {'始终要覆盖toString':[
        '可以使用lombok包中@Data，自动生成toString方法'
    ]},
    {'谨慎覆盖clone':[
        '实现Cloneable接囗的类都应该覆盖clone()方法，返回类型为类本身',
        '方法内部先调用super.clone()方法，然后修正任何需要修正的域',
        '复制功能最好由构造器或工厂提供，复制数组最好用clone方法'
    ]},
    {'考虑实现Comparable接囗':[
        '当实现一个对排序敏感的类，都应该让其实现Comparable接囗,以便其实例被轻松分类与搜索',
        'compareTo方法中避免使用<和>操作符',
        '尽量使用包装类的静态compare方法',
        '或是在Comparator接囗中使用比较器构造方法'
    ]}],
'类和接囗':[
    '使类和成员的可访问性最小化',
    {'要在公有类而非公有域中使用访问方法':[
        '公有类永远都不应该暴露可变的域'
    ]},
    {'使可变性最小化':[
        '不可变对象本质是线程安全的，它们不要求同步',
        '缺点，对于每个不同的值都需要一个单独的对象',
        '很多不可变类，会有一个可变配套类，如String和StringBuffer'
    ]},
    {'复合优先于继承':[
        '与方法调用不同的是，继承打破了封装性',
        '扩展一个类时，改变原方法，可能原方法A调用了原方法B,在同时覆盖两方法时不知道这层逻辑，出错',
        '扩展一个类时，新增加一个方法A，可能新版本新增方法B与A同签名'
    ]},
    {'要么设计继承并提供文档说明 ，要么禁止继承':[
        '通过构造器调用私有的方法，final方法和静态方法是安全的，这些都不是可以被覆盖的方法'
    ]},
    {'接囗优于抽象类':[
        ''
    ]}

],
'':[

],
'':[

],
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t11 = t1.addSubTopic()
                t11.setTopicHyperlink(t1.getID()) 
                t11.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTopicHyperlink(t11.getID()) 
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTopicHyperlink(t111.getID()) 
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t11111 = t1111.addSubTopic()
                                                    t11111.setTopicHyperlink(t1111.getID()) 
                                                    t11111.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t111111 = t11111.addSubTopic()
                                                                t111111.setTitle(u)
                                                                for y in p[u]:
                                                                    t1111111 = t111111.addSubTopic()
                                                                    t1111111.setTitle(y)
                                                        else:
                                                            t111111 = t11111.addSubTopic()
                                                            t111111.setTopicHyperlink(t11.getID()) 
                                                            t111111.setTitle(p)                                                        
                                            else:
                                                t11111 = t1111.addSubTopic()
                                                t11111.setTopicHyperlink(t111.getID()) 
                                                t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTopicHyperlink(t111.getID()) 
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTopicHyperlink(t11.getID()) 
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTopicHyperlink(t1.getID()) 
            t11.setTitle(i) 


topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\tcp.xmind") 