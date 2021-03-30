import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("字段")
r2=s2.getRootTopic()
r2.setTitle("字段")


content={
'自增主键':[
    '用自增列作为主键,可以防止页断裂造成的空洞',
    {'自增id':[
        '无符号整型是4个字节，上限是2的32次-1',
        '表定义的自增值达到上限后：再申请下一个id时，得到的值保持不变',
        'InnoDB系统自增row_id,范围从0到2的48次-1'
    ]},
    {'自增值的保存策略':[
        'MyISA：保存在数据文件中',
        {'InnoDB':[
            'AUTO_INCREMENT=n，存在表结构定义中，放在后缀名为.frm 的文件（不会保存自增值）',
            '自增值保存在内存里，MySQL 8.0后有了“自增值持久化”的能力'
        ]}
    ]},
    {'修改机制及不连续原因':[
        'id字段指定为 0、null 或未指定，把当前AUTO_INCREMENT值填到自增字段',
        'id字段指定了具体值，使用指定值',
        {'双M结构':[
            'auto_increment_increment=2',
            '一个库的自增id是奇数，另一个库的自增id是偶数，避免两库生成的主键发生冲突'
        ]},
        '唯一键冲突',
        '事务回滚'
    ]},
    {'innodb_autoinc_lock_mode，默1':[
        '0：语句执行结束后才释放锁',
        {'1':[
            '普通insert语句，自增锁在申请后马上释放',
            '普通insert语句，含多个value值，一次性申请锁，申请完成后锁释放',
            'insert … select批量插入语句，自增锁要等语句结束后才被释放'
        ]},
        '2：所有申请自增主键的动作都是申请后就释放锁'
    ]},
],
'varchar和char的区别':[
    {'char':[
        '定长字段',
        'char(10)的空间:无论实际存储多少内容.该字段都占用10个字符'
    ]},
    {'varchar':[
        '变长',
        '申请的只是最大长度,占用的空间为实际字符长度+1,最后一个字符存储使用的空间长度'
    ]},
    '检索效率上:char > varchar'
],
'varchar(10)和的区别':[
    {'varchar(10)':[
        '申请的空间长度,也是可以存储数据的最大长度',
        '插入需要判断，时间换空间'
    ]},
    {'int(10)':[
        '展示的长度,不足10位以0填充',
        'int(1)和int(10)所能存储的数字大小以及占用的空间都是相同的,只是在展示时按照长度展示'
    ]}
],
'float和double的区别':[
    '精度不同和数据范围不同',
    {'double':[
        '64位,在小数点后到15位'
    ]},
    {'float':[
        '32位,在小数点后到7位'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 