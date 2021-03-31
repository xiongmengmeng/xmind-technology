import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("其它")
r2=s2.getRootTopic()
r2.setTitle("其它")


content={
'“饮鸩止渴”提高性能的方法':[
    {'短连接风暴':[
        '先处理掉那些占着连接但是不工作的线程',
        '减少连接过程的消耗:跳过权限验证'
    ]},
    {'慢查询性能问题':[
        '索引没有设计好:直接执行alter table语句(创建索引支持Online DDL)的',
        'SQL 语句没写好：查询重写query_rewrite 功能',
        'MySQL 选错了索引：紧急给这个语句加上 force index'
    ]},
    {'QPS 突增问题':[
        '查询重写功能，把压力最大的 SQL 语句直接重写成"select 1"返回'
    ]}
],
'kill不掉的语句':[
    {'MySQL中的kill命令':[
        'kill query + 线程 id：终止线程中正在执行的语句',
        'kill connection + 线程 id：断开线程的连接'
    ]},
    {'执行kill query thread_id_B 时':[
        '1.把session B运行状态改成THD::KILL_QUERY',
        '2.给session B执行线程发一个信号'
    ]},
    {'kill 无效':[
        {'1.线程没有执行到判断线程状态的逻辑':[
            '等锁，未进入InnoDB',
            'IO压力大，读写IO的函数无法返回，导致不能及时判断线程状态'
        ]},
        {'2.终止逻辑耗时较长':[
            '超大事务执行期间被kill',
            '大查询回滚:删除临时文件需要等待 IO 资源',
            'DDL命令执行到最后阶段被kill:删除中间过程的临时文件,需要等待 IO 资源'
        ]}
    ]},
    '发送kill命令的客户端，不会强行停止目标线程的执行，只是设置了状态，并唤醒对应的线程',
    '被kill线程，需执行到判断状态的“埋点”，才会开始进入终止逻辑阶段(需要耗费时间)',
    {'于客户端误解':[
        '1.如果库里面的表多，连接会慢:不是服务端慢，而是客户端慢',
        '客户端在连接成功后，需多做一些操作：构建一个本地的哈希表（表多，耗时）'
        '2.–quick参数：让客户端变得更快,',
        {'MySQL客户端接收服务端返回结果':[
            '本地缓存，在本地开一片内存',
            '不缓存，读一个处理一个'
        ]},
        '加–quick，使用不缓存方式，如本地处理慢，会导致服务端发送结果被阻塞，让服务端变慢'
    ]}
],
'如何获取当前数据库版本':[
    'mysqladmin --version获取当前安装的数据库版本',
    'rpm -qa | grep mysql查询服务器中mysql安装版本'
],
'选择合适的数据存储方案':[
    'mysql，用mysql存储结构化、关联性强，持久化的数据',
    'mongoDB，用MongoDB存储非结构化的，持久化的数据',
    'redis，用redis存储热点、缓存、非持久化得数据',
    'elasticSearch，用es建立海量数据的索引，进行复杂和数据量很大的搜索服务',
],
'mongoDB的ObjectId 规则':[
    'mongo的_id是一个24位16进制字符串，其中包括时间戳，机器hash码，自增id'
],
'聊聊 MongoDB 使用场景':[
    '非结构化数据，如果一个业务每次产生的数据有多种字段，多种结构，那么需要mongo',
    '数组，如果一个数据的结构类型时数组，而且要查a[i]=?的数据，那么需要mongo',
],
'倒排索引':[
    '正排索引指我们为找到关键字在文档、数据表中的位置建立索引，索引的目的是快速在一个确定的文档中找到关键字的位置，在一张确定的表里找到某行数据',
    '倒排索引相反，是为了找到某个文档，由关键字找文档，由某个记录找到所在表',
    '关键字搜索就需要倒排索引，ES就需要倒排索引',
],
'ElasticSearch 使用场景':[
    '数据库有一张几亿数据的表，查询效率极低，但是插入数据不多，导入es中建立索引，每天同步数据建立索引用于查询',
    '数据库中有很多张表需要连表，但是不需要一张大表，连表效率极低，建立包含的数据导入es',
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 