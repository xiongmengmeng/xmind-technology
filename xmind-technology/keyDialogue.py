import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\keyDialogue.xmind") 
s2=w.createSheet()
s2.setTitle("关键对话")
r2=s2.getRootTopic()
r2.setTitle("关键对话")


content={
'1.关键对话':[
    '高风险',
    '不同观点',
    '激烈情绪'
    ],
'2.真正目的':[
    {'受到攻击':[
        '战胜对方',
        '惩罚对方',
        '寻求安全港湾'
    ]},
    '控制情绪'
],
'3.安全感':[
    {'缺失':[
        '暂停对话',
        '营造安全气氛'
    ]},
    {'条件':[
        '共同目的',
        '互相尊重'
    ]},
    {'缺失引起的问题':[
        '自我防御',
        '绵里藏针',
        '无端指责',
        '老调重弹'
    ]},
    {'重建':[
        '道歉',
        '对比法消除误解：否定+肯定',
        {'提出共同目的':[
            '积极寻找共同目的',
            '识别策略背后的目的',
            '开发共同目的',
            '和对方共同构思新策略'
        ]}
    ]}],
'4.管理情绪':[
    '行为->感受->想法->事实',
    {'行为方式回顾':[
        '1．关注你的行为表现:我是否陷入了沉默或暴力应对方式？',
        '2．确定行为背后的感受: 导致这种行为的情绪感受是什么？',
        '3．分析感受背后的想法:造成这种情绪出现的想法是什么？',
        '4．寻找想法背后的事实:形成这种想法的事实依据是什么？',
        {'5．留意三种常见的“小聪明”':[
            '受害者想法——“这可不是我的错！”',
            '大反派想法——“这都是你造成的！”',
            '无助者想法——“这事我也没办法！”'
        ]}
    ]},
    {'改变主观臆断':[
        '把受害者变成参与者:我是否故意忽略自己在这个问题中的责任？',
        '把大反派变成正常人: 一个理智而正常的人为什么会这样做？',
        '把无助者变成行动者:我的真实目的是什么？',
        '我希望为自己、他人、我们的关系实现什么目的?',
        '要想实现这些目的，现在我该怎么做？'
    ]}],
'5.陈述观点':[
    {'内容上':[
        {'分享事实经过':[
            '事实—————不会引起争议的内容',
            '事实—————最具说服力的内容',
            '事实—————最不会令人反感的内容'
        ]},
        {'说出你的想法':[
            '表现得自信',
            '不要堆积问题',
            '注意安全问题'
        ]},
        '征询对方观点',
    ]},
    {'方式上':[
        {'做出试探表述':[
            '事实是……”改为“我认为……”',
            '“人人都知道……”改为“有3位供应商和我谈过，他们认为……”',
            '“很明显……”改为“我有点怀疑是否……”',
            '要谨慎，但不要软弱'
        ]},
        {'鼓励做出尝试':[
            '鼓励对方说出不同的看法',
            '不要虚张声势',
            '抛砖引玉',
            '坚持这样做，直到他们真正理解你交流的意愿'
        ]}
    ]}],
'6.了解动机':[
    {'自我审视——做好倾听的准备':[
        '真诚',
        '好奇',
        '坚持',
        '耐心',
        '鼓励对方探索行为模式'
    ]},
    {'四种倾听手段':[
        '询问观点',
        '确认感受',
        '重新描述:不要急于求成',
        '主动引导'
    ]},
    {'对对方的观点做出响应时':[
        '赞同',
        '补充',
        '比较'
    ]}],
'7.开始行动':[
    {'两种陷阱':[
        '错误期望',
        '不作为'
    ]},
    {'决策的四种方式':[
        '命令式',
        '顾问式',
        '投票式',
        '共识式'
    ]},
    {'明确执行细节':[
        '行动人',
        '行动目标',
        '行动时间:截止时间[重要]',
        '检查方法',
        '记录工作'
    ]}]
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\keyDialogue.xmind") 