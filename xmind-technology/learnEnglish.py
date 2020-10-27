import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\learnEnglish.xmind") 
s2=w.createSheet()
s2.setTitle("learnEnglish")
r2=s2.getRootTopic()
r2.setTitle("learnEnglish")


content={
'1.前言':[
    {'误区':[
        '以背单词为核心',
        '语法无用论或语感重要论',
        '口语万能至上论',
        '口音纯正标准论',
        '听力只听标准音',
        '背诵短文很有用',
        '考试考证至上论'
    ]},
    {'策略':[
        '避免社交网络干扰',
        '保持记笔记',
        '起始小期望，循序渐进',
        '养成立即行动的习惯',
        '正面的自我激励模式'
    ]},
    {'基本原则':[
        '和电视剧说拜拜',
        '学习时间调整到早上',
        '零碎时间和大块时间穿插'
    ]}],
'2.概述':[
    '使用播讲类材料',
    '从听说入手，易有收获感->对英文感兴趣->越学越想学',
    '突破三个关卡：中级、中高级和听说进阶',
    '完成三大任务：慢速英文听力、常速英语听力、实用英文表达',
    '终极目的:轻松看懂美剧电影，工作中口头交流无障碍',
    {'学习方法':[
        '英文听说透析法',
        '艾宾浩斯复习表格'
    ]}
],
'3.初级':[
    '赖世雄“美语从头学”系列丛书'
],
'4.中级':[
    '攻克变速纯正播讲类材料',
    {'1.攻克英语发音（2～3周）':[
        '赖世雄《赖世雄美语音标》',
        '看书听CD，跟读，书学2～3遍'
    ]},
    {'2.跟读ESLPod（3～4个月）':[
        {'简介':[
            '每期的播客自成一课（20分钟）',
            '1.简单介绍课内容和主题',
            '2.一段慢速对话或故事（1～3分钟）',
            '3.对对话或故事进行讲解（10分钟）',
            '4.正常语速播放对话或故事'
        ]},
        {'六本教材':[
            'Introduction to the United States（《美国简介》）',
            'A Day in the Life of Jeff（《杰夫的一天》）',
            'A Day in the Life of Lucy（《露西的一天》）',
            'Interview Questions Answered（《面试问题回答》）',
            'English for Business Meetings（《商务会谈英语》）',
            'Using English at Work（《工作常用英语》'
        ]},
        {'学习方法':[
            '1.不看教材，全书音频听一遍（2天）',
            '2.读教材，对照着笔记搞定生词和短语（3天）',
            {'3.跟读练习':[
                '丢开课本，播放一句，暂停，跟读（1遍）',
                '翻开课本，不暂停，跟读（6遍）',
                '丢开课本，不暂停，跟读（3遍）'
            ]},
            '4.注意复习:使用第二或第三种方法跟读',
            '5.选做练习：录和听结合'
        ]}
    ]},
    {'发音难点':[
        {'难发的音':[
            '/r/:不发',
            '/l/音和/n/音:/l/音：舌尖抵住上腭发出',
            '/ʊ/和/u:/',
            '/ɪ/和/i:/'
        ]},
        {'语流中的发音':[
            '爆破音/t/和/g/、/k/和/g/、/p/和/b/:词末，不发音，停顿0.1秒',
            '注意at的读法',
            '音变: t在末尾,浊化，t在词中，读/d/， /h/音省略'
        ]}
    ]}],
'5.中高级':[
    {'1.发音复习（2～3周）':[
        {'American Pronunciation Workshop（《美语发音教程》':[
            '视频可在优酷观看学习',
            '主播说得很慢，附带字幕，不需做笔记，跟读即可',
            '一共16段视频，每段视频长20分钟'
        ]},
        {'爱荷华大学的口腔剖面':[
            '网址：http://soundsofspeech.uiowa.edu/english/english.html'
        ]}
    ]},
    {'2.常速多口音EnglishPod（2～3个月）':[
        '1.确定水平，VOA慢速无问题',
        '2.制订计划，每天听几课、如何复习',
        '3.拿到一课内容，先听讲解录音（记得做笔记），听2遍，听懂即可',
        '4.听对话录音，约一分钟时长，听9遍',
        '5.跟读，注意语调，体会英语的韵律之美',
        '6.看文本跟读3遍，不看文本且不中断一口气跟读9遍',
        '7.注意复习',
        '8.一段时间后，挑出喜欢的一期，用手机录音。录音时尽量不停顿，回想会话场景和语气',
        '9.原音和录音分别听9次，如对录音不满意，重复5,6步并再次录音'
    ]}],
'6.高级':[
    'American Accent Training（《美语发音秘诀》',
    '1.浏览目录，清楚书的编排结构，从头到尾通读几遍',
    '2.边看书边听音频，多听几遍',
    '3.一章节一章节突破，跟着音频做每章练习题'
    ],
'7.语法学习':[
    '台湾旋元佑老师的《语法俱乐部》',
    {'内容':[
        '第一篇:简单句:五种基本句型，时态、不定式等',
        '第二篇:复合句与复杂句',
        '第三篇:简化从句(不符合语法规则的句子)和倒装句'
    ]},
    {'学习方法':[
        '1.一个月时间把书认真钻研一遍',
        '2.阅读大量文章，记录遇到的问题',
        '3.再读一遍书，然后再读文章',
        '4.读两三个月后，再回头把书读一遍'
    ]},
    '学习《剑桥中级英语语法》'
],
'8.单词积累':[
    '听，听实时英语新闻，可选媒体BBC，CNN，Al Jazeera',
    '说，英语聊天',
    '读，读原版英文，从短信、邮件到大部头的专著',
    '写，写英文邮件和短信',
    {'选择适合的英文原著':[
        '生词量：“首万词”不重复词数',
        '蓝思值：句子复杂程度的测算',
        '兴趣'
    ]},
    {'透析英文读物':[
        '透析准备：测试词汇量',
        '核心操作：50%自适应查词',
        '猜生词抓住英文原著大意',
        '识破英文原著中的“猫腻”'
    ]},
    {'训练计划':[
        '七天行动1：置之死地而后生',
        '七天行动2：欲速则不达',
        '读到翻页之前绝不做其他事情',
        '长期激励：承诺一年读10本原著',
        '每读完一本就写透析记录'
    ]},
    {'坚持效果':[
        '记忆效应1：单词会反复出现',
        '记忆效应2：单词的背景很强大',
        '英文原著为口语源源不断地输送“弹药”',
        '考试得高分'
    ]}],
'9.提升商务英语':[
    '商业小说',
    '商业励志书',
    '商业教科书',
    '商业期刊',
    '商务写作之模板激励',
    '手把手教你写好英文简历']
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\learnEnglish.xmind") 