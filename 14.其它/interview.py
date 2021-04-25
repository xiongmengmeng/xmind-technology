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
'离职的原因':[
    '为什么要离职+为什么这个时间+工作期待',
    '1.肯定这份工作给自己带来的经验的积累和成长，深度和维度',
    '2.表达下客观原因，不带情绪',
    '3.表达乘风破浪的进取心',
    '个人成长价值+薪酬体系客观原因无法突破',
    '个人成长价值吧，我上家公司的技术部门其实很优秀，有完整的技术栈，以及非常成熟的工作流程体系',
    '从技术层面，和工作能力来说，都得到了很大的锻炼和提升',
    '但因为公司发展出了些问题，从去年取消了绩效和补贴，还有晋升制度',
    '但我去年没有离职，因为我对自己的职业规划是比较明确的，一是在上家公司我还是有可以提升的空间的，二是我想下份工作可以换份TOC的工作，更有挑战性'，
    '今年觉得自己已经准备好了'
],
'对加班怎么看':[
    '上一份工作的时间：早上十点，晚上七点半(包括晚饭时间)，晚上值班，物流高峰，十二点前反馈的问题，一般要做下处理'
    '自己能够接受的工作强度和工作节奏',
    '反问这份工作的强度'
],
'投入最多的项目':[
    '',
    ''
],
'当前在面试其他公司的情况':[
    '',
    ''
],
'未来的规则':[
    '',
    ''
],
'你有什么问题想问我的吗':[
    '1.团队情况：这个岗位所以部门的团队情况是怎样的，我直接汇报对象是谁'
]
'面试催回复':[
    '自报身份（姓名+时间+岗位）',
    'xxx你好，我是上周x来面试xxx岗位的xxx',
    '请问一下这个岗位是否已经有确定的人选了',
    '因为我最近确实是要确认新的机会了,',
    '希望您这边尽快能给到回复哦',
    '贵司如果对我个人情况还有要了解的，可以安排两次沟通哦'
],
'':[
    '1.摸清情况：可以先介绍下咱们这里的薪酬体系吗，比如福利，涨薪体系',
    '2.自我定位，以您对我面试的了解',
    '3.迂回谈薪：',
    '肯定对公司团队的认可：',
    '强调自己的价值点和稀缺性：',
    '薪水OK,最快可以多久到岗'
],
'':[
    
    {'技术能力较强':[
        '对项目的把控能力较强，开发效率高，项目均如期上线且上线后较为稳定;',
        '代码质量好，会跟同事间进行codeReview,持续提升物流系统代码质量;',
        '一直都在提升技术能力，把所学知识应用到系统建设上'
    ]},
    {'做事积极主动，责任心较强':[
        '正式做需求前会做技术设计，列出需求的所有改动点，就细节问题与产品测试达成共识',
        '减少开发过程中需求变动的风险，同时对可能出现的异常情况提出解决方案，预防线上问题的发生',
        '值班时即时响应业务方，快速定位问题原因，修复问题数据，保证业务的正常运作',
        '后续，能代码解决的线上问题，均在一周内上线解决，不能解决的，会输出文档，方便同事值班时使用'
    ]},
    {'注重流程规范':[
        '注重流程规范，也一直在努力优化工作流程，如会在PRD评审前列出所有疑惑点，会上提出与产品测试一起讨论,以此提升会议效率',
        '用例评审时记下开发时可能遗漏的场景，及时修正，提高提测质量'
    ]},
    {'团队意识较强':[
        '在与外部平台对接过程中，会充分准备，技术评审前确认对接内容，评审时做二次确认，提升对接效率',
        '对业务和代码进行过多次分享并输出相关文档，方便同事对相关需求的了解与开发'
    ]},
    {'':[
    ''
    ]}
],
'':[
    {'1.交易平台':[
        '汽配铺商城',
        'CRM-PC',
        'CRM-APP',
        '花果山商城'
    ]},
    {'2.业务平台':[
        '客服系统',
        '物流系统',
        'TMS--移动端',
        '财务系统',
        '通天晓系统'
    ]},
    {'3.商家平台':[
        '天戟ERP系统',
        '商务平台'
    ]},
    {'4.保险平台':[
        '中配保PC',
        '中配保APP（Android，iOS）',
        '青月定损系统'
    ]},
    {'5.数据平台':[
        '巴图鲁开放平台（暂无界面访问）'
    ]} 
]


    ：


。


：
，
;
;
。

： 
，
;。

;
。
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 