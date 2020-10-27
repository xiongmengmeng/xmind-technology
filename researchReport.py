import xmind
from xmind.core.markerref import MarkerId

w = xmind.load("c:\\Users\\btr\\Desktop\\researchReport.xmind") 
s2=w.createSheet()
s2.setTitle("researchReport")
r2=s2.getRootTopic()
r2.setTitle("研报")


content={
'研报':[
    {'定义':[
        '指证券公司为提供投资咨询服务而发布的研究报告']},
    {'分类':[
        {'宏观研究':[
            '经济运行指标（GDP、CPI、PPI、固投、工业增加值、进出口）'
            '先行指标（PMI、发电量、高炉开工、房地产销售）的研究报告',
            '流动性（货币、社融、利率、汇率）',
            '相关的宏观专题报告（例如供给侧改革、雄安新区、军改、国改等）',
            '世界经济方面的研究报告'
        ]},
        {'债券研究：也叫固收（固定收益）研究':[
            '特点：一是机构市场，二是资金市场',
            '债市反映了金融市场基本的流动性情况'
        ]}
        {'策略研究':[
            ''
        ]},
        '读研报的话，先宏观，继而策略，最后行业，或策略、宏观相互印证入手，再及行业，是理想的入门之径'
        {'行业研究':[
            '题目都是A+B型，A是行业，B是观点',
            '行业专题、数据、动态、简评以及行业策略'
        ]},
        '公司研究',
        '金融工程研报'
    ]}],

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

xmind.save(w,"c:\\Users\\btr\\Desktop\\researchReport.xmind") 