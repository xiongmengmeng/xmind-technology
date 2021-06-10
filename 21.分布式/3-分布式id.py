import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="分布式"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式事务")
r2=s2.getRootTopic()
r2.setTitle("分布式事务")


content={
'分布式ID生成系统':[
    '高可用',
    '高并发'
],
'数据库自增id':[],
'数据库多主模式':[
    '1.针对分表，设置成不同步长',
    '2.建一个表专门用来生成表id',
],
'号段模式':[
    'maxid:0->1000->2000',
    'length:1000',
    'version:本质就是cas'
],
'滴滴Tinyid':[
    {'表结构tiny_id_info':[
        'id:自增主键',
        'biz_type:业务类型',
        'begin_id:开始id,仅记录初始值,初始时与max_id相同',
        'max_id:当前最大id',
        'step:步长',
        'delta:每次id增量',
        'remainder:余数',
        'version:版本号'
    ]},
    {'SegmentId号段':[
        'long maxId:最大id',
        'AtomicLont currentId:当前的id',
        'long loadingId:用来触发封装nextSegmentId',
        'delta:步长',
        'remainder',
        'isInit',
        {'nextId()':[
            {'1.初始化':[
                'init()'
            ]},
            {'2.自增':[
                'long id=currentId.addAndGet(deta)'
            ]},
            {'3.返回':[
                '如果id>maxid,返回new Result(ResultCode.OVER,id)',
                '如果id>loadingId,返回new Result(ResultCode.LOADING,id)',
                '否则，返回new Result(ResultCode.NORMAL,id)'
            ]}
        ]}
    ]},
    {'idGenerator(id生成器)':[
        'SegmentId current',
        'SegmentId next',
        {'nextId()':[
            {'1.current==null':[
                'loadCurrent()',
                'coutinue'
            ]},
            {'2.得到下一个id':L[
                'Result result=current.nextId()'
            ]},
            {'3.根据result中返回的状态做不同处理':[
                '状态为ResultCode.OVER:loadCurrent()',
                '状态为ResultCode.LOADING:loadNext()',
                '状态为ResultCode.NORMAL:return.getId()'
            ]},
            '以上过程都在一个循环里'
        ]}
    ]}
],
'雪花算法':[
    'twitter开源分布式id生成算法，不依赖数据库',
    '让负责生成分布式id的每台机器在每毫秒内生成不一样的id',
    {'核心思想':[
        '分布式id固定是一个long型的数字，占8个字节，64bit',
        '1bit不用,符号位',
        '41bit:时间戳',
        '10bit:工作机器id',
        '12bit:序列号,4096',
    ]},
    '以上bit位可以改',
    {'实现':[
        '1.定义起始时间戳',
        '2.定义各部分占的位数，最大值，向左的移位',
        {'nextId()':[
            '1.拿到当前系统的毫秒数START_STMP',
            {'2.currStmp<lastStmp':[
                '抛异常',
            ]},
            {'2.currStmp==lastStmp':[
                {'序列号+1':[
                    'seuqence=(sequence+1)&Max_sequence',
                    '返回为0，代表同一毫秒内序列数已经达到最大'
                ]},
                {'同一毫秒内序列数已经达到最大':[
                    'currStmp=getNextMill()',
                    '循环等待下一毫秒的到来'
                ]}
            ]},
            {'3.不同毫秒':[
                'seuqence=0',
            ]},
            {'4.组装id':[
                'lastStemp=currStemp',
                'currStemp-START_STMP)<<TIMESTMP_LEFT//时间戳部分',
                '|datacenterId<<DATACENTER_LEFT//数据中心部分',
                '|machineId<<MACHINE_LEFT//机器标识部分',
                '|sequence//序列号部分'
            ]}
        ]}
    ]},
    {'使用':[
        '百度uid-generator',
        '美团leaf'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 