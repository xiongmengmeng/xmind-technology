import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\philosophy.xmind") 
s2=w.createSheet()
s2.setTitle("philosophy")
r2=s2.getRootTopic()
r2.setTitle("philosophy")


content={
'孔子':[
    {'核心思想':[
        '仁：爱人'
    ]},
    {'具体':[
        '国家：礼治和德治',
        '个人：爱人',
        '中庸：平衡仁和礼'
    ]},
    '《六经》,《论语》'
],
'老子':[
    {'前提':[
        '阴阳五行',
        '《易经》,《易传》=《周易》'
    ]},
    {'故事':[
        '孔子问礼',
        '函谷关留书'
    ]},
    '《道德经》',
    {'重点':[
        '道：自然规律',
        '辩证法：物极必反',
        '无为：无为而无不为'
    ]},
    {'具体':[
        '反对义务教育',
        '反对尚贤',
        '反对生产奢侈品'
    ]}
],
'墨子':[
    '平民出身',
    '科圣',
    '代表底层人民利益',
    {'十论':[
        '兼爱&非攻（惩恶扬善）：love&peace',
        '非乐，节葬，节用',
        '非命，天志，明鬼',
        '尚贤，尚同'
    ]}
],
'孟子':[
    '推广，升级儒学',
    '民贵君轻',
    '性善论：人心向善',
    '仁政',
    {'具体':[
        '经济：井田制，少收税',
        '政治：招揽人才',
        '教育：更多人学习文化知识'
    ]},
    '目标：国富，民强',
    '《孟子》'
],
'荀子':[
    '人之生固小人',
    '性恶论',
    '《劝学》',
    '提倡礼制，遏制人的欲望'
],
'天命观':[
    '万物有灵',
    '天，用巫术与天沟通',
    '天子',
    '天命有常',
    '天命无常，惟德是从',
    '知天命',
    '顺天命',
    '制天命'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\philosophy.xmind") 