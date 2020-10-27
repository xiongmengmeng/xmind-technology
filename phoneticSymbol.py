import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\phoneticSymbol.xmind") 
s2=w.createSheet()
s2.setTitle("phoneticSymbol")
r2=s2.getRootTopic()
#英语音标
r2.setTitle("phoneticSymbol")


content={
'单元音':[
    'ɔ:ɜːu:ʌɒəʊeɪaɪɔɪɪəeəʊəəʊ',
    {'i':[
        '读音：yi',
        'eat/need/thief/heat/sheep'
    ]},
    {'ɪ':[
        '读音：ei',
        'sit/fit/give/kiss'
    ]},
    {'e':[
        '读音：ai',
        'bed/let/pen'
    ]},
    {'æ':[
        '读音：ai',
        'bad/dad/matter/bag/land'
    ]},
    {'ɑ':[
        '读音：啊',
        'lock/hot/stop/block/cop/ox'
    ]},
    {'ɔ':[
        '读音：噢',
        'hall/law/saw/tall'
    ]},
    {'u':[
        '读音：乌，嘴唇较平',
        'too/mood/food/soon/cool/fool/move'
    ]},
    {'ʊ':[
        '读音：乌饿，嘴唇较开',
        'book/good/would/foot/full'
    ]},
    {'ʌ':[
        '读音：饿',
        'bus/money/tougf/color/hut/cup'
    ]},
    {'ə':[
        '读音：饿',
        'ago/seven/sofa/student/saddle'
    ]},
    {'ɜ':[
        '读音：尔',
        'bird/her/worry/certain/learn/person/birth/church'
    ]}
],
'双元音':[
    {'ar':[
        '读音：啊尔',
        'hard/far/artist/park/Mars'
    ]},
    {'ɔr':[
        '读音：噢尔',
        'born/for/warning/four/mourn/pour'
    ]},
    {'ɔɪ':[
        '读音：噢ei',
        'coin/noise/boy/joy/soil/oil/coil'
    ]},
    {'o':[
        '读音：欧屋',
        'coat/soap/open/bowl/coal'
    ]},
    {'ʊr':[
        '读音：屋尔，卧',
        'townr/your/poor/moor'
    ]},
    {'er':[
        '读音：尔',
        'letter/temper/nature'
    ]},
    {'aɪ':[
        '读音：啊ei  爱',
        'life/child/idea/kite'
    ]},
    {'aʊ':[
        '读音：a+o=ao',
        'down/how/house/cow/doubt/loud/owl/drought/nowadays'
    ]},
    {'er':[
        '读音：air',
        'spare/share/chair/hair/fair/fare'
    ]},
    {'ɪr':[
        '读音：ei+饿（卷）',
        'here/beer/hear/were'
    ]},
    {'ɪə':[
        '读音：ei+饿（不卷）',
        'idea'
    ]},
    {'iə':[
        '读音：yi+饿（不卷）',
        'real'
    ]}
],
'铺音':[
    {'p':[
        '读音：前p后pu',
        'peak/pay/cup/top/pat'
    ]},
    {'b':[
        '读音：前b后bu(不发)',
        'bey/beat/mob/boy/robbler/mob'
    ]},
    {'t':[
        '读音：t(后不发)',
        'take/teacher/hit/sit'
    ]},
    {'d':[
        '读音：d(后不发)',
        'day/under/red/wanted/patted'
    ]},
    {'k':[
        '读音：k(后不发)',
        'key/cake/book'
    ]},
    {'g':[
        '读音：g',
        'gate/get/bag/mug/forget/gap'
    ]},
    {'f':[
        '读音：f',
        'food/left/wife'
    ]},
    {'v':[
        '读音：v',
        'very/never/give/vase/leave'
    ]},
    {'θ':[
        '读音：s',
        'thank/healthy/both/thick/mouth/bath/breath'
    ]},
    {'ð':[
        '读音：z(振)',
        'that/father/with/breathe'
    ]},
    {'s':[
        '读音：s',
        'see/ask/class/sister/whisptor/whisky',
        's后p->b:spacious',
        's后k->g:speak/skirt/skillfull',
        's后t->d:steak/standard',
        't+s=c(刺)：bats/seats'
    ]},
    {'z':[
        '读音：z',
        'zebra/busy/is/eyes/plays',
        'd+s=z:beds/kids'
    ]},
    {'ʃ':[
        '读音：sh',
        'ship/show/sure/she/sheep/shake/machine'
    ]},
    {'ʒ':[
        '读音：日',
        'pleasure/usual/television/occasion/measure/',
        'garage/regim/leisure/treasure'
    ]},
    {'tʃ':[
        '读音：取',
        'church/chase/teach/cheap/nature/mature/ditch'
    ]},
    {'dʒ':[
        '读音：zhe/zh/ji(尾)',
        'jade/joy/judge/page/joke/danger/strange'
    ]},
    {'ŋ':[
        '读音：eng',
        '单词：ing/ink'
        'sing/wing/link/sink/bring/drink/think/thing',
        {'区别ŋə与ŋgə':[
            'ŋə:singer/hanger',
            'ŋgə:finger/anger'
        ]}
    ]},
    {'l':[
        '读音：前乐/后ou',
        'like/lake/all/sell/long/call/look'
    ]},
    {'r':[
        '读音：前r/后er',
        'right/grade/ear/poor/read/red/part/rock/correct'
    ]},
    {'j':[
        '读音：ye yi',
        'yard/yet/you/yes/young/year/yeast/yale',
        'tju/nju->tu/nu:',
        '变音：this/year'
    ]},
    {'h':[
        '读音：h',
        'hi/hate/he/hat/hot/hair/home'
    ]},
    {'w':[
        '读音：乌',
        'we/way/beware/wood/wind/work',
        'wh->w'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\phoneticSymbol.xmind") 