import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\cpu.xmind") 
s2=w.createSheet()
s2.setTitle("cpu2_memory")
r2=s2.getRootTopic()
r2.setTitle("计算机基础")


content={
'内存':[
    {'物理模型':[
        {'内存IC构造':[
            'VCC和GND是电源',
            'A0～A9是地址信号的引脚',
            'D0～D7是数据信号的引脚',
            'RD和WR是控制信号的引脚']},
        {'内存IC大小估算':[
            '数据信号引脚8个：一次可以输入输出8位（=1字节）的数据',
            '地址信号引脚10个：可指定0000000000～1111111111共1024个地址',
            '地址:表示数据的存储场所',
            '这个内存IC可存储1024个1字节数据，1024=1K,该内存IC容量为1KB'
        ]}
    ]},
    {'逻辑模型':[
        '楼房:1层可以存储1个字节的数据，楼层号表示的就是地址'
    ]},
    {'指针':[
        '一种变量，不表示数据的值，而表示存储着数据的内存地址',
        '通过指针，可以对任意指定地址的数据进行读写',
        '指针的数据类型表示一次可以读写的长度'
    ]},
    {'数组':[
        '定义：多个同样数据类型的数据在内存中连续排列的形式',
        {'分类':[
            '栈:使用LIFO（LastInput First Out，后入先出）方式',
            '队列:使用FIFO（First Input First Out，先入先出）方式',
            '链表:更加高效地对数组数据（元素）进行追加和删除处理',
            '二叉查找树:使数据的搜索更有效率'
        ]}
    ]}],
'磁盘':[
    {'物理结构':[
        '扇区方式',
        '可变长方式'
    ]},
    {'扇区':[
        '定义：对磁盘进行物理读写的最小单位',
        '1个扇区是512字节,1簇=512字节=1扇区',
        '不管是多么小的文件，都会占用1簇的空间',
        '文件占用磁盘空间都是1簇的整数倍'
    ]},
    {'作用':[
        '存储程序,缺点是读取速度慢',
        '应用启动时，程序会由磁盘加载到内存'

    ]},
    {'重要概念':[
         {'虚拟内存':[
            '把磁盘的一部分作为假想的内存来使用',
            '实际上正在运行的程序，必须存在内存中',
            '实现：把实际内存的内容，和磁盘虚拟内存的内容进行部分置换，并同时运行程序',
            '虚拟内存的方法有分页式和分段式,页大小为4KB',
            '虚拟内存能避免因内存不足导致的应用无法启动',
            '虚拟内存使用时的Page In和Page Out往往伴随低速的磁盘访问->应用的运行变得迟钝']},
         {'磁盘缓存（disk cache）':[
             '从磁盘中读出的数据存储到内存空间中']}
    ]},
    {'节省内存的方法':[
        'DLL（Dynamic Link Library）文件实现函数共有:程序运行时可以动态加载Library文件',
        'Library（函数和数据的集合）',
        '调用_stdcall来减小程序文件大小'
    ]}],
'文件压缩':[
    '文件：字节数据的集合体',
    {'压缩算法':[
        {'RLE算法':[
            '把文件内容用“数据×重复次数”的形式压缩',
            '缺点:文本文件中，同样字符多次重复出现情况少',
            '适用于压缩图像，exe文件']},
        {'哈夫曼算法':[
            '常出现数据用小于8位字节数表示，不常用数据用超过8位的字节数表示',
            '为各压缩对象文件构造最佳编码体系，并以该编码体系为基础进行压缩',
            '用二叉树实现哈夫曼编码:构建能够明确进行区分的编码体系',
            '应用：压缩软件LHA'
        ]}
    ]},
    {'可逆和非可逆压缩':[
        '原始的图像文件是BMP格式',
        'JPEG格式文件：非可逆压缩，还原后图像信息有部分模糊',
        'GIF格式文件：可逆压缩，因有色数不能超过256色，还原后颜色会有一些缺失'
    ]}]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split("：")
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\cpu.xmind") 