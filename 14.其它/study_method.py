import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("interview")
r2=s2.getRootTopic()
r2.setTitle("interview")


content={

'学习习惯，怎么学习，现在在学习什么':[
    {'学习途径':[
        {'书籍':[
            {'好处':[
                '内容相对比较系统，能够了解一个东西的全貌'
            ]},
            {'坏处':[
                '每一方法都详细，让人不知道重点在哪里'
            ]},
            {'解决':[
                '1.看第一遍后，可以对书籍内容做下大致分类',
                '2.然后在工作中，思考和使用',
                '如果项目中在使用，可以思考下东西是怎么用的，有什么优化空间，redis使用，设置key的序列化方式',
                '如果项目中没有使用，可以思考下什么场景可以用到，可以试着把它用来需求里,python学习过程',
                '3.隔差不多一年多，可把之前的学习笔记翻出来再过一遍',
                '这个时候通常就会知道知识的重点在哪里，可以自己画图把重点流程梳理出来，也可以对核心内容做下总结'
            ]}
        ]},
        {'视频':[
            {'好处':[
                '通俗易懂，标记重点，对一些看博客较难理解的内容，我会去搜相关视频'
            ]},
            {'坏处':[
                '不够系统'
            ]},
        ]},
        {'公众号/博客':[
            {'好处':[
                '上下班途中或上班遇到不懂的问题就可以翻阅，方便使用',
                '一些公众号的质量也很不错，对一些知识的简介很深入，但也可以很通俗'
            ]},
            {'坏处':[
                '知识点散乱，不够系统'
            ]},
        ]}
    ]},
    {'学习方式':[
        '1.每年有相映规则，不拘泥于具体形势',
        {'去年':[
            '1.学习了python,爬虫，并且也在工具中使用它,帮产品做了很多的数据处理工作',
            '2.学习springboot相关内容',
            '3.把之前学习的jvm部份重新看了下，然后整理成文档'
        ]},
        {'今年':[
            '1.之前看过挺多书籍的，今天打算过之前看过的书籍再过一遍，对核心内容做下汇总'
            '暂时已经梳理了线程，mybatis源码部分',
            '2.学习spring源码，整理的内容也都发到博客上了',
            '3.学习dubbo源码'
        ]},
        '2.把内容梳理成思维导图'
    ]}
],
'工作中遇到的有挑战性的问题':[
    {'物流系统重构':[
        {'遇到问题':[
            '1.代码质量',
            '2.进度拖沓'
        ]},
        {'代码质量':[
            '因为带的新人做事不太积极，代码规则不太好',
            {'努力':[
                '给他们的代码做了codeReview,办理出相关问题，发了相关文档给他们'
            ]},
            '但他们只改了一小部分，很多问题还是没有改',
            {'努力':[
                '组织了codeReview了串讲(约个会议室，同组人员参加，大家讲下各自的代码)',
                '我首先有讲自己的，使用了什么设计模式，跟着代码讲解了各处的代码规范',
                '因为有别的组员在，也有领导在，他们代码确实也做了一些优化',
                '但会上大家提的反馈的问题，提的建议，后期还是没有改的为这样的会议是有会议记要的，大家一般会根据会议记要来修正代码)'
            ]},
            '经过这些努力，只能说代码勉强可以合格'
        ]},
        {'进度拖沓':[
            '不及时维护tapd，不问题不及时反馈，拖到提测再提出来',
            {'努力':[
                '每天下班前组织站会，让大家反馈各自问题及遇到的问题'
            ]}
        ]},
        {'结果':[
            '通过一些方法，确实可以解决代码质量不高，进度拖沓的问题，但是确实付出了很大的成本',

        ]},
        {'换人':[
            '已经做了两期，第三期我已经决定换人了，换成比较靠谱的同事，这是彻底解决上问题的方法',
            '因为你永远叫不醒装睡的人',
        ]},
        {'结果':[
            '后面换成了靠谱的同事，工作就很顺畅，我只需要分工，每周五周会前提醒大家维护tapd',
            '过程中遇到一些遗漏的改动点，旧代码不合理的地方等等，就在群里说一下，有空就承接下，没空就我来改，很美好'
        ]},
        {'总结':[
            '解决一个非常困难的问题时，可以思考下这个问题是否是一定是要解决的，有时候解决问题，只需要解决(换掉)造成这个问题的人',
            '我们做需求也是，有时产品的设计很难实现，我们不一定要绞尽脑汁去想解决方案，可以根据需求目标，给产品提供另一个替代方案就可以了'
        ]}
    ]},
    {'线上问题':[
        {'现象':[
            '供应商订单表的一个字段赋值错误，导致后续流程卡住'
        ]},
        {'出现频率':[
            '不高，大概一周一二单，解决'
        ]},
        {'涉及代码':[
            '订单拆分与推送模块，也交易，erp，物流三者的交汇地带',
            '三个部门都要负责，但三个部门也都不太想负责，但物流在下游，会影响自身业务，肯定是物流来排查'
        ]},
        {'解决':[
            '1.加日志，出现问题，看日志，缩小排查范围',
            '2.再加日志,循环这个过程，最后定位到出问题的方法',
            '3.然后对问题方法，做单元测试，debug,排查出问题点',
            '过程并不难，但需要毅力跟坚持吧，问题从出现到解决，其实是花费了一个多月时间的'
        ]},
        {'后续':[
            '把查物流数据的内容抽出来封装成接囗，把订单拆分与推送流程交接给erp'
        ]}
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 