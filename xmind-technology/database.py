import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\database.xmind") 
s2=w.createSheet()
s2.setTitle("algorithm")
r2=s2.getRootTopic()
r2.setTitle("algorithm")


content={
'1.数据结构':[
    '关系型、键-值对型、列型、文档型、图型',
    'CAP原理或MapReduce',
    'MongoDB和CouchDB（二者实现文档数据库的不同方式)',
    'Riak:Dynamo（亚马逊的数据库）的一种实现',
    'HBase:BigTable（谷歌的数据库）的一种实现'
    {'':[
        '这是什么类型的数据库？',
        '驱动力是什么',
        '如何与数据库交互',
        '每种数据库的独特性体现在哪里',
        '每种数据库的性能如何',
        '每种数据库的可伸缩性如何'
    ]}
],
'PostgreSQL':[
    {'关系、CRUD和联接':[
        '关系为表（TABLE），属性为列（COLUMN），元组为行（ROW）',
        '联接',
        '索引',
        'B树',
        ' 聚合',
        ' 分组 GROUP BY  DISTINCT',
        '窗口函数',
        ' 事务',
        '存储过程'
    ]},
    {'选择排序':[
        '从待排序的数据中寻找最小值，将其与序列最左边的数字进行交换',
        '总的比较次数为（n-1）+（n-2）+…+1≈n2/2',
        '复杂度为O（n2）'
    ]}
]

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
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\database.xmind") 