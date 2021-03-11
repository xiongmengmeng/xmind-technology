import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDBC--DataSource")
r2=s2.getRootTopic()
r2.setTitle("JDBC--DataSource")


content={
'Connection的管理（连接池）':[
    {'数据源DataSource':[
        '目的：解决频繁创建销毁Connection所产生的时间开销问题(会经历TCP的“三次握手”，以及数据库的各种校验)',
        {'做法':[
            '项目启动时初始化固定数量的Connection，把创建连接的时间开销提前',
            '用完Connection不是直接关闭，而是归还到连接池',
            '当连接池现有的Connection不够时，才会去进行耗时的Connection创建'
        ]},
        {'Conntecion为什么要使用代理模式/装饰者模式':[
            'Conncetion conn = dataSource.getConnection();',
            '一顿骚操作之后...',
            'conn.close();',
            'Connection的close()做法：销毁连接',
            '而我们要将connection.close()方法变成“将Connection归还连接池”，而不是实际关闭',
            '所以使用代理模式/装饰者模式'
        ]}
    ]}
],
'实现思路':[
    {'DataSource':[
        '如com.alibaba.druid.pool.DruidDataSource',
        '项目创建时组装一个连接池，初始化一些Connection的代理放到连接池'
    ]},
    {'JDBCUtil':[
        '获得数据库连接Connection及释放数据库连接Connection',
    ]},
    {'JDBCTemplate':[
        '将获得，释放数据库连接公共出来，提供勾子方法给子类实现',
    ]},
],
'参考':[
    'https://zhuanlan.zhihu.com/p/64827222'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 