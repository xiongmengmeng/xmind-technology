import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\learningMethod.xmind") 
s2=w.createSheet()
s2.setTitle("learningMethod")
r2=s2.getRootTopic()
r2.setTitle("learningMethod")


content={
'高效记忆':[
    {'三个关键点':[
        '记忆过程趣味化',
        '待记忆碎片信息连成整体->有规律的整块记忆',
        '借助自己熟悉的内容来记忆新知识点，以旧带新'
    ]},
    {'五大记忆能效提升方法':[
        '多感官刺激记忆法',
        '缩略词记忆法',
        '联想记忆法',
        '晨起／睡前记忆法',
        '故事串联记忆法'
    ]}
],
'超级笔记':[
    {'5R笔记法':[
        'Record，记录',
        'Reduce，简化、简写',
        'Recite，背诵、记忆',
        'Reflect，思考、回顾',
        'Review，复习'
    ]},
    {'记笔记方法':[
        '主题分类笔记法',
        '移动笔记法：便利贴',
        '录音笔记法'
    ]}],
'有效预习':[
    '限制时长专注预习法',
    {'制定合理目标预习法':[
        '促进旧知识内化',
        '与新知识“混个脸熟”',
        '发现最难知识点'
    ]},
    {'LEO牌实操预习法':[
        '预习前极速复习',
        '抽象+具象混搭:公式定理同具体习题案例相结合',
        '动笔之后再听课:标记未理解部分，听课有重点'
    ]}],
'科学复习':[
    {'分阶段复习法':[
        '小复习',
        '中复习',
        '大复习',
        '大考前复习'
    ]},
    '关键词串联回忆复习法',
    '小组互考复习法'
    ],
'善做作业':[
    '提前库存法',
    '碎片时间见缝插针法',
    '不同作业间歇转换法:换脑子、防枯燥、提效率',
    '先复习再做作业',
    '假设考试作业法'
],
'重视错题':[
    '遇到错题时，不“想当然”、不逃避',
    {'把应对错题变成一件“其乐无穷”的事':[
        '确认错因',
        '对症下药',
        '错题整理归档，定期复习'
    ]}
],
'战胜偏科':[
    '重建自信',
    '诊断&评估',
    '制订偏科补救计划',
    '执行与结果评定'

],
'请教老师':[

    '....'
],
'培养逻辑思考力':[
    '5W2H分析思考法',
    '鱼骨图分析法（又称因果分析法）',
    '金字塔原理法：'
],
'学会速读':[
    '确定速读素材',
    '速读前:快速转眼速读法',
    '速读中:7:3原则速读法',
    '速读后:三分钟闭眼过电影法'
],
'掌握精读':[
    '精读开始前，明确任务量、制订整体阅读计划',
    {'二不做二做':[
        '不整段画重点',
        '不重复摘抄书中的事实性陈述',
        '在笔记里主要记录自己的所思所想',
        '积极进行批判性思考，利用“多色批注法”记录自己的观点立场'
    ]},
    '朗读+录音精读法'
],
'写作入门':[
    '建立“灵感与素材本”',
    '写作练笔“四定原则”：·定期定量，定时，定字数，定主题',
    '语音／口头作文法',
    {'规避流水账的建议':[
        '开始练笔时，不选难度过高的生僻选题',
        '动笔前确立中心思想，动笔后聚焦中心思想+论点，抛除一切不相关论述'
    ]},
    {'写作心得':[
        '不论写什么，列提纲都有利无害',
        '内容／观点／立意永远第一，不刻意堆砌华丽辞藻',
        '写作时真心诚意，切勿虚情假意',
        '写完后请他人帮助评点，能发现被自己忽视的漏洞'
    ]},
    {'三要素写作法':[
        '可信',
        '情感',
        '逻辑'
    ]}
],
'合理减压':[
    '积极心理暗示法',
    '他人经历排压法',
    '...'
],
'提高注意力':[
    '番茄钟工作法',
    '与世隔绝法',
    '激励法',
    '两分钟原则法：能两分钟完成的事情，绝不拖到第三分钟去做'
],
'快速自学':[
    '请教牛人法',
    {'3A自学法':[
        'Anywhere，Anytime，Anything',
        '自学时做好记录',
        '自学后经常回顾'
    ]}
],
'时间管理':[
    '每日任务清单（To-do list）',
    '周计划／月计划表',
    '四象限记录法'
],
'学好英语':[
    {'单词':[
        '英到中、中到英、不同词性、变体时态、例句回顾'
    ]},
    {'语法':[
        '《薄冰英语语法》'
    ]},
    {'听力':[
        '...'
    ]},
    {'阅读':[
        '读得杂、读得频，大量读，精读和泛读相结合'
    ]},
    {'口语':[
        '说的内容大于语音语调',
        '大量、反复练习',
        '《英文经典演讲50篇》之类带音频的书'
    ]}
],
'其它':[
    'SMART原则法',
    'OKA工作法',
    '五步法'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\learningMethod.xmind") 